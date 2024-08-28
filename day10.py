# Function to add two numbers and return the negative result
def add_and_negate(a, b):
    result = a + b
    return -result
num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

negative_sum = add_and_negate(num1, num2)

print("The negative of the sum is:", negative_sum)
