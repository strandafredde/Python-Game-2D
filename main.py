from game.game import Game

def main():
    game = Game()
    while True:
        game.new()
        game.show_start_screen()
        game.run()

if __name__ == "__main__":
    main()