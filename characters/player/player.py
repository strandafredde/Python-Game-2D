import pygame
from game.settings import *
from spritesheet import *
from game.tilemap import *




class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.load_assets()
        self.groups =  game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.scale_factor = 1
        self.game = game
        self.image = self.walk_down[0]
        self.rect = self.image.get_rect() 
        self.x = x * 2 # multiply by 2 to scale the player same as the tilemap
        self.y = y * 2 # multiply by 2 to scale the player same as the tilemap
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.midbottom = self.rect.midbottom
        self.width = 64
        self.height = 64
        self.vel = PLAYER_SPEED
        self.vx, self.vy = 0, 0
        self.idle_counter = 0
        self.walking_counter = 0
        self.walking = False
        self.frame_speed = 40
        self.direction = "down"
        self.teleporting = False
        self.money = 100
        self.has_sword = False
        self.equipped_sword = False
        self.swinging_sword = False
        self.health = 100
        self.sword_size = 48
        
    

    def load_assets(self):
        # #normal
        self.walk_down = load_spritesheet("assets/player/main_char_default.png", 64, 64, 10, 1.6)
        self.walk_up = load_spritesheet("assets/player/main_char_default.png", 64, 64, 8, 1.6)
        self.walk_right = load_spritesheet("assets/player/main_char_default.png", 64, 64, 11, 1.6)
        self.walk_left = load_spritesheet("assets/player/main_char_default.png", 64, 64, 9, 1.6)

        #sword
        self.walk_down_sword = load_spritesheet("assets/player/sword/main_character_sword_walk.png", 192, 192, 2, 1.6)
        self.walk_up_sword = load_spritesheet("assets/player/sword/main_character_sword_walk.png", 192, 192, 0, 1.6)
        self.walk_right_sword = load_spritesheet("assets/player/sword/main_character_sword_walk.png", 192, 192, 3, 1.6,)
        self.walk_left_sword = load_spritesheet("assets/player/sword/main_character_sword_walk.png", 192, 192, 1, 1.6)

        self.walk_down_sword_idle = load_spritesheet("assets/player/sword/main_character_sword_idle.png", 192, 192, 2, 1.6)
        self.walk_up_sword_idle = load_spritesheet("assets/player/sword/main_character_sword_idle.png", 192, 192, 0, 1.6)
        self.walk_right_sword_idle = load_spritesheet("assets/player/sword/main_character_sword_idle.png", 192, 192, 3, 1.6)
        self.walk_left_sword_idle = load_spritesheet("assets/player/sword/main_character_sword_idle.png", 192, 192, 1, 1.6)

        self.swing_sword_down = load_spritesheet("assets/player/sword/main_character_sword_slash.png", 192, 192, 2, 1.6)
        self.swing_sword_up = load_spritesheet("assets/player/sword/main_character_sword_slash.png", 192, 192, 0, 1.6)
        self.swing_sword_right = load_spritesheet("assets/player/sword/main_character_sword_slash.png", 192, 192, 3, 1.6)
        self.swing_sword_left = load_spritesheet("assets/player/sword/main_character_sword_slash.png", 192, 192, 1, 1.6)

        self.hit_hurt_fly = pygame.mixer.Sound("assets/sounds/hit_hurt_fly.wav")   

        self.coin_image = pygame.image.load("assets/items/coin.png").convert_alpha()
        self.coin_image = pygame.transform.scale(self.coin_image, (self.coin_image.get_width() // 10, self.coin_image.get_height() // 10))
        print("Player assets loaded")
        print(self.walk_left_sword)
        print(len(self.walk_left_sword))
        print(len(self.walk_up_sword_idle))
        print(self.walk_up_sword_idle)

    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))
        
    def draw_money(self):
        font = pygame.font.Font("e:\\PythonProjects\\Python-Game-2D\\assets\\fonts\\PressStart2P.ttf", 20)
        self.game.screen.blit(self.coin_image, (10, 44))
        money_text = font.render(f"{self.game.player.money}", True, WHITE)
        self.game.screen.blit(money_text, (50, 50))
        
    def swing_sword(self):
    # Create a new hit rectangle for the sword
        if self.direction == "up":
            self.sword_rect = pygame.Rect(self.hit_rect.x, self.hit_rect.y - self.sword_size, self.rect.width, self.sword_size)
        elif self.direction == "down":
             self.sword_rect = pygame.Rect(self.hit_rect.x, self.hit_rect.bottom, self.rect.width, self.sword_size)
        elif self.direction == "left":
             self.sword_rect = pygame.Rect(self.hit_rect.x - self.sword_size, self.rect.y, self.sword_size, self.rect.height)
        elif self.direction == "right":
             self.sword_rect = pygame.Rect(self.hit_rect.right, self.rect.y, self.sword_size, self.rect.height)

        hits = [fly for fly in self.game.monsters if  self.sword_rect.colliderect(fly.hit_rect)]
        for fly in hits:
            print("Hit the fly")
            self.hit_hurt_fly.set_volume(VOLUME)
            self.hit_hurt_fly.play()
            fly.is_hit = True
            fly.health -= SWORD_DAMAGE # Or however much damage you want the sword to do
   
    def collide_with_obstacles(self, dir):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.obstacles, False, collide_hit_rect)
            if hits:
                if hits[0].rect.centerx > self.hit_rect.centerx:
                    self.x = hits[0].rect.left - self.hit_rect.width / 2
                if hits[0].rect.centerx < self.hit_rect.centerx:
                    self.x = hits[0].rect.right + self.hit_rect.width / 2
                self.vx = 0
                self.hit_rect.centerx = self.x
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.obstacles, False, collide_hit_rect)
            if hits:
                if hits[0].rect.bottom > self.hit_rect.bottom:
                    self.y = hits[0].rect.top 
                if hits[0].rect.bottom < self.hit_rect.bottom:
                    self.y = hits[0].rect.bottom + self.hit_rect.height 
                self.vy = 0
                self.rect.bottom = self.y

    def move(self):
        if self.swinging_sword:
            return
        if not self.game.fade_active:

            keys = pygame.key.get_pressed()
            vx, vy = 0, 0
            if not self.game.is_fading:
                if not self.game.is_paused:
                    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                        vx = -self.vel * self.game.dt
                    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                        vx = self.vel * self.game.dt
                    elif keys[pygame.K_UP] or keys[pygame.K_w]:
                        vy = -self.vel * self.game.dt
                    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                        vy = self.vel * self.game.dt

            if keys[pygame.K_LSHIFT]:
                self.vel = PLAYER_SPEED * 2
                self.frame_speed = 20
            if not keys[pygame.K_LSHIFT]:
                self.vel = PLAYER_SPEED
                self.frame_speed = 40

            if not self.game.fade_active:  # Only update position if a fade is not active
                # Move along the x axis and handle collisions
                self.x += vx
                self.rect.midbottom = (self.x, self.y)
                self.hit_rect.midbottom = self.rect.midbottom
                self.collide_with_obstacles('x')

                # Move along the y axis and handle collisions
                self.y += vy
                self.rect.midbottom = (self.x, self.y)
                self.hit_rect.midbottom = self.rect.midbottom
                self.collide_with_obstacles('y')

            if vx != 0 or vy != 0:
                self.walking = True
            else:
                self.walking = False

            if vx < 0:
                self.direction = "left"
            elif vx > 0:
                self.direction = "right"
            elif vy < 0:
                self.direction = "up"
            elif vy > 0:
                self.direction = "down"
                    
    def update(self):
        if not self.game.fade_active:
            self.move()
            self.idle_counter += 1

            self.walking_counter = (self.walking_counter + 1) % self.frame_speed  
            
            if self.swinging_sword and self.equipped_sword:
                #print("Swinging sword")
                self.walking = False
                
                frame_sword = (self.walking_counter // 5) % 5
                if self.direction == "down":
                    self.image = self.swing_sword_down[frame_sword]
                elif self.direction == "up":
                    self.image = self.swing_sword_up[frame_sword]
                elif self.direction == "left":
                    self.image = self.swing_sword_left[frame_sword]
                elif self.direction == "right":
                    self.image = self.swing_sword_right[frame_sword]
                if frame_sword >= 4:
                    #print("Done swinging sword")
                    self.swinging_sword = False

            elif self.walking :
                self.idle_counter = 0
                frame_horizontal = (self.walking_counter // 6) % 9 + 1  
                frame_vertical = (self.walking_counter // 6) % 8 + 1  

                frame_sword = (self.walking_counter // 6) % 8
                if not self.equipped_sword:
                    if self.direction == "down":
                        self.image = self.walk_down[frame_vertical]
                    elif self.direction == "up":
                        self.image = self.walk_up[frame_vertical]
                    elif self.direction == "left":
                        self.image = self.walk_left[frame_horizontal]
                    elif self.direction == "right":
                        self.image = self.walk_right[frame_horizontal]
                
                if self.equipped_sword:
                    if self.direction == "down":
                        self.image = self.walk_down_sword[frame_sword]
                    elif self.direction == "up":
                        self.image = self.walk_up_sword[frame_sword]
                    elif self.direction == "left":
                        self.image = self.walk_left_sword[frame_sword]
                    elif self.direction == "right":
                        self.image = self.walk_right_sword[frame_sword]

            else:
                self.walking_counter = 0
                if not self.equipped_sword:
                    if self.direction == "down":
                        if self.idle_counter % 60 < 40:
                            self.image = self.walk_down[0]
                        else:
                            self.image = self.walk_down[10]
                    
                    elif self.direction == "up":
                        if self.idle_counter % 60 < 40:
                            self.image = self.walk_up[0]
                        else:
                            self.image = self.walk_up[10]
                    
                    elif self.direction == "left":
                        if self.idle_counter % 60 < 40:
                            self.image = self.walk_left[0]
                        else:
                            self.image = self.walk_left[10]
                    
                    elif self.direction == "right":
                        if self.idle_counter % 60 < 40:
                            self.image = self.walk_right[0]
                        else:
                            self.image = self.walk_right[10]
                
                if self.equipped_sword:
                    if self.direction == "down":
                        if self.idle_counter % 60 < 40:
                            self.image = self.walk_down_sword_idle[0]
                        else:
                            self.image = self.walk_down_sword_idle[1]
                    
                    elif self.direction == "up":
                        if self.idle_counter % 60 < 40:
                            self.image = self.walk_up_sword_idle[0]
                        else:
                            self.image = self.walk_up_sword_idle[1]
                    
                    elif self.direction == "left":
                        if self.idle_counter % 60 < 40:
                            self.image = self.walk_left_sword_idle[0]
                        else:
                            self.image = self.walk_left_sword_idle[1]
                    
                    elif self.direction == "right":
                        if self.idle_counter % 60 < 40:
                            self.image = self.walk_right_sword_idle[0]
                        else:
                            self.image = self.walk_right_sword_idle[1]
                    