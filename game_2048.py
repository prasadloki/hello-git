import random
import os

def print_board(board):
    os.system("cls" if os.name == "nt" else "clear")
    print("\n2048 Game\n")
    for row in board:
        print("+----"*4 + "+")
        print("".join(f"|{str(num).center(4) if num else '    '}" for num in row) + "|")
    print("+----"*4 + "+")

def add_new_tile(board):
    empty = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if empty:
        r, c = random.choice(empty)
        board[r][c] = 2 if random.random() < 0.9 else 4

def compress(row):
    new_row = [num for num in row if num != 0]
    new_row += [0] * (4 - len(new_row))
    return new_row

def merge(row):
    for i in range(3):
        if row[i] != 0 and row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0
    return row

def move_left(board):
    changed = False
    new_board = []
    for row in board:
        compressed = compress(row)
        merged = merge(compressed)
        final = compress(merged)
        if final != row:
            changed = True
        new_board.append(final)
    return new_board, changed

def move_right(board):
    reversed_board = [row[::-1] for row in board]
    moved, changed = move_left(reversed_board)
    return [row[::-1] for row in moved], changed

def move_up(board):
    transposed = list(zip(*board))
    moved, changed = move_left([list(row) for row in transposed])
    return [list(row) for row in zip(*moved)], changed

def move_down(board):
    transposed = list(zip(*board))
    moved, changed = move_right([list(row) for row in transposed])
    return [list(row) for row in zip(*moved)], changed

def has_moves(board):
    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:
                return True
            if c < 3 and board[r][c] == board[r][c+1]:
                return True
            if r < 3 and board[r][c] == board[r+1][c]:
                return True
    return False

def game():
    board = [[0]*4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)

    while True:
        print_board(board)

        move = input("Move (WASD): ").lower()
        if move not in ['w', 'a', 's', 'd']:
            continue

        if move == 'a':
            board, changed = move_left(board)
        elif move == 'd':
            board, changed = move_right(board)
        elif move == 'w':
            board, changed = move_up(board)
        elif move == 's':
            board, changed = move_down(board)

        if changed:
            add_new_tile(board)

        if any(2048 in row for row in board):
            print_board(board)
            print("🎉 You reached 2048! You win!")
            break

        if not has_moves(board):
            print_board(board)
            print("💀 No more moves! Game over!")
            break

if __name__ == "__main__":
    game()
