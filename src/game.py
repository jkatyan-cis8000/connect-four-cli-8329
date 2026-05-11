class Game:
    def __init__(self, board):
        self.board = board
        self.current_player_value = 'X'
        self.player_names = {'X': 'Player 1', 'O': 'Player 2'}

    def current_player(self):
        return self.player_names[self.current_player_value]

    def make_move(self, col):
        if not self.board.is_valid_column(col):
            raise ValueError(f"Invalid column: {col}. Must be between 1 and 7")
        
        if self.board.get_available_row(col) is None:
            raise ValueError(f"Column {col} is full")
        
        if self.board.apply_move(col, self.current_player_value):
            winner = self.board.check_winner()
            if winner:
                return self.player_names[winner]
            if self.board.is_full():
                return 'Draw'
            self.current_player_value = 'O' if self.current_player_value == 'X' else 'X'
        return None

    def is_game_over(self):
        return self.board.check_winner() is not None or self.board.is_full()

    def get_winner(self):
        winner = self.board.check_winner()
        if winner:
            return self.player_names[winner]
        if self.board.is_full():
            return 'Draw'
        return None
