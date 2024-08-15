import pygame
from game.settings import *
import config
class Item:
    def __init__(self, name, image, quantity=1):
        self.name = name
        self.image = image
        self.quantity = quantity

class Inventory:
    def __init__(self, game):
        self.game = game
        self.items = []

    def add_item(self, item):
        for i in self.items:
            if i.name == item.name:
                i.quantity += item.quantity
                return
        self.items.append(item)

    def remove_item(self, item):
        for i in self.items:
            if i.name == item.name:
                i.quantity -= item.quantity
                if i.quantity <= 0:
                    self.items.remove(i)
                return

    def get_item(self, name):
        for i in self.items:
            if i.name == name:
                return i

    def draw(self, screen):
        x = 0
        y = 0
        for i in self.items:
            font = pygame.font.Font(None, 36)
            text = font.render(f"{i.name}: {i.quantity}", True, (255, 255, 255))
            screen.blit(text, (x, y))

            y += 40

    def draw_inventory(self, screen):
        for index, i in enumerate(self.items):
            font = pygame.font.Font(config.FONT_PATH, 13)
            text = font.render(f"{i.quantity}", True, (255, 255, 255))
            image = i.image
            image = pygame.transform.scale(image, (48, 48))
            pygame.draw.rect(screen, (LIGHTGREY), (WIDTH//4 - 8 + 64 * index, HEIGHT - 72, 64, 64))
            if(self.game.player.equipped_sword and i.name == "Sword"):
                print("Drawing equipped sword slot")
                pygame.draw.rect(screen, (LIGHTYELLOW), (WIDTH//4 - 8 + 64 * index, HEIGHT - 72, 64, 64))

            screen.blit(image, (WIDTH//4 + 64 * index, HEIGHT - 64))
            pygame.draw.rect(screen, (DARKGREY), (WIDTH//4 - 8 + 64 * index, HEIGHT - 72, 64, 64), 2)
            screen.blit(text, (WIDTH//4 + 40 + 64 * index, HEIGHT - 24))
    def __str__(self):
        return str(self.items)