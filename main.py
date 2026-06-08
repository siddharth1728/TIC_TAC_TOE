from game import (
    board,
    print_board,
    player_move,
    check_winner,
    is_draw
)

from ai import ai_move

print("TIC TAC TOE AI")

while True:

    # Player turn
    print_board()
    player_move("X")

    if check_winner("X"):
        print_board()
        print("🎉 You Win!")
        break

    if is_draw():
        print_board()
        print("🤝 It's a Draw!")
        break

    # AI turn
    move = ai_move(board)
    board[move] = "O"

    print("\n🤖 AI made a move!")

    if check_winner("O"):
        print_board()
        print("🤖 AI Wins!")
        break

    if is_draw():
        print_board()
        print("🤝 It's a Draw!")
        break