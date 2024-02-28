from game.game import Game

def main():
    game = Game()
    while True:
        game.new()
        game.run()

if __name__ == "__main__":
    main()