def get_char_at_index():
    # Prompt the user for a string
    user_string = input("Please enter a string: ")

    while True:
        try:
            # Prompt the user for an integer index
            index_input = input("Please enter an integer index: ")
            # Attempt to convert the input to an integer
            index = int(index_input)
            # Attempt to access the character at the given index
            character = user_string[index]
            # If successful, display the character and break the loop
            print(f"The character at index {index} is: {character}")
            break
        except ValueError:
            # Handle the case where the index input is not an integer
            print("That's not a valid integer. Please try again.")
        except IndexError:
            # Handle the case where the index is out of bounds
            print("Index is out of bounds. Please enter a valid index.")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}")

# Run the function
get_char_at_index()
