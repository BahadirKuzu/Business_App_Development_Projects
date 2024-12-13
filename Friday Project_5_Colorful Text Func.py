import random

# Define functions to format text with specific colors
def redText(text):
    return f"\033[91m{text}\033[0m"  # Red color

def blueText(text):
    return f"\033[94m{text}\033[0m"  # Blue color

def greenText(text):
    return f"\033[92m{text}\033[0m"  # Green color

def yellowText(text):
    return f"\033[93m{text}\033[0m"  # Yellow color

def brownText(text):
    return f"\033[38;5;130m{text}\033[0m"  # Brown color

# Random color function
def randomColor(text):
    color_functions = [redText, blueText, greenText, yellowText, brownText]
    return random.choice(color_functions)(text)

# Function to display all available colors
def display_all_colors():
    color_samples = {
        "Red": redText("This is red text"),
        "Blue": blueText("This is blue text"),
        "Green": greenText("This is green text"),
        "Yellow": yellowText("This is yellow text"),
        "Brown": brownText("This is brown text")
    }
    
    print("Available colors:")
    for color_name, sample_text in color_samples.items():
        print(f"{color_name}: {sample_text}")

# Main program logic with additional features
def main():
    # Display all colors at the beginning
    display_all_colors()
    
    # Dictionary to map color choices to functions
    color_functions = {
        "red": redText,
        "blue": blueText,
        "green": greenText,
        "yellow": yellowText,
        "brown": brownText,
        "random": randomColor
    }

    # Loop to allow multiple text entries
    while True:
        # Prompt the user to choose a color and input text
        color_choice = input("Choose a color (red, blue, green, yellow, brown, random) or type 'exit' to quit: ").lower()
        
        if color_choice == "exit":
            print("Exiting the program. Goodbye!")
            break
        
        user_text = input("Enter the text to be displayed in the chosen color: ")
        
        if color_choice in color_functions:
            # Display the text in the selected or random color
            print(color_functions[color_choice](user_text))
        else:
            print("Invalid color choice. Please try again.")

        # Optional: Prompt for custom ANSI color code
        custom_option = input("Would you like to enter a custom ANSI color code? (yes/no): ").lower()
        if custom_option == "yes":
            ansi_code = input("Enter the ANSI color code number: ")
            if ansi_code.isdigit():  # Check if the input is a valid number
                print(f"\033[{ansi_code}m{user_text}\033[0m")
            else:
                print("Invalid ANSI code. Please enter only the number part of the ANSI code.")

if __name__ == "__main__":
    main()
