import pygame

WIDTH, HEIGHT = 800, 600

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

    def fade(self, mode):
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0, 0, 0))  # Fill with black color
        for i in range(30):
            fade_surface.set_alpha(i * 8 if mode == 'out' else 255 - i * 8)
            self.screen.fill((255, 255, 255))  # Fill the screen with white color
            self.screen.blit(fade_surface, (0, 0))
            pygame.display.flip()
            pygame.time.wait(50)  # Delay to slow down the fade effect

    def run(self):
        while self.running:
            self.screen.fill((255, 255, 255))  # Fill the screen with white color
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.fade('out')
                    if event.key == pygame.K_g:
                        self.fade('in')
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()