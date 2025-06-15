import random

def load_words():
    with open("words.txt", "r") as f:
        return [word.strip() for word in f.readlines()]

def display_word(secret_word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])

def play_game():
    words = load_words()
    secret_word = random.choice(words).lower()
    guessed_letters = set()
    attempts = 6

    print("🕵️ Welcome to Hangman!")
    
    while attempts > 0:
        print(f"\nWord: {display_word(secret_word, guessed_letters)}")
        print(f"Guessed Letters: {' '.join(sorted(guessed_letters))}")
        print(f"Attempts left: {attempts}")
        
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Invalid input. Enter a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("✅ Correct guess!")
            if all(letter in guessed_letters for letter in secret_word):
                print(f"\n🎉 You won! The word was: {secret_word}")
                break
        else:
            print("❌ Wrong guess.")
            attempts -= 1

    if attempts == 0:
        print(f"\n💀 Game over! The word was: {secret_word}")

if __name__ == "__main__":
    play_game()
