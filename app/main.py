import random

def guess_game():
    number = random.randint(1, 100)
    attempts = 0
    print("🎮 Welcome to the Guessing Game!")

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            if guess < number:
                print("📉 Too low!")
            elif guess > number:
                print("📈 Too high!")
            else:
                print(f"🎯 Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Enter a valid number.")

if __name__ == "__main__":
    guess_game()
