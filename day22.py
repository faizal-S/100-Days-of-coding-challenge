

def get_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def main():
    while True:
        try:
            # Get user input
            user_input = int(input("Please enter a positive integer: "))
            if user_input <= 0:
                print("The number must be positive. Please try again.")
                continue

            # Get factors of the number
            factors = get_factors(user_input)

            # Print factors
            print(f"The factors of {user_input} are: {', '.join(map(str, factors))}")
            break  # Exit loop if successful
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
