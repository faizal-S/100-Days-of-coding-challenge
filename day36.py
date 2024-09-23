# 1. Create a list named food with two elements
food = ["rice", "beans"]

# 2. Append the string "broccoli" to food
food.append("broccoli")

# 3. Add the string "bread" and "pizza" to food using .extend()
food.extend(["bread", "pizza"])

# 4. Print the first two items in the food list using slicing
print("First two items in food:", food[:2])

# 5. Print the last item in food using index notation
print("Last item in food:", food[-1])

# 6. Create a list called breakfast from the string "eggs, fruit, orange juice"
breakfast = "eggs, fruit, orange juice".split(", ")

# 7. Verify that breakfast has three items using len()
print("Number of items in breakfast:", len(breakfast))

# 8. Create a new list called lengths using a list comprehension
lengths = [len(item) for item in breakfast]

# Print the lengths of each string in the breakfast list
print("Lengths of each item in breakfast:", lengths)
