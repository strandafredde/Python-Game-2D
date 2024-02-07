import pygame
from .settings import *
from characters.player.player import *
# Initialize the game

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDHT, HEIGHT))
        self.running = True


    def new(self):
        # Initialize a new game. This method is called when a new game is started.
        player = Player(self, 50, 50)


    def run(self):
        # This is the main game loop. It continues to run as long as the game is active.
        # It handles events, updates the game state, and draws the game to the screen.
        while self.running:
            self.events()
            self.update()
            self.draw()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def update(self):
        # This method updates the game state.
        # It could move game objects, check for collisions, update the score, etc.
        pass

    def draw(self):
        # This method draws the game to the screen.
        # It could clear the screen, draw game objects, draw the UI, etc.
        pass

    def events(self):
        # This method handles events.
        # It could handle input from the player, respond to game events, etc.
        pass






