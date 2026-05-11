from .board import Board
from .game import Game


class UI:
    def display_board(self, board):
        print(board.to_string())

    def prompt_for_move(self, player):
        while True:
            try:
                move = input(f"Player {player}, enter column (1-7): ").strip()
                col = int(move)
                if 1 <= col <= 7:
                    return col
                else:
                    self.display_invalid_move("Column must be between 1 and 7")
            except ValueError:
                self.display_invalid_move("Invalid input. Please enter a number between 1 and 7")

    def display_invalid_move(self, message):
        print(f"Error: {message}")

    def display_winner(self, winner):
        if winner == "Draw":
            print("Game over! It's a draw!")
        else:
            print(f"{winner} wins!")


def main():
    board = Board()
    game = Game(board)
    ui = UI()

    while not game.is_game_over():
        ui.display_board(board)
        player = game.current_player()
        col = ui.prompt_for_move(player)
        
        try:
            result = game.make_move(col)
            if result:
                break
        except ValueError as e:
            ui.display_invalid_move(str(e))

    ui.display_board(board)
    winner = game.get_winner()
    ui.display_winner(winner)


if __name__ == "__main__":
    main()
