# Step 1: Create a tuple literal named cardinal_numbers
cardinal_numbers = ("first", "second", "third")

# Step 2: Display the string at index 1 in cardinal_numbers
print(cardinal_numbers[1])

# Step 3: Unpack the values in cardinal_numbers into three new strings
position1, position2, position3 = cardinal_numbers
print(position1)
print(position2)
print(position3)

# Step 4: Create a tuple called my_name containing the letters of the name
my_name = tuple("Alex")  # Replace "Alex" with your actual name if needed

# Step 5: Check if the character "x" is in my_name
print('x' in my_name)

# Step 6: Create a new tuple containing all but the first letter in my_name
my_name_no_first = my_name[1:]
print(my_name_no_first)
