import pygame
from game.inventory import *


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
        self.buy1_button_rect = None
        self.buy2_button_rect = None
        self.buy3_button_rect = None
        self.close_button_rect = None
        
    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))
    
    def display_shop_menu(self):
        og_menu = pygame.image.load("assets/gui/shop_menu.png")
        scaled_menu = pygame.transform.scale(og_menu, (og_menu.get_width() // 2.5, og_menu.get_height() // 2.5))

        # Calculate the position to center the menu
        pos_x = (self.game.screen.get_width() - scaled_menu.get_width()) // 2
        pos_y = (self.game.screen.get_height() - scaled_menu.get_height()) // 2

        #buttons
        buy_button_width = 160 // 2.5
        buy_button_height = 70 // 2.5

        buy_button_x = 200
        buy_button_y = 300 # +55 second button +110 third button etc

        close_button_width = 40
        close_button_height = 40

        close_button_x = 838
        close_button_y = 150

        self.buy1_button_rect = pygame.Rect(buy_button_x, buy_button_y, buy_button_width, buy_button_height)
        self.buy2_button_rect = pygame.Rect(buy_button_x, buy_button_y + 55, buy_button_width, buy_button_height )
        self.buy3_button_rect = pygame.Rect(buy_button_x, buy_button_y + 110, buy_button_width, buy_button_height)
        
        self.close_button_rect = pygame.Rect(close_button_x, close_button_y, close_button_width, close_button_height)

        pygame.draw.rect(self.game.screen, (0, 0, 0), self.buy1_button_rect)
    
        self.game.screen.blit(scaled_menu, (pos_x, pos_y))

        #pygame.draw.rect(self.game.screen, (0, 0, 0), self.buy1_button_rect)
        #pygame.draw.rect(self.game.screen, (0, 0, 0), self.buy2_button_rect)
        #pygame.draw.rect(self.game.screen, (0, 0, 0), self.buy3_button_rect)
    
    def check_button_click(self, pos):
        if self.buy1_button_rect is not None and self.buy1_button_rect.collidepoint(pos):
            if self.game.player.money >= 5:
                self.game.player.money -= 15
                self.game.inventory.add_item(Item("FLOUR"))
            
            print("Money: ", self.game.player.money)
            print("Buy button clicked: FLOUR")

        elif self.buy2_button_rect is not None and self.buy2_button_rect.collidepoint(pos):
            if self.game.player.money >= 5:
                self.game.player.money -= 5
                self.game.inventory.add_item(Item("TACO"))

            print("Money: ", self.game.player.money)
            print("Buy button clicked: TACO")

        elif self.buy3_button_rect is not None and self.buy3_button_rect.collidepoint(pos):
            if self.game.player.money >= 2:
                self.game.player.money -= 2
                self.game.inventory.add_item(Item("HP POTION"))
            
            print("Money: ", self.game.player.money)
            print("Buy button clicked: HP POTION")
        
        elif self.close_button_rect is not None and self.close_button_rect.collidepoint(pos):
            self.game.talking_merchant = False
            print("Close button clicked")