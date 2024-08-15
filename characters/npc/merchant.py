import pygame
import textwrap
from game.inventory import *
from game.settings import *
from game.items import *
import config  # Import the configuration module

class Merchant(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.npcs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        # Load and scale the merchant image
        original_image = pygame.image.load(config.MERCHANT_IMAGE)
        image_width, image_height = original_image.get_size()
        self.image = pygame.transform.scale(original_image, (image_width, image_height))
        self.rect = self.image.get_rect()
        self.x = x * 2
        self.y = y * 2
        self.rect.midbottom = (self.x, self.y)

        self.select_sound = pygame.mixer.Sound(config.SELECT_SOUND)
        self.buying_sound = pygame.mixer.Sound(config.BUYING_SOUND)
        self.talk_sound = pygame.mixer.Sound(config.TALK_SOUND)
        self.talk_sound.set_volume(VOLUME)

        self.play_sound = False
        self.skip_text = False

        self.taco_button_rect = None
        self.flour_button_rect = None
        self.gas_mask_button_rect = None
        self.hp_potion_button_rect = None
        self.close_button_rect = None
        self.counters = []

    def draw(self):
        # Draw the merchant sprite
        self.game.screen.blit(self.image, self.rect)

    def draw_text_box(self, message):
        padding = 20
        text_padding = 10
        line_spacing = 5
        font = pygame.font.Font(config.FONT_PATH, 13)
        snip = font.render('', True, DARKGREY)
        speed = 2

        # Load and scale the text box image
        text_box = pygame.image.load(config.TEXT_BOX_IMAGE)
        text_box_width = int(WIDTH * 3 / 5)
        text_box_x = (WIDTH - text_box_width) // 2
        text_box = pygame.transform.scale(text_box, (text_box_width, 100))

        char_per_line = (text_box_width // (font.size(' ')[0]) - 1)
        lines = textwrap.wrap(message, width=char_per_line)
        self.game.screen.blit(text_box, (text_box_x, HEIGHT - 100 - padding))

        if not self.play_sound:
            self.play_sound = True
            self.talk_sound.play(-1)

        if not self.counters:
            self.counters = [0 for _ in lines]

        for i, line in enumerate(lines):
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
            font = pygame.font.Font(config.FONT_PATH, size)
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
        scaled_menu = pygame.image.load(config.SHOP_MENU_IMAGE)
        pos_x = (self.game.screen.get_width() - scaled_menu.get_width()) // 2
        pos_y = (self.game.screen.get_height() - scaled_menu.get_height()) // 2

        # Define button rectangles
        button_y_offsets = [96, 176, 256, 336]
        button_rects = {
            "taco": pygame.Rect(pos_x + 32, pos_y + button_y_offsets[0], config.BUTTON_WIDTH, config.BUTTON_HEIGHT),
            "flour": pygame.Rect(pos_x + 32, pos_y + button_y_offsets[1], config.BUTTON_WIDTH, config.BUTTON_HEIGHT),
            "gas_mask": pygame.Rect(pos_x + 32, pos_y + button_y_offsets[2], config.BUTTON_WIDTH, config.BUTTON_HEIGHT),
            "hp_potion": pygame.Rect(pos_x + 32, pos_y + button_y_offsets[3], config.BUTTON_WIDTH, config.BUTTON_HEIGHT),
            "close": pygame.Rect(786, 162, 40, 40)
        }

        self.taco_button_rect = button_rects["taco"]
        self.flour_button_rect = button_rects["flour"]
        self.gas_mask_button_rect = button_rects["gas_mask"]
        self.hp_potion_button_rect = button_rects["hp_potion"]
        self.close_button_rect = button_rects["close"]

        self.game.screen.blit(scaled_menu, (pos_x, pos_y))
        text_x = pos_x + scaled_menu.get_width() // 2

        # Draw text and prices
        items = [
            ("Taco", config.TACO_PRICE, button_rects["taco"].topright),
            ("Flour", config.FLOUR_PRICE, button_rects["flour"].topright),
            ("Gas mask", config.GAS_MASK_PRICE, button_rects["gas_mask"].topright),
            ("Hp potion", config.HP_POTION_PRICE, button_rects["hp_potion"].topright)
        ]
        self.draw_text("SHOP", self.game.screen, (text_x + 20, pos_y + 20), 30, LIGHTBROWN, "n")

        for item, price, pos in items:
            self.draw_text(item, self.game.screen, (pos_x - 200, pos[1]), 20, LIGHTBROWN, "nw")
            self.draw_text(str(price), self.game.screen, (pos[0] + 190, pos[1]), 16, LIGHTBROWN, "nw")

    def check_button_click(self, pos):
        self.buying_sound.set_volume(VOLUME)
        items = {
            self.taco_button_rect: (config.TACO_PRICE, Taco),
            self.flour_button_rect: (config.FLOUR_PRICE, Flour),
            self.gas_mask_button_rect: (config.GAS_MASK_PRICE, GasMask),
            self.hp_potion_button_rect: (config.HP_POTION_PRICE, HpPotion)
        }

        for button_rect, (price, item_class) in items.items():
            if button_rect.collidepoint(pos):
                if self.game.player.money >= price:
                    self.buying_sound.play()
                    self.game.player.money -= price
                    item = item_class(self.game)
                    self.game.inventory.add_item(Item(item.name, item.image, 1))
                    print(f"{item.name} purchased, Money: {self.game.player.money}")
                break

        if self.close_button_rect and self.close_button_rect.collidepoint(pos):
            self.select_sound.set_volume(VOLUME)
            self.select_sound.play()
            self.game.talking_merchant = False
            print("Close button clicked")
            self.taco_button_rect = None