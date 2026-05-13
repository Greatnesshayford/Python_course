# Required library installation:
# pip install colorama

import random
from colorama import init, Fore, Style

# Initialize colorama
init()

def print_board(board):
    """Print the tic-tac-toe board with colored symbols."""
    print()
    for i in range(3):
        row_display = []
        for j in range(3):
            if board[i][j] == 'X':
                row_display.append(f"{Fore.MAGENTA}X{Style.RESET_ALL}")
            elif board[i][j] == 'O':
                row_display.append(f"{Fore.YELLOW}O{Style.RESET_ALL}")
            else:
                row_display.append(' ')
        print(f" {row_display[0]} | {row_display[1]} | {row_display[2]} ")
        if i < 2:
            print("..." + "." + "..." + "." + "...")
    print()

def check_winner(board, player):
    """Check if the given player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    """Check if the board is full (draw)."""
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    """Get all empty cells on the board."""
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing, alpha, beta):
    """Minimax algorithm with alpha-beta pruning for hard difficulty."""
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            score = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = ' '
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            score = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = ' '
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

def computer_move(board, difficulty):
    """Computer makes a move based on difficulty level."""
    empty_cells = get_empty_cells(board)

    if difficulty == 'easy':
        # Random move
        return random.choice(empty_cells)

    elif difficulty == 'medium':
        # 50% chance of best move, 50% random
        if random.random() < 0.5:
            return random.choice(empty_cells)
        else:
            best_score = float('-inf')
            best_move = None
            for i, j in empty_cells:
                board[i][j] = 'O'
                score = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
            return best_move if best_move else random.choice(empty_cells)

    else:  # hard
        # Always best move using minimax
        best_score = float('-inf')
        best_move = None
        for i, j in empty_cells:
            board[i][j] = 'O'
            score = minimax(board, 0, False, float('-inf'), float('inf'))
            board[i][j] = ' '
            if score > best_score:
                best_score = score
                best_move = (i, j)
        return best_move

def get_player_move(board):
    """Get player's move input."""
    while True:
        try:
            move = input("Enter your move (1-9): ").strip()
            if move.lower() == 'q':
                return None

            move = int(move)
            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue

            # Convert 1-9 to row, col (1 is top-left, 9 is bottom-right)
            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] != ' ':
                print("That cell is already taken!")
                continue

            return row, col
        except ValueError:
            print("Invalid input! Enter a number between 1 and 9.")

def print_position_guide():
    """Show position numbers for reference."""
    print("\nPosition Guide:")
    print(" 1 | 2 | 3 ")
    print("..." + "." + "..." + "." + "...")
    print(" 4 | 5 | 6 ")
    print("..." + "." + "..." + "." + "...")
    print(" 7 | 8 | 9 \n")

def select_difficulty():
    """Let user select difficulty level."""
    print("\nSelect Difficulty Level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice == '1':
            return 'easy'
        elif choice == '2':
            return 'medium'
        elif choice == '3':
            return 'hard'
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

def play_game():
    """Main game loop."""
    print("=" * 40)
    print("       TIC-TAC-TOE")
    print("=" * 40)
    print(f"\nYou are {Fore.MAGENTA}X{Style.RESET_ALL}, Computer is {Fore.YELLOW}O{Style.RESET_ALL}")
    print("Enter 'q' to quit at any time.")

    difficulty = select_difficulty()
    print(f"\nDifficulty set to: {difficulty.upper()}")

    # Initialize empty board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    print_position_guide()

    # Player goes first
    while True:
        # Player's turn
        print_board(board)
        print("Your turn!")

        move = get_player_move(board)
        if move is None:
            print("\nGame quit by player.")
            return

        row, col = move
        board[row][col] = 'X'

        # Check if player wins
        if check_winner(board, 'X'):
            print_board(board)
            print(f"{Fore.MAGENTA}🎉 CONGRATULATIONS! You WIN! 🎉{Style.RESET_ALL}")
            return

        # Check for draw
        if is_board_full(board):
            print_board(board)
            print(f"{Fore.CYAN}It's a DRAW!{Style.RESET_ALL}")
            return

        # Computer's turn
        print(f"\n{Fore.YELLOW}Computer is thinking...{Style.RESET_ALL}")
        comp_row, comp_col = computer_move(board, difficulty)
        board[comp_row][comp_col] = 'O'

        # Check if computer wins
        if check_winner(board, 'O'):
            print_board(board)
            print(f"{Fore.YELLOW}💻 Computer WINS! Better luck next time! 💻{Style.RESET_ALL}")
            return

        # Check for draw
        if is_board_full(board):
            print_board(board)
            print(f"{Fore.CYAN}It's a DRAW!{Style.RESET_ALL}")
            return

if __name__ == "__main__":
    play_game()
