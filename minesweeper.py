import random

def create_board(size, bombs):
    board = [['0' for _ in range(size)] for _ in range(size)]
    bomb_locations = set()

    while len(bomb_locations) < bombs:
        r = random.randint(0, size - 1)
        c = random.randint(0, size - 1)
        if (r, c) not in bomb_locations:
            bomb_locations.add((r, c))
            board[r][c] = 'B'

    # Fill numbers
    for r in range(size):
        for c in range(size):
            if board[r][c] == 'B':
                continue
            count = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < size and 0 <= nc < size and board[nr][nc] == 'B':
                        count += 1
            board[r][c] = str(count)
    
    return board, bomb_locations

def print_visible_board(visible):
    print("\n   " + " ".join(str(i) for i in range(len(visible))))
    for i, row in enumerate(visible):
        print(f"{i:2} " + " ".join(row))
    print()

def play_game(size=6, bombs=6):
    real_board, bomb_set = create_board(size, bombs)
    visible = [['*' for _ in range(size)] for _ in range(size)]

    print("💣 Welcome to Terminal Minesweeper!")
    print("Uncover cells without hitting a bomb!")
    print("Type coordinates as `row col` (e.g. 1 3)")

    while True:
        print_visible_board(visible)

        try:
            move = input("Enter cell to uncover: ")
            r, c = map(int, move.strip().split())

            if (r < 0 or r >= size or c < 0 or c >= size):
                print("❌ Invalid cell. Try again.")
                continue

            if real_board[r][c] == 'B':
                print("💥 Boom! You hit a bomb.")
                print("Final board:")
                for i in range(size):
                    for j in range(size):
                        visible[i][j] = real_board[i][j]
                print_visible_board(visible)
                break
            else:
                visible[r][c] = real_board[r][c]

            # Check win
            unrevealed = sum(row.count('*') for row in visible)
            if unrevealed == bombs:
                print("🎉 You win! All safe cells uncovered.")
                print_visible_board(visible)
                break

        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    play_game()
