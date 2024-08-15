import pygame
import textwrap
from game.settings import *
import config

class Walter(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.npcs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        # Load and scale the Walter image
        original_image = pygame.image.load(config.WALTER_IMAGE)
        image_width, image_height = original_image.get_size()
        self.image = pygame.transform.scale(original_image, (image_width // 4, image_height // 4))
        self.rect = self.image.get_rect()
        self.x = x * 2
        self.y = y * 2
        self.rect.midbottom = (self.x, self.y)

        self.width = 40
        self.height = 64
        self.counters = []
        self.speed = 2

        self.talk_sound = pygame.mixer.Sound(config.TALK_SOUND)
        self.talk_sound.set_volume(VOLUME)
        self.play_sound = False

    def draw_text_box(self, message):
        self.game.play_sound = False
        padding = 20  # Space from the sides and the bottom
        text_padding = 10  # Space from the text to the text box
        line_spacing = 5  # Space between lines
        font = pygame.font.Font(config.FONT_PATH, 13)

        text_box = pygame.image.load(config.TEXT_BOX_IMAGE)
        text_box_width = int(WIDTH * config.TEXT_BOX_WIDTH_RATIO)
        text_box_x = (WIDTH - text_box_width) // 2
        text_box = pygame.transform.scale(text_box, (text_box_width, config.TEXT_BOX_HEIGHT))

        char_per_line = (text_box_width // (font.size(' ')[0])) - 1
        lines = textwrap.wrap(message, width=char_per_line)
        self.game.screen.blit(text_box, (text_box_x, HEIGHT - config.TEXT_BOX_HEIGHT - padding))

        if not self.counters:
            self.counters = [0 for _ in lines]

        if not self.play_sound:
            self.play_sound = True
            self.talk_sound.play(-1)

        for i, line in enumerate(lines):
            if i > 0 and self.counters[i - 1] < self.speed * len(lines[i - 1]):
                break

            if self.counters[i] < self.speed * len(line):
                self.counters[i] += 1

            snip = font.render(line[:self.counters[i] // self.speed], True, DARKGREY)
            self.game.screen.blit(
                snip,
                (
                    text_box_x + text_padding,
                    HEIGHT - config.TEXT_BOX_HEIGHT - padding + text_padding + i * (font.get_height() + line_spacing)
                ),
            )

        if all(counter >= self.speed * len(line) for counter, line in zip(self.counters, lines)):
            self.talk_sound.stop()
            self.play_sound = False

    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))
