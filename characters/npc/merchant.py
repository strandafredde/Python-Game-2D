import pygame


class Merchant(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.npcs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        original_image = pygame.image.load("assets/npc/merchant.png")
        image_width, image_height = original_image.get_size()
        scaled_image = pygame.transform.scale(original_image, (image_width, image_height))
        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.x = x * 2
        self.y = y * 2
        self.rect.midbottom= (self.x, self.y)
        self.width = 40
        self.height = 64
    
    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))
    
