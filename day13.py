import re

def is_password_valid(password):
    """
    Check if the password is valid.
    A valid password must:
    - Contain at least one special character from the list ['@', '#', '$', '%']
    - Be at least 8 characters long
    """
    # Regular expression patterns for validation
    special_characters = r'[@#$%]'
    min_length = 8
    
    if len(password) < min_length:
        print("Error: Password must be at least 8 characters long.")
        return False

    if not re.search(special_characters, password):
        print(f"Error: Password must contain at least one special character from {special_characters}.")
        return False

    return True

def get_username():
    """
    Prompt the user to enter a username.
    """
    return input("Enter your username: ")

def get_password():
    """
    Prompt the user to enter a password and validate it.
    """
    while True:
        password = input("Enter your password: ")
        if is_password_valid(password):
            print("Password accepted.")
            return password
        else:
            print("Please try again.")

def main():
    """
    Main function to run the user input and validation process.
    """
    print("Welcome to the secure login system!")
    username = get_username()
    print(f"Hello, {username}!")
    password = get_password()
    
    # Display a success message
    print("Login successful. Have a great day!")

if __name__ == "__main__":
    main()
