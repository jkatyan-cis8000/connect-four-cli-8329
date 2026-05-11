# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- `src/board.py`: 7x6 grid state, column validation, disc placement, win detection (horizontal, vertical, diagonal)
- `src/game.py`: turn management, player state (Player 1/Player 2), game loop, draw detection
- `src/ui.py`: terminal rendering of board, user input parsing (column selection 1-7), move confirmation
- `src/main.py`: entry point, orchestrates game initialization and main loop

## Interfaces

### board.py
- `class Board`: 7 columns x 6 rows grid
  - `__init__()` - initialize empty grid
  - `is_valid_column(col)` -> bool - check if column index is valid (1-7)
  - `get_available_row(col)` -> int | None - find lowest empty row in column
  - `apply_move(col, player)` -> bool - place disc, return True if successful
  - `check_winner()` -> str | None - returns 'Player 1', 'Player 2', or None
  - `is_full()` -> bool - check if grid is completely filled
  - `to_string()` -> str - render board for terminal display

### game.py
- `class Game`: manages game flow
  - `__init__(board)` - initialize with Board instance
  - `current_player()` -> str - returns current player ('Player 1' or 'Player 2')
  - `make_move(col)` -> str | None - process move, returns winner if any
  - `is_game_over()` -> bool - check win or draw condition
  - `get_winner()` -> str | None - returns winning player or 'Draw' or None

### ui.py
- `class UI`: handles terminal I/O
  - `display_board(board)` - render current board state
  - `prompt_for_move(player)` -> int - ask player for column (1-7)
  - `display_invalid_move(message)` - show error for invalid input
  - `display_winner(winner)` - show game result

### main.py
- `main()` - entry point, creates instances, runs game loop

## Shared Data Structures

- **Grid**: 6 rows x 7 columns represented as list of lists
  - Empty cell: `None`
  - Player 1: `'X'`
  - Player 2: `'O'`
- **Column indices**: 1-7 (1-indexed for user input)
- **Player values**: `'Player 1'` and `'Player 2'`
- **Win types**: horizontal, vertical, diagonal (both directions)

## External Dependencies

- No external dependencies - pure Python standard library
- Uses built-in `sys` for potential future expansion
