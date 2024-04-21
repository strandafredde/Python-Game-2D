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

class Coin(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.items
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = "Coin"
        original_image = pygame.image.load("assets/items/coin.png")
        image_width, image_height = original_image.get_size()
        scaled_image = pygame.transform.scale(original_image, (image_width // 10, image_height // 10))
        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.midbottom= (self.x, self.y)
        self.width = 32
        self.height = 32
        print(self.image)
        print(self.rect.midbottom)
    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))

class Taco(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.items
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = "Taco"
        original_image = pygame.image.load("assets/items/taco.png")
        self.image = original_image
        self.rect = self.image.get_rect()
        self.width = 32
        self.height = 32
        print(self.image)
        print(self.rect.midbottom)
    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))

class Flour(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.items
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = "Flour"
        original_image = pygame.image.load("assets/items/flour.png")
        self.image = original_image
        self.rect = self.image.get_rect() 
        self.width = 32
        self.height = 32
        print(self.image)
        print(self.rect.midbottom)
    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))

class GasMask(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.items
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = "GasMask"
        original_image = pygame.image.load("assets/items/gas_mask.png")
        self.image = original_image 
        self.rect = self.image.get_rect()
        self.width = 32
        self.height = 32
        print(self.image)
        print(self.rect.midbottom)
    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))

class HazmatSuit(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.items
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = "HazmatSuit"
        original_image = pygame.image.load("assets/items/hazmat_suit.png")
        self.image = original_image
        self.rect = self.image.get_rect()
        self.width = 32
        self.height = 32
        print(self.image)
        print(self.rect.midbottom)
    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))

class HpPotion(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.items
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = "HpPotion"
        original_image = pygame.image.load("assets/items/hp_potion.png")
        self.image = original_image
        self.rect = self.image.get_rect()
        self.width = 32
        self.height = 32
        print(self.image)
        print(self.rect.midbottom)
        
    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))

