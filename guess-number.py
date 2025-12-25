import random

secret_number = random.randint(1, 10)
attempts = 3

print("🎮 Welcome to the Guessing Game!")
print("You have 3 attempts.")

while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret_number:
        print("🎉 Correct! You won!")
        break
    elif guess < secret_number:
        print("Too low 😅")
    else:
        print("Too high 😬")

    attempts -= 1
    print("Attempts left:", attempts)

if attempts == 0:
    print("😢 You lost. The number was:", secret_number)
