import tkinter as tk
from tkinter import messagebox
from ai import ai_move, check_winner, is_draw
window = tk.Tk()

window.title("Tic Tac Toe AI")
window.geometry("500x600")

buttons = []

board = [""] * 9
player_score = 0
ai_score = 0
draw_score = 0

def reset_board():
    
    global board

    board = [""] * 9

    for button in buttons:
        button.config(text="")

def button_click(index):

    # Ignore already occupied cells
    if board[index] != "":
        return

    # Player move
    board[index] = "X"
    buttons[index].config(text="X")

    # Check if board is full
    if "" not in board:
        return

    # AI move
    ai_index = ai_move(board)

    if ai_index is not None:
        board[ai_index] = "O"
        buttons[ai_index].config(text="O")


title = tk.Label(
    window,
    text="Tic Tac Toe AI",
    font=("Arial", 24, "bold")
)

title.pack(pady=20)

score_label = tk.Label(
    window,
    text="Player: 0 | AI: 0 | Draws: 0",
    font=("Arial", 14)
)

score_label.pack(pady=10)

restart_button = tk.Button(
    window,
    text="Restart Game",
    font=("Arial", 12),
    command=reset_board
)

restart_button.pack(pady=10)


frame = tk.Frame(window)
frame.pack()

for row in range(3):

    for col in range(3):

        index = row * 3 + col

        button = tk.Button(
            frame,
            text="",
            width=4,
            height=2,
            font=("Arial", 28, "bold"),
            command=lambda i=index: button_click(i)
        )

        button.grid(
            row=row,
            column=col,
            padx=5,
            pady=5
        )

        buttons.append(button)

window.mainloop()