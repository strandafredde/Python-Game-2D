import pygame
import textwrap
from game.inventory import *
from game.settings import *

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
        self.select_sound = pygame.mixer.Sound("assets/sounds/select.wav")
        self.buying_sound = pygame.mixer.Sound("assets/sounds/buying_sound.wav")
        self.taco_button_rect = None
        self.flour_button_rect = None
        self.gas_mask_button_rect = None
        self.hp_potion_button_rect = None
        self.close_button_rect = None
        self.counters = []

        self.talk_sound = pygame.mixer.Sound("e:\\PythonProjects\\Python-Game-2D\\assets\\sounds\\talk.wav")
        self.talk_sound.set_volume(VOLUME)
        self.play_sound = False

    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))

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

        if not self.play_sound:
            self.play_sound = True
            self.talk_sound.play(-1) 
        
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
        
        if all(counter >= speed * len(line) for counter, line in zip(self.counters, lines)):
            self.talk_sound.stop()
            self.play_sound = False

    def draw_text(self, text, surface, position, size, color, alignment="nw"):
            font = pygame.font.Font("e:\\PythonProjects\\Python-Game-2D\\assets\\fonts\\PressStart2P.ttf", size)  # Use the default font
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()

            if alignment == "nw":
                text_rect.topleft = position
            elif alignment == "ne":
                text_rect.topright = position
            elif alignment == "sw":
                text_rect.bottomleft = position
            elif alignment == "se":
                text_rect.bottomright = position
            elif alignment == "n":
                text_rect.midtop = position
            elif alignment == "s":
                text_rect.midbottom = position
            elif alignment == "e":
                text_rect.midright = position
            elif alignment == "w":
                text_rect.midleft = position
            elif alignment == "center":
                text_rect.center = position

            outline_color = BLACK
            outline = 1  # Outline thickness
            outline_surface = font.render(text, True, outline_color)

            # Draw the outline
            for x in range(-outline, outline+1):
                for y in range(-outline, outline+1):
                    surface.blit(outline_surface, (text_rect.x + x, text_rect.y + y))



            surface.blit(text_surface, text_rect)
    def display_shop_menu(self):
        scaled_menu = pygame.image.load("assets/gui/shop_menu2.png")
        #scaled_menu = pygame.transform.scale(og_menu, (og_menu.get_width() // 2.5, og_menu.get_height() // 2.5))

        # Calculate the position to center the menu
        pos_x = (self.game.screen.get_width() - scaled_menu.get_width()) // 2
        pos_y = (self.game.screen.get_height() - scaled_menu.get_height()) // 2

        
        close_button_width = 40
        close_button_height = 40

        close_button_x = 786
        close_button_y = 162

        self.close_button_rect = pygame.Rect(close_button_x, close_button_y, close_button_width, close_button_height)

        self.game.screen.blit(scaled_menu, (pos_x, pos_y))
        text_x = pos_x + scaled_menu.get_width() // 2

        self.taco_button_rect = pygame.Rect(pos_x + 32 , pos_y + 96, 560, 50)
        self.flour_button_rect = pygame.Rect(pos_x + 32, pos_y + 176, 560, 50)
        self.gas_mask_button_rect = pygame.Rect(pos_x + 32, pos_y + 256, 560, 50)
        self.hp_potion_button_rect = pygame.Rect(pos_x + 32, pos_y + 336, 560, 50)
        


        # Draw the text
        self.draw_text("SHOP", self.game.screen, (text_x + 20, pos_y + 20), 30, LIGHTBROWN, "n")
        self.draw_text("Taco", self.game.screen, (text_x - 200, pos_y + 113), 20, LIGHTBROWN, "nw")
        self.draw_text("Flour", self.game.screen, (text_x - 200, pos_y + 194), 20, LIGHTBROWN, "nw")
        self.draw_text("Gas mask", self.game.screen, (text_x - 200, pos_y + 274), 20, LIGHTBROWN, "nw")
        self.draw_text("Hp potion", self.game.screen, (text_x - 200, pos_y + 354), 20, LIGHTBROWN, "nw")
        # Draw the price
        self.draw_text("10", self.game.screen, (text_x + 190, pos_y + 113), 16, LIGHTBROWN, "nw")
        self.draw_text("5", self.game.screen, (text_x + 190, pos_y + 194), 16, LIGHTBROWN, "nw")
        self.draw_text("10", self.game.screen, (text_x + 190, pos_y + 274), 16, LIGHTBROWN, "nw")
        self.draw_text("2", self.game.screen, (text_x + 190, pos_y + 354), 16, LIGHTBROWN, "nw")
        

        # pygame.draw.rect(self.game.screen, (LIGHTBROWN), self.taco_button_rect)
        # pygame.draw.rect(self.game.screen, (LIGHTBROWN), self.flour_button_rect)
        # pygame.draw.rect(self.game.screen, (LIGHTBROWN), self.gas_mask_button_rect)
        # pygame.draw.rect(self.game.screen, (LIGHTBROWN), self.hp_potion_button_rect)
        # pygame.draw.rect(self.game.screen, (GREEN), self.close_button_rect)

    
    def check_button_click(self, pos):
        self.buying_sound.set_volume(VOLUME)
        if self.taco_button_rect is not None and self.taco_button_rect.collidepoint(pos):
            if self.game.player.money >= 5:
                self.buying_sound.play()
                self.game.player.money -= 5
                self.game.inventory.add_item(Item("FLOUR"))
            
            print("Money: ", self.game.player.money)
            print("Buy button clicked: FLOUR")

        elif self.flour_button_rect is not None and self.flour_button_rect.collidepoint(pos):
            if self.game.player.money >= 5:
                self.buying_sound.play()
                self.game.player.money -= 5
                self.game.inventory.add_item(Item("TACO"))

            print("Money: ", self.game.player.money)
            print("Buy button clicked: TACO")

        elif self.gas_mask_button_rect is not None and self.gas_mask_button_rect.collidepoint(pos):
            if self.game.player.money >= 2:
                self.buying_sound.play()
                self.game.player.money -= 2
                self.game.inventory.add_item(Item("HP POTION"))
            
            print("Money: ", self.game.player.money)
            print("Buy button clicked: HP POTION")
        
        elif self.hp_potion_button_rect is not None and self.hp_potion_button_rect.collidepoint(pos):
            if self.game.player.money >= 10:
                self.buying_sound.play()
                self.game.player.money -= 10
                self.game.inventory.add_item(Item("GAS MASK"))
            
            print("Money: ", self.game.player.money)
            print("Buy button clicked: GAS MASK")

        elif self.close_button_rect is not None and self.close_button_rect.collidepoint(pos):
            self.select_sound.set_volume(VOLUME)
            self.select_sound.play()
            self.game.talking_merchant = False
            print("Close button clicked")