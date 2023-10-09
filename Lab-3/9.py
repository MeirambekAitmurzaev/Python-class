import random


target_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a random number between 1 and 100.")
print({target_number})

while True:
    user_guess = int(input("Guess the number: "))

    if user_guess < target_number:
        print("Too small! Try again.")
    elif user_guess > target_number:
        print("Too large! Try again.")
    else:
        print(f"Congratulations! You guessed the correct number, which is {target_number}.")
        break
