import random

# Color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

secret_number = random.randint(1, 10)
attempts = 3

print(CYAN + "🎮 Welcome to the Guessing Game!" + RESET)
print(YELLOW + "You have 3 attempts.\n" + RESET)

while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == secret_number:
        print(GREEN + "🎉 Correct! You won!" + RESET)
        break
    elif guess < secret_number:
        print(RED + "Too low 😅" + RESET)
    else:
        print(RED + "Too high 😬" + RESET)

    attempts -= 1
    print(YELLOW + "Attempts left:" , attempts , RESET)

if attempts == 0:
    print(RED + "😢 You lost. The number was:" , secret_number , RESET)
print("hello")

