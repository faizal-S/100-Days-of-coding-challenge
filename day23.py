#task 1

def main():
    while True:
        user_input = input("Enter something (or 'q'/'Q' to quit): ")
        if user_input.lower() == 'q':
            print("Exiting the program.")
            break  # Exit the loop if 'q' or 'Q' is entered
        else:
            print(f"You entered: {user_input}")

if __name__ == "__main__":
    main()

# task2

def main():
    for number in range(1, 51):
        if number % 3 == 0:
            continue  # Skip numbers that are multiples of 3
        print(number)

if __name__ == "__main__":
    main()
