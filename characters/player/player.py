import pygame
from game.settings import *
from spritesheet import load_spritesheet
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.load_assets()
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.walk_down[0]
        self.rect = self.image.get_rect() 
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = 64
        self.height = 64
        self.vel = PLAYER_SPEED
        self.vx, self.vy = 0, 0
        self.idle_counter = 0
        self.walking_counter = 0
        self.walking = False

        self.direction = "down"

    def load_assets(self):
        self.walk_down = load_spritesheet("assets/player/main_char_default.png", 64, 64, 10, 1.6)
        self.walk_up = load_spritesheet("assets/player/main_char_default.png", 64, 64, 8, 1.6)
        self.walk_right = load_spritesheet("assets/player/main_char_default.png", 64, 64, 11, 1.6)
        self.walk_left = load_spritesheet("assets/player/main_char_default.png", 64, 64, 9, 1.6)

    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.walking = True
            self.direction = "left"
            self.x -= self.vel * self.game.dt

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.walking = True
            self.direction = "right"
            self.x += self.vel * self.game.dt

        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.walking = True
            self.direction = "up"
            self.y -= self.vel * self.game.dt

        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.walking = True
            self.direction = "down"
            self.y += self.vel * self.game.dt

        
        else:
            self.walking = False

        self.rect.center = (self.x, self.y)


    def update(self):
        self.move()
        self.idle_counter += 1

        self.walking_counter = (self.walking_counter + 1) % 32  # cycle from 0 to 40

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