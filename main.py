from game.game import Game
import pygame
def main():
    game = Game()
    while True:
        game.new()
        game.show_start_screen()
        pygame.event.clear()
        game.run()

if __name__ == "__main__":
    main()