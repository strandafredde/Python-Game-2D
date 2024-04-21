import pygame
from game.settings import *
class Item:
    def __init__(self, name, image, quantity=1):
        self.name = name
        self.image = image
        self.quantity = quantity

class Inventory:
    def __init__(self):
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
            font = pygame.font.Font(None, 36)
            text = font.render(f"{i.name}: {i.quantity}", True, (255, 255, 255))
            image = i.image
            image = pygame.transform.scale(image, (48, 48))
            screen.blit(image, (WIDTH//5 + 64 * index, HEIGHT - 64))
        

    def __str__(self):
        return str(self.items)