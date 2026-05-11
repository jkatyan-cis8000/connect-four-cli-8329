class Board:
    def __init__(self):
        self.columns = 7
        self.rows = 6
        self.grid = [[None for _ in range(self.columns)] for _ in range(self.rows)]

    def is_valid_column(self, col):
        return 1 <= col <= self.columns

    def get_available_row(self, col):
        if not self.is_valid_column(col):
            return None
        actual_col = col - 1
        for row in range(self.rows - 1, -1, -1):
            if self.grid[row][actual_col] is None:
                return row
        return None

    def apply_move(self, col, player):
        row = self.get_available_row(col)
        if row is not None:
            self.grid[row][col - 1] = player
            return True
        return False

    def check_winner(self):
        for row in range(self.rows):
            for col in range(self.columns):
                player = self.grid[row][col]
                if player is None:
                    continue
                if self._check_direction(row, col, player, 0, 1):
                    return player
                if self._check_direction(row, col, player, 1, 0):
                    return player
                if self._check_direction(row, col, player, 1, 1):
                    return player
                if self._check_direction(row, col, player, 1, -1):
                    return player
        return None

    def _check_direction(self, row, col, player, delta_row, delta_col):
        count = 1
        # Check positive direction
        for i in range(1, 4):
            r = row + delta_row * i
            c = col + delta_col * i
            if r < 0 or r >= self.rows or c < 0 or c >= self.columns:
                break
            if self.grid[r][c] != player:
                break
            count += 1
        # Check negative direction
        for i in range(1, 4):
            r = row - delta_row * i
            c = col - delta_col * i
            if r < 0 or r >= self.rows or c < 0 or c >= self.columns:
                break
            if self.grid[r][c] != player:
                break
            count += 1
        return count >= 4

    def is_full(self):
        for col in range(self.columns):
            if self.grid[0][col] is None:
                return False
        return True

    def to_string(self):
        lines = []
        for row in range(self.rows):
            line = "|"
            for col in range(self.columns):
                cell = self.grid[row][col]
                if cell is None:
                    line += " "
                else:
                    line += cell
                line += "|"
            lines.append(line)
        lines.append("-" * (self.columns * 2 + 1))
        header = " " + " ".join(str(i) for i in range(1, self.columns + 1))
        lines.append(header)
        return "\n".join(lines)
