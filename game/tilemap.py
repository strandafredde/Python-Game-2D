import pygame
import pytmx
from .settings import *

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

class TiledMap():
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.scale_factor = 1  # Change this to zoom in or out
        self.width = tm.width * tm.tilewidth * self.scale_factor
        self.height = tm.height * tm.tileheight * self.scale_factor
        self.tmxdata = tm
    
    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid # get image for certain tile
        scale_factor = 1  # Change this to zoom in or out
        for layer in self.tmxdata.visible_layers:  # loop through all visible layers
            if isinstance(layer, pytmx.TiledTileLayer):  # check if layer is a tile layer
                print(layer.name)
                for x, y, gid in layer:  # loop through all tiles in the layer
                    tile = ti(gid)  # get the image for the tile 
                    if tile:  # if the tile exists draw it
                        tile = pygame.transform.scale(tile, (self.tmxdata.tilewidth * scale_factor, self.tmxdata.tileheight * scale_factor))
                        surface.blit(tile, (x * self.tmxdata.tilewidth * scale_factor, y * self.tmxdata.tileheight * scale_factor))
    
    def make_map(self):
        temp_surface = pygame.Surface((self.width, self.height)) # create a temporary surface 
        self.render(temp_surface) # render the map to the temporary surface
        return temp_surface
    
class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.scale_factor = 1

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width * self.scale_factor - WIDTH), x)  # right
        y = max(-(self.height * self.scale_factor - HEIGHT), y)  # bottom
        self.camera = pygame.Rect(x, y, self.width * self.scale_factor, self.height * self.scale_factor)