#day14
def get_gmail_and_password():
    while True:
        email = input("Please enter your Gmail address: ")
        if '@gmail.com' not in email:
            print("Error: The email must include '@gmail.com'.")
        else:
            break

    password = input("enter your password: ")
    return email, password

def main():
    email, password = get_gmail_and_password()
    print(f"Your Gmail: {email}")
    print(f"Your password: {password}")

if __name__ == "__main__":
    main()

#day15
def get_valid_age():
    while True:
        age_input = input("Please enter your age: ")
        if age_input.isdigit():  # Check if the input consists only of digits
            age = int(age_input)
            if age > 0:
                return age
            else:
                print("Error: Age must be a positive number.")
        else:
            print("Error: Please enter a valid number.")

def main():
    age = get_valid_age()
    print(f"Thank you! Your age is {age}.")

if __name__ == "__main__":
    main()
