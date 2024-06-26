from game.game import Game
import pygame
import os
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

resource_path('assets/npc/arthur.png')
def main():

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    game = Game()
    while True:
        game.new()
        game.show_start_screen()
        pygame.event.clear()
        game.run()


if __name__ == "__main__":
    main()