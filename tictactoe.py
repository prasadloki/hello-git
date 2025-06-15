def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current = 'X'

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        try:
            move = input(f"Player {current}, enter your move (row,col): ")
            row, col = map(int, move.split(','))

            if board[row][col] != ' ':
                print("Cell already taken! Try again.")
                continue

            board[row][col] = current
            print_board(board)

            winner = check_winner(board)
            if winner:
                print(f"🎉 Player {winner} wins!")
                break

            if is_draw(board):
                print("It's a draw!")
                break

            current = 'O' if current == 'X' else 'X'
        except (ValueError, IndexError):
            print("Invalid input. Enter row,col (0-2).")

if __name__ == "__main__":
    play_game()
