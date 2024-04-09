import pygame
from spritesheet import *

class Fly(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.load_assets()
        self.groups = game.monsters
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.flying[0]
        self.rect = self.image.get_rect() 
        self.x = x * 2
        self.y = y * 2
        self.rect.midbottom= (self.x, self.y)
        self.width = 64
        self.height = 64
        self.frame_speed = 40
        self.counter = 0
        self.health= 20
        self.dying_sound = False
        self.last_hit_time = 0

    def load_assets(self): 
        try:
            self.fly_dying = pygame.mixer.Sound("e:\\PythonProjects\\Python-Game-2D\\assets\\sounds\\fly_dying.wav")
            self.flying = load_spritesheet("assets/npc/fly.png", 32, 32, 0, 3)
            self.dying = load_spritesheet("assets/npc/fly.png", 32, 32, 3, 3)
            self.hurt = pygame.mixer.Sound("assets/sounds/hurt.wav")
            print("Game data loaded successfully")
        except Exception as e:
            print("Cannot load game data: " + str(e))


    def update(self):
        #Updates info about the fly
        if self.health > 0:
            self.move_towards_player()
            self.counter = self.counter + 1 % self.frame_speed
            self.flying_counter = (self.counter // 12) % 3
            self.image = self.flying[self.flying_counter]

        if self.health <= 0:
            self.counter = (self.counter + 1) % self.frame_speed
            self.dying_counter = ((self.counter // 12) + 3) % len(self.dying)
            self.image = self.dying[self.dying_counter]
            if self.dying_sound == False:
                self.fly_dying.set_volume(0.1)
                self.fly_dying.play()
                self.dying_sound = True
            if self.dying_counter == len(self.dying) - 1:
                self.kill()
        
        if self.rect.colliderect(self.game.player.hit_rect):
            now = pygame.time.get_ticks()
            if now - self.last_hit_time > 1000:  # 1000 milliseconds = 1 second
                self.hurt.set_volume(0.1)
                self.hurt.play()
                self.game.player.health -= 10
                print(self.game.player.health)
                self.last_hit_time = now
    def move_towards_player(self):
        #Make the fly move towards the player if the player is within 400 pixels
        if abs(self.game.player.rect.x - self.rect.x) < 400:
            if self.game.player.rect.x + 20 < self.rect.x:
                self.rect.x -= 1
            elif self.game.player.rect.x - 20 > self.rect.x:
                self.rect.x += 1
        if abs(self.game.player.rect.y - self.rect.y) < 400:
            if self.game.player.rect.y + 20 < self.rect.y:
                self.rect.y -= 1
            elif self.game.player.rect.y - 20 > self.rect.y:
                self.rect.y += 1

    def draw(self):
        pygame.draw.rect(self.game.screen, (self.x, self.y, self.width, self.height))
    
