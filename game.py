# game.py

board = [" "] * 9


def print_board():
    print()

    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i + 1]} | {board[i + 2]} ")

        if i < 6:
            print("-----------")

    print()


def player_move(symbol):

    while True:

        try:
            move = int(input(f"Player {symbol}, choose a position (1-9): "))

            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue

            if board[move - 1] == "X" or board[move - 1] == "O":
                print("Position already taken.")
                continue

            board[move - 1] = symbol
            break

        except ValueError:
            print("Please enter a valid number.")


def check_winner(symbol):
    
    winning_combinations = [
        [0, 1, 2],  # Row 1
        [3, 4, 5],  # Row 2
        [6, 7, 8],  # Row 3
        [0, 3, 6],  # Col 1
        [1, 4, 7],  # Col 2
        [2, 5, 8],  # Col 3
        [0, 4, 8],  # Diagonal
        [2, 4, 6]   # Diagonal
    ]

    for combo in winning_combinations:
        if all(board[i] == symbol for i in combo):
            return True

    return False

def is_draw():
    
    for cell in board:
        if cell not in ["X", "O"]:
            return False

    return True