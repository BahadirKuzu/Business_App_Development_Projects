# Import random module for number generation
import random

# Ask user if they want to play
print("Welcome! Do you want to play the number guessing game? (yes/no)")
response = input().lower()  # Convert input to lowercase

# Exit if user says no
if response == "no":
    print("Maybe next time!")  
else:
    # Generate random number between 1 and 10
    secret_number = random.randint(1, 10)
    guess = None  # Initialize guess variable

    # Keep asking until the correct guess
    while guess != secret_number:
        try:
            # Prompt user for a guess
            guess = int(input("Guess a number between 1 and 10: "))
        except ValueError:
            # Handle invalid input
            print("Please enter a valid number.")
            continue  # Skip rest of loop and ask again

        # Give hints if guess is too low or high
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed it!")

    # Farewell message
    print("Thanks for playing! Goodbye!")
