def invest(amount, rate, years):
    """
    Calculate and print the investment amount for each year.
    
    :param amount: Initial principal amount (float or int)
    :param rate: Annual rate of return as a decimal (float)
    :param years: Number of years to calculate (int)
    """
    for year in range(1, years + 1):
        amount = amount + amount * rate  # Issue here: Incorrect calculation
        print(f"year {year}: ${amount:.2f}")

def main():
    # Get user input
    initial_amount = float(input("Enter the initial amount: $"))
    annual_rate_percentage = float(input("Enter the annual rate of return (as a percentage): "))
    number_of_years = int(input("Enter the number of years: "))
    
    # Convert annual rate from percentage to decimal
    annual_rate_decimal = annual_rate_percentage / 100
    
    # Call the invest function
    invest(initial_amount, annual_rate_decimal, number_of_years)

# Execute the main function
if __name__ == "__main__":
    main()
