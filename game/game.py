from os import path
import sys
import pygame
from .settings import *
from characters.player.player import *
from characters.npc.arthur import *

from .tilemap import *

#sprite for collision
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height):
        self.groups = game.obstacles
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x*2, y*2, width*2, height*2)
        self.x = x * 2
        self.y = y * 2
        self.rect.x = self.x
        self.rect.y = self.y


class Door(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height, tp_x, tp_y):
        self.groups = game.doors
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x*2, y*2, width*2, height*2)
        self.x = x * 2
        self.y = y * 2
        self.rect.x = self.x
        self.rect.y = self.y
        self.tp_x = tp_x * 2
        self.tp_y = tp_y * 2

def text_box(self, text):
    padding = 20  # Space from the sides and the bottom
    text_padding = 10  # Space from the text to the text box

    # Create a Surface for the text box
    text_box = pygame.Surface((WIDTH - 2 * padding, 100), pygame.SRCALPHA)  # Use SRCALPHA to allow transparent background
    text_box.fill((0, 0, 0, 0))  # Fill the text box with transparent color

    # Create a rounded border for the text box
    border = pygame.Rect(0, 0, WIDTH - 2 * padding, 100)
    pygame.draw.rect(text_box, BROWN, border, 0, border_radius=10)

    # Create a smaller rounded rectangle for the inner part of the text box
    inner_rect = pygame.Rect(2, 2, WIDTH - 2 * padding - 4, 96)
    pygame.draw.rect(text_box, WHITE, inner_rect, 0, border_radius=10)

    # Create a font object
    font = pygame.font.Font('freesansbold.ttf', 25)  

    # Render the text onto a new Surface
    text_surface = font.render(text, True, BLACK)  

    # Calculate the position of the text (top corner of the left side of the text box)
    text_rect = text_surface.get_rect(left=text_padding, top=text_padding)

    # Blit the text Surface onto the text box Surface
    text_box.blit(text_surface, text_rect)

    # Blit the text box Surface onto the screen with space from the sides and the bottom
    self.screen.blit(text_box, (padding, HEIGHT - 100 - padding))  # padding pixels space from the sides and the bottom
