import random

print("🎰 Welcome to the Jackpot Game! 🎰")
print("Choose difficulty level:")
print("1. Easy (20 attempts)")
print("2. Medium (10 attempts)")
print("3. Difficult (5 attempts)")

level = input("Enter level (1/2/3): ")

# set attempts based on level
if level == "1":
    attempts = 20
elif level == "2":
    attempts = 10
elif level == "3":
    attempts = 5
else:
    print("Invalid choice, defaulting to Medium level.")
    attempts = 10

# generate random jackpot number between 1 and 100
jackpot = random.randint(1, 100)

print(f"\nI have selected a number between 1 and 100. You have {attempts} attempts to guess it!")

for i in range(1, attempts + 1):
    guess = int(input(f"Attempt {i}: Enter your guess: "))

    if guess == jackpot:
        print(f"🎉 Congratulations! You guessed the jackpot number {jackpot} in {i} attempts.")
        break
    elif guess < jackpot:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    if i == attempts:
        print(f"\n❌ Out of attempts! The jackpot number was {jackpot}. Better luck next time!")
