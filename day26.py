def get_integer():
    while True:
        try:
            # Prompt the user for input
            user_input = input("Please enter an integer: ")
            # Attempt to convert the input to an integer
            number = int(user_input)
            # If successful, display the number and break the loop
            print(f"You entered the integer: {number}")
            break
        except ValueError:
            # If a ValueError occurs, display a message and try again
            print("That's not a valid integer. Please try again.")

# Run the function
get_integer()