# Initialize the game
class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.fade_active = False 
        self.fade_alpha = 0
        self.door_opened = False
        self.talking_arthur = False


    def load_data(self):
        # Load all game data. This method is called when the game is started.
        try:
            self.open_door = pygame.mixer.Sound("e:\\PythonProjects\\Python-Game-2D\\assets\\sounds\\door_open.wav")
            self.town_music = pygame.mixer.Sound("e:\\PythonProjects\\Python-Game-2D\\assets\\sounds\\littleroot_town_music.wav")
            print("Game data loaded successfully")
        except:
            print("Cannot load game data")


    def new(self):
        # Initialize a new game. This method is called when a new game is started.
        self.load_data()

        self.all_sprites = pygame.sprite.Group()
        self.npcs = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()

        map_folder = path.join("e:\\PythonProjects\\Python-Game-2D\\scenes\\base_map")

        self.map = TiledMap(path.join(map_folder, "main_map.tmx"))
        self.map_img = self.map.make_map("base_layer")
        self.map_img2 = self.map.make_map("detail_layer")
        self.map_img3 = self.map.make_map("second_detail_layer")
        self.map_img_last = self.map.make_map("walkbehind_layer")

        self.map_rect = self.map_img.get_rect()
        

        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == "arthur":
                self.arthur = Arthur(self, tile_object.x, tile_object.y)
            if tile_object.name == "player":
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == "border":
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == "rv_door":
                tp_x = 0  # Default teleportation coordinates
                tp_y = 0
                for tp_object in self.map.tmxdata.objects:
                    if tp_object.name == "rv_door_inside":
                        tp_x = tp_object.x
                        tp_y = tp_object.y
                        #door to exit the rv
                        Door(self, tp_object.x, tp_object.y, tp_object.width, tp_object.height , tile_object.x + tile_object.width / 2, tile_object.y + tile_object.height + 25)
                        break
                #door to enter the rv
                Door(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height, tp_x + tp_object.width/2, tp_y)

            if tile_object.name == "start_door":
                tp_x = 0  # Default teleportation coordinates
                tp_y = 0
                for tp_object in self.map.tmxdata.objects:
                    if tp_object.name == "start_door_inside":
                        tp_x = tp_object.x
                        tp_y = tp_object.y
                        #door to exit the rv
                        Door(self, tp_object.x, tp_object.y, tp_object.width, tp_object.height , tile_object.x + tile_object.width / 2, tile_object.y + tile_object.height + 25)
                        break
                #door to enter the rv
                Door(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height, tp_x + tp_object.width/2, tp_y)


            if tile_object.name == "second_door_outside":
                tp_x = 0  # Default teleportation coordinates
                tp_y = 0
                for tp_object in self.map.tmxdata.objects:
                    if tp_object.name == "second_door_inside":
                        tp_x = tp_object.x
                        tp_y = tp_object.y
                        #door to exit the rv
                        Door(self, tp_object.x, tp_object.y, tp_object.width, tp_object.height , tile_object.x + tile_object.width / 2, tile_object.y + tile_object.height + 25)
                        break
                #door to enter the rv
                Door(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height, tp_x + tp_object.width/2, tp_y)

        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False

        self.town_music.set_volume(VOLUME)
        self.town_music.play(loops=-1)

    def run(self):
        # This is the main game loop. It continues to run as long as the game is active.
        # It handles events, updates the game state, and draws the game to the screen.
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000 
            self.events()
            self.update()
            
            self.draw()
           
    def quit(self):
        pygame.quit()
        sys.exit()  

    def update(self):
        # This method updates the game. It could be used to update counters, check for collisions, etc.
        
        self.npcs.update()
        self.all_sprites.update()
        self.camera.update(self.player)
        enter_doors = pygame.sprite.spritecollide(self.player, self.doors, False, collide_hit_rect)
        for door in enter_doors:  # Iterate over all collided doors
            print("Player collided with door")
            if not self.door_opened:
                self.open_door.set_volume(VOLUME)
                self.open_door.play(loops=0)
                self.door_opened = True
            
            self.fade_active = True
            self.player.x = door.tp_x
            self.player.y = door.tp_y
        
        if not enter_doors:
            self.door_opened = False
            

        
        talk_to_arthur = pygame.sprite.spritecollide(self.player, self.npcs, False, collide_hit_rect)
        if talk_to_arthur:
            if self.player.direction == "up":
                self.near_arthur = True

        if not talk_to_arthur:
            self.near_arthur = False
            self.talking_arthur = False

    def fade_out(self):
        print("Fading out")
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))  # Fill with black color
        fade_surface.set_alpha(self.fade_alpha)
        self.screen.blit(fade_surface, (0, 0))
        self.fade_alpha += 5  # Increase the alpha value to make the fade effect progress'
        print("Alpha:", self.fade_alpha)
        if self.fade_alpha >= 255:
            print("Alpha:", self.fade_alpha)
            self.fade_active = False
            self.fade_alpha = 0  # Reset the alpha value for the next fade effect
        
    def draw(self):
        # This method draws the game to the screen.
        # It could clear the screen, draw game objects, draw the UI, etc.



        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        self.screen.blit(self.map_img2, self.camera.apply_rect(self.map_rect))
        self.screen.blit(self.map_img3, self.camera.apply_rect(self.map_rect))

        for sprite in self.npcs:
            self.screen.blit(sprite.image, self.camera.apply(sprite))


        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pygame.draw.rect(self.screen, RED, self.camera.apply_rect(sprite.hit_rect ))

        self.screen.blit(self.map_img_last, self.camera.apply_rect(self.map_rect))

        if self.draw_debug:
            for obstacle in self.obstacles:
                pygame.draw.rect(self.screen, RED, self.camera.apply_rect(obstacle.rect))
            
            for door in self.doors:
                pygame.draw.rect(self.screen, GREEN, self.camera.apply_rect(door.rect))

        if self.fade_active:
            self.fade_out()

        if self.talking_arthur and self.player.direction == "up":
            print("Arthur: Hello, I'm Arthur")
            text_box(self, "Hey there Mister I'm Arthur!")
            
        pygame.display.flip()  # Update the display




    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_h:
                    self.draw_debug = not self.draw_debug
                if event.key == pygame.K_x:
                    if self.near_arthur:
                        print("Arthur: Hello, I'm Arthur")
                        self.talking_arthur = not self.talking_arthur
                        print(self.talking_arthur)



        # This method handles events.
        # It could handle input from the player, respond to game events, etc.