def main():
    # Get user input
    number = float(input("Enter a number: "))
    
    # Check conditions using not and or
    if number < 20 or number == 20:
        doubled_number = number * 2
        print(f"The doubled number is: {doubled_number}")
    elif number > 20 and number != 25:
        print("The number is greater than 20 but not 25; it will not be doubled.")
    else:
        print("The number is 25; specific handling not defined.")

# Execute the main function
if __name__ == "__main__":
    main()
