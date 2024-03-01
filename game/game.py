from os import path
import pygame
from .settings import *
from characters.player.player import *
from .tilemap import *

# Initialize the game

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True


    def new(self):
        # Initialize a new game. This method is called when a new game is started.
        self.all_sprites = pygame.sprite.Group()

        map_folder = path.join("e:\\PythonProjects\\Python-Game-2D\\scenes\\base_map")
        self.map = TiledMap(path.join(map_folder, "2Dmap.tmx"))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

        self.player = Player(self, 130, 100)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        # This is the main game loop. It continues to run as long as the game is active.
        # It handles events, updates the game state, and draws the game to the screen.
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000 
            self.events()
            self.update()
            self.draw()
    def update(self):
        # This method updates the game state.
        # It could move game objects, check for collisions, update the score, etc.
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        # This method draws the game to the screen.
        # It could clear the screen, draw game objects, draw the UI, etc.

        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()  # Update the display

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
        # This method handles events.
        # It could handle input from the player, respond to game events, etc.
    





