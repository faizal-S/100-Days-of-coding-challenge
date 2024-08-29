# Function to convert Celsius to Fahrenheit
def convert_cel_to_far(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

# Get temperature in Celsius from the user
celsius_temp = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit_temp = convert_cel_to_far(celsius_temp)

# Print the result
print("The temperature in Fahrenheit is:", fahrenheit_temp)
