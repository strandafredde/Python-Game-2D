import pygame
from game.settings import *
from spritesheet import load_spritesheet
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
        
    def load_assets(self):
        self.walk_down = load_spritesheet("assets/player/main_char_default.png", 64, 64, 10, 1.6)
        self.walk_up = load_spritesheet("assets/player/main_char_default.png", 64, 64, 8, 1.6)
        self.walk_right = load_spritesheet("assets/player/main_char_default.png", 64, 64, 11, 1.6)
        self.walk_left = load_spritesheet("assets/player/main_char_default.png", 64, 64, 9, 1.6)

    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))
        
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
        if not self.game.fade_active:

            keys = pygame.key.get_pressed()
            vx, vy = 0, 0

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

            if self.walking:
                self.idle_counter = 0
                frame = (self.walking_counter // 4) + 1  # get the current frame, now you have 10 images per direction
                if self.direction == "down":
                    self.image = self.walk_down[frame]
                elif self.direction == "up":
                    self.image = self.walk_up[frame]
                elif self.direction == "left":
                    self.image = self.walk_left[frame]
                elif self.direction == "right":
                    self.image = self.walk_right[frame]

            else:
                self.walking_counter = 0
                if self.direction == "down":
                    if self.idle_counter % 60 < 30:
                        self.image = self.walk_down[0]
                    else:
                        self.image = self.walk_down[10]
                
                elif self.direction == "up":
                    if self.idle_counter % 60 < 30:
                        self.image = self.walk_up[0]
                    else:
                        self.image = self.walk_up[10]
                
                elif self.direction == "left":
                    if self.idle_counter % 60 < 30:
                        self.image = self.walk_left[0]
                    else:
                        self.image = self.walk_left[10]
                
                elif self.direction == "right":
                    if self.idle_counter % 60 < 30:
                        self.image = self.walk_right[0]
                    else:
                        self.image = self.walk_right[10]

                
