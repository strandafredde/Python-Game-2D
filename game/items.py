import pygame

class Pizza(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.items
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = "Pizza"
        original_image = pygame.image.load("assets/items/pizza.png")
        image_width, image_height = original_image.get_size()
        scaled_image = pygame.transform.scale(original_image, (image_width // 40, image_height // 40))
        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.x = x * 2
        self.y = y * 2
        self.rect.midbottom= (self.x, self.y)
        self.width = 32
        self.height = 32
    
    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))


class Sword(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.items
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = "Sword"
        original_image = pygame.image.load("assets/items/sword.png")
        image_width, image_height = original_image.get_size()
        scaled_image = pygame.transform.scale(original_image, (image_width // 30, image_height // 30))
        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.x = x * 2
        self.y = y * 2
        self.rect.midbottom= (self.x, self.y)
        self.width = 32
        self.height = 32
    
    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))