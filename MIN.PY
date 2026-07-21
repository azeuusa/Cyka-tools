import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def bot_move(board):
    # Simple AI: first try to win, then block, then random
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

    # Check for winning move
    for r, c in empty_cells:
        temp_board = [row[:] for row in board]
        temp_board[r][c] = "O"
        if check_winner(temp_board) == "O":
            return r, c

    # Block player's winning move
    for r, c in empty_cells:
        temp_board = [row[:] for row in board]
        temp_board[r][c] = "X"
        if check_winner(temp_board) == "X":
            return r, c

    # Random move
    return random.choice(empty_cells)

def tictactoe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("You are X, the bot is O.")
    print("Enter row (0-2) and column (0-2) to make your move.")

    while True:
        print_board(board)

        if current_player == "X":
            try:
                row = int(input("Your turn (row): "))
                col = int(input("Your turn (column): "))
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Please enter numbers between 0 and 2.")
                    continue
                if board[row][col] != " ":
                    print("That spot is already taken!")
                    continue
            except ValueError:
                print("Please enter valid numbers!")
                continue
        else:
            print("Bot's turn...")
            row, col = bot_move(board)
            print(f"Bot chooses row {row}, column {col}")

        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tictactoe()