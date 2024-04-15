import pygame
import time
import textwrap
from game.settings import *

class Arthur(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.npcs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        original_image = pygame.image.load("assets/npc/arthur.png")
        image_width, image_height = original_image.get_size()
        scaled_image = pygame.transform.scale(original_image, (image_width // 3, image_height // 3))
        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.x = x * 2
        self.y = y * 2
        self.rect.midbottom= (self.x, self.y)
        self.width = 40
        self.height = 64
        self.counters = []
        self.talk_sound = pygame.mixer.Sound("e:\\PythonProjects\\Python-Game-2D\\assets\\sounds\\talk.wav")
        self.talk_sound.set_volume(VOLUME)

    def draw_text_box(self, message):
        padding = 20  # Space from the sides and the bottom
        text_padding = 10  # Space from the text to the text box
        line_spacing = 5  # Space between lines
        font = pygame.font.Font("e:\\PythonProjects\\Python-Game-2D\\assets\\fonts\\PressStart2P.ttf", 13)
        timer = pygame.time.Clock()
        snip = font.render('', True, DARKGREY)
        
        speed = 3
        done = False
        text_box = pygame.image.load("e:\\PythonProjects\\Python-Game-2D\\assets\\gui\\text_box.png")

        # Adjust the width of the text box to be 3/5 of the screen width
        text_box_width = int(WIDTH * 3 / 5)
        # Calculate the x-coordinate to center the text box
        text_box_x = (WIDTH - text_box_width) // 2
        # Scale the image to the desired size
        text_box = pygame.transform.scale(text_box, (text_box_width, 100))
        # Calculate the maximum number of characters that can fit in a line
        char_per_line = (text_box_width // (font.size(' ')[0]) -1)

        # Split the message into lines
        lines = textwrap.wrap(message, width=char_per_line)
        self.game.screen.blit(text_box, (text_box_x, HEIGHT - 100 - padding))

        if not self.counters:
            self.counters = [0 for _ in lines]

        # Render and blit each line
        for i, line in enumerate(lines):
            # Only start rendering the next line when the current line is fully rendered
            if i > 0 and self.counters[i - 1] < speed * len(lines[i - 1]):
                break

            if self.counters[i] < speed * len(line):
                self.counters[i] += 1

            snip = font.render(line[:self.counters[i] // speed], True, DARKGREY)
            self.game.screen.blit(snip, (text_box_x + text_padding, HEIGHT - 100 - padding + text_padding + i * (font.get_height() + line_spacing)))
        
    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))
    
