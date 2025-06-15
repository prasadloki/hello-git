import curses
from random import randint

# Initialize screen
screen = curses.initscr()
curses.curs_set(0)
sh, sw = screen.getmaxyx()
win = curses.newwin(sh, sw, 0, 0)
win.keypad(1)
win.timeout(100)

# Initial snake and food
snake = [[sh//2, sw//4 + i] for i in range(3)][::-1]
food = [randint(1, sh - 2), randint(1, sw - 2)]
win.addch(food[0], food[1], '🍎')

# Game loop
key = curses.KEY_RIGHT
score = 0

while True:
    next_key = win.getch()
    key = key if next_key == -1 else next_key

    # Calculate new head
    y, x = snake[0]
    if key == curses.KEY_DOWN: y += 1
    if key == curses.KEY_UP: y -= 1
    if key == curses.KEY_LEFT: x -= 1
    if key == curses.KEY_RIGHT: x += 1

    new_head = [y, x]

    # Game over conditions
    if (y in [0, sh] or x in [0, sw] or new_head in snake):
        curses.endwin()
        print(f"\nGame Over! Final Score: {score}")
        break

    snake.insert(0, new_head)

    if new_head == food:
        score += 1
        food = [randint(1, sh - 2), randint(1, sw - 2)]
        win.addch(food[0], food[1], '🍎')
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    win.addch(snake[0][0], snake[0][1], '🐍')
