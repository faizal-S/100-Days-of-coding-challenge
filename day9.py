def multiply(x, y):
    product = x * y
    return product


num = multiply(2, 4)
print(num)

def welcome(name):
    print(f"welcome, {name}!")

# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Get user input for the first number
number1 = float(input("Enter the first number: "))

# Get user input for the second number
number2 = float(input("Enter the second number: "))

# Call the function with the user input
result = add_numbers(number1, number2)

# Print the result
print(f"The sum of {number1} and {number2} is: {result}")
