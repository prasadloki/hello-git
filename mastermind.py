import random

def generate_code():
    return [str(random.randint(0, 9)) for _ in range(4)]

def get_feedback(code, guess):
    correct_pos = sum(c == g for c, g in zip(code, guess))
    common = sum(min(code.count(d), guess.count(d)) for d in set(guess))
    wrong_pos = common - correct_pos
    return correct_pos, wrong_pos

def mastermind():
    print("🎯 Welcome to Mastermind!")
    print("Try to guess the 4-digit secret code (digits 0–9).")
    print("After each guess, you'll get feedback:")
    print("✅ Digits in correct position")
    print("🔁 Correct digits in wrong position")
    print("You have 10 attempts.\n")

    code = generate_code()
    attempts = 10

    for turn in range(1, attempts + 1):
        while True:
            guess = input(f"Attempt {turn}: Enter a 4-digit number: ")
            if len(guess) == 4 and guess.isdigit():
                break
            print("❌ Invalid input. Try again.")

        guess_list = list(guess)
        correct, misplaced = get_feedback(code, guess_list)

        if correct == 4:
            print(f"🎉 You cracked the code in {turn} tries! Code was: {''.join(code)}")
            return

        print(f"✅ Correct position: {correct} | 🔁 Misplaced: {misplaced}\n")

    print(f"💥 Game Over! The code was: {''.join(code)}")

if __name__ == "__main__":
    mastermind()
