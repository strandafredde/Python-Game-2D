from os import path
import sys
import pygame

from characters.player.player import *
from characters.npc.arthur import *
from characters.npc.walter import *
from characters.npc.merchant import *
from characters.monsters.fly import *

from .items import *
from .inventory import *
from .tilemap import *
from .settings import *

#sprite for collision
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height):
        self.groups = game.obstacles
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x*2, y*2, width*2, height*2)
        self.x = x * 2
        self.y = y * 2
        self.rect.x = self.x
        self.rect.y = self.y

class Door(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height, tp_x, tp_y):
        self.groups = game.doors
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pygame.Rect(x*2, y*2, width*2, height*2)
        self.x = x * 2
        self.y = y * 2
        self.rect.x = self.x
        self.rect.y = self.y
        self.tp_x = tp_x * 2
        self.tp_y = tp_y * 2

    
def text_box(self, text):
    padding = 20  # Space from the sides and the bottom
    text_padding = 10  # Space from the text to the text box
    line_spacing = 5  # Space between lines

    # Create a Surface for the text box
    text_box = pygame.Surface((WIDTH - 2 * padding, 100), pygame.SRCALPHA)  # Use SRCALPHA to allow transparent background
    text_box.fill((0, 0, 0, 0))  # Fill the text box with transparent color

    # Create a rounded border for the text box
    border = pygame.Rect(0, 0, WIDTH - 2 * padding, 100)
    pygame.draw.rect(text_box, BROWN, border, 0, border_radius=10)

    # Create a smaller rounded rectangle for the inner part of the text box
    inner_rect = pygame.Rect(2, 2, WIDTH - 2 * padding - 4, 96)
    pygame.draw.rect(text_box, WHITE, inner_rect, 0, border_radius=10)

    # Create a font object
    font = pygame.font.Font('freesansbold.ttf', 20)

    # Split the text into words
    words = text.split(' ')
    lines = ['']
    line_index = 0

    # Add words to lines
    for word in words:
        if lines[line_index]:  # If the current line is not empty, add a space before the word
            temp_line = lines[line_index] + ' ' + word
        else:  # If the current line is empty, add the word without a space
            temp_line = lines[line_index] + word
        temp_surface = font.render(temp_line, True, BLACK)
        if temp_surface.get_width() <= text_box.get_width() - 2 * text_padding:
            lines[line_index] = temp_line
        else:
            lines.append(word)
            line_index += 1

    # Render the lines and blit them onto the text box Surface
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, BLACK)
        text_rect = text_surface.get_rect(left=text_padding, top=text_padding + i * (font.get_height() + line_spacing))
        text_box.blit(text_surface, text_rect)

    # Blit the text box Surface onto the screen with space from the sides and the bottom
    self.screen.blit(text_box, (padding, HEIGHT - 100 - padding))  # padding pixels space from the sides and the bottom# Initialize the game

