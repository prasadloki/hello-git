import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)            # Hide cursor
    stdscr.nodelay(True)          # Don't block on getch
    stdscr.keypad(True)           # Enable arrow keys
    sh, sw = stdscr.getmaxyx()

    ship = "🚀"                  
    ship_width = len(ship)
    x = sw // 2                   # Start position
    score = 0
    lives = 3
    asteroids = []

    while lives > 0:
        stdscr.clear()
        stdscr.addstr(0, 2, f"Score: {score}  Lives: {'❤ ' * lives}")

        # Draw the ship
        stdscr.addstr(sh - 2, x, ship)

        # Generate new asteroids
        if random.randint(1, 10) > 6:
            asteroid_x = random.randint(1, sw - 2)
            asteroids.append([0, asteroid_x])

        # Draw and move asteroids
        for a in asteroids:
            a[0] += 1
            if a[0] < sh - 1:
                stdscr.addstr(a[0], a[1], "*")  # You can try "💣" or "☄️", but "*" is safest

        # Check for collisions
        for a in asteroids:
            if a[0] == sh - 2 and x <= a[1] < x + ship_width:
                lives -= 1
                stdscr.addstr(sh - 3, sw // 2 - 5, "💥 HIT! 💥")
                stdscr.refresh()
                time.sleep(0.4)
                asteroids.remove(a)

        # Remove off-screen asteroids
        asteroids = [a for a in asteroids if a[0] < sh - 1]

        # Handle input
        key = stdscr.getch()
        if key == curses.KEY_LEFT and x > 0:
            x -= 2
        elif key == curses.KEY_RIGHT and x < sw - ship_width:
            x += 2

        score += 1
        stdscr.refresh()
        time.sleep(0.06)

    # Game Over
    stdscr.clear()
    stdscr.addstr(sh // 2, sw // 2 - 6, "💀 GAME OVER 💀")
    stdscr.addstr(sh // 2 + 1, sw // 2 - 8, f"Final Score: {score}")
    stdscr.refresh()
    time.sleep(2)

if __name__ == "__main__":
    curses.wrapper(main)

