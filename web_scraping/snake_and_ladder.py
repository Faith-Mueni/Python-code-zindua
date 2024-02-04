import random

class SnakesAndLaddersGame:
    def __init__(self, board, ladders, snakes, size=10):
        self.size = size
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.board = [0] * (size * size + 1)

    def get_position(self, player):
        return player.position

    def dice_roll(self):
        return random.randint(1, 6)

    def snake_and_ladder(self, player):
        position = self.get_position(player)

        if position in self.ladders:
            player.position = self.ladders[position]
            print(f"{player.name} climbed the ladder from {position} to {self.ladders[position]}!")

        elif position in self.snakes:
            player.position = self.snakes[position]
            print(f"{player.name} got bitten by the snake and moved from {position} to {self.snakes[position]}.")

    def play_turn(self, player):
        dice_value = self.dice_roll()
        player.position += dice_value
        print(f"{player.name} rolled a {dice_value}. Current position: {player.position}")
        self.snake_and_ladder(player)

    def play(self, player1, player2):
        print("Welcome to Snake and Ladder Game.")

        while True:
            input(f"{player1.name}, press Enter to roll the dice...")
            self.play_turn(player1)

            if player1.position >= self.size * self.size:
                print(f"Congratulations! {player1.name} wins!")
                return player1

            input(f"{player2.name}, press Enter to roll the dice...")
            self.play_turn(player2)

            if player2.position >= self.size * self.size:
                print(f"Congratulations! {player2.name} wins!")
                return player2


    player1 = Player("Player 1")
    player2 = Player("Player 2")

    game = SnakesAndLaddersGame(size=10)
    winner = game.play(player1, player2)