def text_box2(self, text, y):
    padding = 20  # Space from the sides and the bottom
    text_padding = 10  # Space from the text to the text box
    line_spacing = 5  # Space between lines

    # Create a Surface for the text box
    text_box = pygame.Surface((WIDTH - 2 * padding, 100), pygame.SRCALPHA)  # Use SRCALPHA to allow transparent background
    text_box.fill((0, 0, 0, 0))  # Fill the text box with transparent color

    # Create a rounded border for the text box
    border = pygame.Rect(0, 0, WIDTH - 2 * padding, 100)
    pygame.draw.rect(text_box, BROWN, border, 0, border_radius=10)

    # Create a smaller rounded rectangle for the inner part of the text box
    inner_rect = pygame.Rect(2, 2, WIDTH - 2 * padding - 4, 96)
    pygame.draw.rect(text_box, WHITE, inner_rect, 0, border_radius=10)

    # Create a font object
    font = pygame.font.Font('freesansbold.ttf', 20)

    # Split the text into words
    words = text.split(' ')
    lines = ['']
    line_index = 0

    # Add words to lines
    for word in words:
        if lines[line_index]:  # If the current line is not empty, add a space before the word
            temp_line = lines[line_index] + ' ' + word
        else:  # If the current line is empty, add the word without a space
            temp_line = lines[line_index] + word
        temp_surface = font.render(temp_line, True, BLACK)
        if temp_surface.get_width() <= text_box.get_width() - 2 * text_padding:
            lines[line_index] = temp_line
        else:
            lines.append(word)
            line_index += 1

    # Render the lines and blit them onto the text box Surface
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, BLACK)
        text_rect = text_surface.get_rect(left=text_padding, top=text_padding + i * (font.get_height() + line_spacing))
        text_box.blit(text_surface, text_rect)
    
    # Blit the text box Surface onto the screen with space from the sides and the bottom
    self.screen.blit(text_box, (padding, y))  # padding pixels space from the sides and the bottom# Initialize the game


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.fade_active = False 
        self.fade_alpha = 0
        self.door_opened = False
        self.swung_sword = False
        self.talking_arthur = False
        self.talking_walter = False
        self.talking_merchant = False
        self.text_box_state_walter = "closed"
        self.text_box_state_arthur = "closed"
        self.text_box_state_merchant = "closed"
        self.talk_counter_walter = 0
        self.talk_counter_arthur = 0
        self.talked_to_walter = False
        self.mouse_button_down = False
        self.button_click_in_progress = False
        self.buttons = []

    def load_data(self):
        # Load all game data. This method is called when the game is started.
        try:
            self.open_door = pygame.mixer.Sound("e:\\PythonProjects\\Python-Game-2D\\assets\\sounds\\door_open.wav")
            self.town_music = pygame.mixer.Sound("e:\\PythonProjects\\Python-Game-2D\\assets\\sounds\\littleroot_town_music.wav")
            self.sword_swing = pygame.mixer.Sound("e:\\PythonProjects\\Python-Game-2D\\assets\\sounds\\sword_swing.wav")
            print("Game data loaded successfully")
        except Exception as e:
            print("Cannot load game data: " + str(e))


    def new(self):
        # Initialize a new game. This method is called when a new game is started.
        self.load_data()
        self.inventory = Inventory()

        # Create sprite groups which is used to draw and update sprites
        self.all_sprites = pygame.sprite.Group()
        self.npcs = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.items = pygame.sprite.Group()

        map_folder = path.join("e:\\PythonProjects\\Python-Game-2D\\scenes\\base_map")

        # Load the maps and create the map images
        self.map = TiledMap(path.join(map_folder, "main_map.tmx"))
        self.map_img = self.map.make_map("base_layer")
        self.map_img2 = self.map.make_map("detail_layer")
        self.map_img3 = self.map.make_map("second_detail_layer")
        self.map_img_last = self.map.make_map("walkbehind_layer")

        self.map_rect = self.map_img.get_rect()
        
        # Places the objects on the map in the correct location depending on the object name
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == "arthur":
                self.arthur = Arthur(self, tile_object.x, tile_object.y)
            if tile_object.name == "walter":
                self.walter = Walter(self, tile_object.x, tile_object.y)
            if tile_object.name == "merchant":
                self.merchant = Merchant(self, tile_object.x, tile_object.y)
            if tile_object.name == "fly":
                Fly(self, tile_object.x, tile_object.y)

            if tile_object.name == "player":
                self.player = Player(self, tile_object.x, tile_object.y)
            if tile_object.name == "border":
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)



            if tile_object.name == "pizza":
                Pizza(self, tile_object.x, tile_object.y)

            if tile_object.name == "sword":
                Sword(self, tile_object.x, tile_object.y)

            # Teleportation to doors, both enter and exit
            if tile_object.name == "rv_door":
                tp_x = 0  # Default teleportation coordinates
                tp_y = 0
                for tp_object in self.map.tmxdata.objects:
                    if tp_object.name == "rv_door_inside":
                        tp_x = tp_object.x
                        tp_y = tp_object.y
                        #door to exit the rv
                        Door(self, tp_object.x, tp_object.y, tp_object.width, tp_object.height , tile_object.x + tile_object.width / 2, tile_object.y + tile_object.height + 25)
                        break
                #door to enter the rv
                Door(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height, tp_x + tp_object.width/2, tp_y)

            if tile_object.name == "start_door":
                tp_x = 0  # Default teleportation coordinates
                tp_y = 0
                for tp_object in self.map.tmxdata.objects:
                    if tp_object.name == "start_door_inside":
                        tp_x = tp_object.x
                        tp_y = tp_object.y
                        #door to exit the rv
                        Door(self, tp_object.x, tp_object.y, tp_object.width, tp_object.height , tile_object.x + tile_object.width / 2, tile_object.y + tile_object.height + 25)
                        break
                #door to enter the rv
                Door(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height, tp_x + tp_object.width/2, tp_y)


            if tile_object.name == "second_door_outside":
                tp_x = 0  # Default teleportation coordinates
                tp_y = 0
                for tp_object in self.map.tmxdata.objects:
                    if tp_object.name == "second_door_inside":
                        tp_x = tp_object.x
                        tp_y = tp_object.y
                        #door to exit the rv
                        Door(self, tp_object.x, tp_object.y, tp_object.width, tp_object.height , tile_object.x + tile_object.width / 2, tile_object.y + tile_object.height + 25)
                        break
                #door to enter the rv
                Door(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height, tp_x + tp_object.width/2, tp_y)

        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False

        #self.town_music.set_volume(VOLUME)
        #self.town_music.play(loops=-1)

    def run(self):
        # This is the main game loop. It continues to run as long as the game is active.
        # It handles events, updates the game state, and draws the game to the screen.
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000 
            self.events()
            self.update()
            self.draw()
           
    def quit(self):
        pygame.quit()
        sys.exit()  

    def update(self):
        # This method updates the game. It could be used to update counters, check for collisions, etc.
        
        self.npcs.update()
        self.monsters.update()
        self.all_sprites.update()
        self.camera.update(self.player)
        enter_doors = pygame.sprite.spritecollide(self.player, self.doors, False, collide_hit_rect)
        for door in enter_doors:  # Iterate over all collided doors
            print("Player collided with door")
            if not self.door_opened:
                self.open_door.set_volume(VOLUME)
                self.open_door.play(loops=0)
                self.door_opened = True
            
            self.fade_active = True
            self.player.x = door.tp_x
            self.player.y = door.tp_y
        
        if not enter_doors:
            self.door_opened = False
            
        if self.player.swinging_sword:
            if not self.swung_sword:
                self.sword_swing.set_volume(0.05)
                self.sword_swing.play(loops=0)
                self.swung_sword = True
                self.player.swing_sword()

        if not self.player.swinging_sword:
            self.swung_sword = False
        
        talk_to_npc = pygame.sprite.spritecollide(self.player, self.npcs, False, collide_hit_rect)
        for npc in talk_to_npc:
            if self.player.direction == "up":
                if npc == self.arthur:
                    self.near_arthur = True
                if npc == self.walter:
                    self.near_walter = True
                if npc == self.merchant:
                    self.near_merchant = True
        
        if not talk_to_npc:
            self.near_arthur = False
            self.talking_arthur = False
            self.talking_merchant = False

            self.talking_walter = False
            self.near_walter = False
            self.near_merchant = False
        
        item_pickup = pygame.sprite.spritecollide(self.player, self.items, False, collide_hit_rect)
        for item in item_pickup:
            print("Player picked up item")
            self.inventory.add_item(Item(item.name, 1))
            if item.name == "Sword":
                self.player.has_sword = True
                print("sword: ", self.player.equipped_sword)
            item.kill()
        
        

    def fade_out(self):
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))  # Fill with black color
        fade_surface.set_alpha(self.fade_alpha)
        self.screen.blit(fade_surface, (0, 0))
        self.fade_alpha += 5  # Increase the alpha value to make the fade effect progress'
        #print("Alpha:", self.fade_alpha)
        if self.fade_alpha >= 255:
            #print("Alpha:", self.fade_alpha)
            self.fade_active = False
            self.fade_alpha = 0  # Reset the alpha value for the next fade effect
    


    def draw(self):
        # This method draws the game to the screen.
        # It could clear the screen, draw game objects, draw the UI, etc.



        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        self.screen.blit(self.map_img2, self.camera.apply_rect(self.map_rect))
        self.screen.blit(self.map_img3, self.camera.apply_rect(self.map_rect))

        # Draw all sprites
        for sprite in self.npcs:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        for sprite in self.items:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        for sprite in self.all_sprites:
            if sprite == self.player and self.player.equipped_sword:
                pos = self.camera.apply(sprite)
                adjusted_pos = (pos[0] - 102.5, pos[1] - 102.5)  # Adjust the x position
                self.screen.blit(sprite.image, adjusted_pos)

            else:
                if not self.player.equipped_sword:
                    self.screen.blit(sprite.image, self.camera.apply(sprite))
                

                if sprite != self.player:
                    self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pygame.draw.rect(self.screen, RED, self.camera.apply_rect(sprite.hit_rect ))

        for sprite in self.monsters:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pygame.draw.rect(self.screen, RED, self.camera.apply_rect(sprite.hit_rect))

        self.screen.blit(self.map_img_last, self.camera.apply_rect(self.map_rect))

        if self.draw_debug:
            for obstacle in self.obstacles:
                pygame.draw.rect(self.screen, RED, self.camera.apply_rect(obstacle.rect))
            
            for door in self.doors:
                pygame.draw.rect(self.screen, GREEN, self.camera.apply_rect(door.rect))

        self.player.hp_bar()
        if self.fade_active:
            self.fade_out()

        #talking to arthur
        if self.talking_arthur and self.player.direction == "up":
            if self.talked_to_walter == False:
                print("Arthur: Hello, I'm Arthur")
                text_box(self, "Hey there Mister I'm Arthur!")

            if self.talked_to_walter == True:
                if self.text_box_state_arthur == 'closed':
                    text_box(self, "Hey there Mister I'm Arthur! I heard you're helping Walter. I have a hazmat suit that you can have. I'll give it to you if you can find me a taco.")
                    self.talk_counter_arthur += 1
                elif self.text_box_state_arthur == 'first':
                    text_box(self, "I need you to get me a taco. You can find it at the local market.")
                    self.talk_counter_arthur += 1
                
                if self.inventory.get_item("TACO"):
                    text_box(self, "Thanks for the taco! Here's the hazmat suit.")
                    self.inventory.remove_item(Item("TACO"))
                    self.inventory.add_item(Item("HAZMAT SUIT"))
                    

        #talking to walter
        if self.talking_walter and self.player.direction == "up":
            if self.text_box_state_walter == 'closed':
                text_box(self, "Hello, I'm Walter White. I'm a high school chemistry teacher. I have cancer and I need to make money for my family. I'm going to start cooking and i need your help")
                self.talk_counter_walter += 1
            elif self.text_box_state_walter == 'first':
                self.talked_to_walter = True
                text_box(self, "I need you to help me gather supplies. I need a gas mask, a hazmat suit, and some flour. Arthur might got a hazmat suit. You can find the flour and gasmask at the local market.")
                
     
        #talking to merchant
        if self.talking_merchant and self.player.direction == "up":
            if self.text_box_state_merchant == 'closed':
                #text_box(self, "Welcome to my shop! I have a variety of items for sale. What can I get you?")
                self.merchant.display_shop_menu()

        if not self.player.direction == "up":
            self.talking_arthur = False
            self.talking_walter = False
            self.talking_merchant = False

        self.inventory.draw(self.screen)

        pygame.display.flip()  # Update the display


    def events(self):
         # This method handles events.
        # It could handle input from the player, respond to game events, etc.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_h:
                    self.draw_debug = not self.draw_debug
                if event.key == pygame.K_x:
                    #talking to arthur
                    if self.near_arthur:
                        self.talking_arthur = not self.talking_arthur
                        if self.talk_counter_arthur >= 1:
                            self.text_box_state_arthur = 'first'
                    
                    #talking to walter
                    if self.near_walter:
                        print(self.talk_counter_walter)
                        if self.text_box_state_walter == 'closed':
                            self.talking_walter = True
                            if self.talk_counter_walter >= 1:
                                self.text_box_state_walter = 'first'
                        elif self.text_box_state_walter == 'first':
                            self.talking_walter = not self.talking_walter
                            
                    #talking to merchant
                    if self.near_merchant:
                        self.talking_merchant = not self.talking_merchant
                if event.key == pygame.K_p:
                    print("adding item")
                    self.inventory.add_item(Item("potion"))
                

                if event.key == pygame.K_1:
                    if self.inventory.get_item("Sword") and self.player.has_sword:
                        self.player.equipped_sword = not self.player.equipped_sword
                        print("sword: ", self.player.equipped_sword)
                
                if event.key == pygame.K_SPACE:
                    if self.player.equipped_sword:
                        self.player.swinging_sword = True
                        print("pressed space")
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    print("Mouse button up: ", event.pos)
                    self.merchant.check_button_click(event.pos)
            
            