# Creating tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 'hello', 3.14)

# Accessing elements
print("First element of tuple1:", tuple1[0])
print("Last element of tuple2:", tuple2[-1])

# Slicing tuples
print("Slice of tuple3 (1:3):", tuple3[1:3])
print("Slice of tuple1 (0:2):", tuple1[0:2])

# Length of tuples
print("Length of tuple1:", len(tuple1))
print("Length of tuple3:", len(tuple3))

# Concatenation
combined_tuple = tuple1 + tuple2
print("Combined tuple:", combined_tuple)

# Repeating tuples
repeated_tuple = tuple2 * 2
print("Repeated tuple:", repeated_tuple)

# Membership testing
print("Is 'a' in tuple2?", 'a' in tuple2)
print("Is 3 in tuple1?", 3 in tuple1)

# Counting elements
print("Count of 'a' in tuple2:", tuple2.count('a'))

# Finding index of an element
print("Index of 'hello' in tuple3:", tuple3.index('hello'))

# Iterating through a tuple
print("Elements in tuple1:")
for item in tuple1:
    print(item)

# Nested tuples
nested_tuple = (tuple1, tuple2)
print("Nested tuple:", nested_tuple)

# Tuple unpacking
x, y, z = tuple1
print("Unpacked values:", x, y, z)

# Converting a list to a tuple
my_list = [4, 5, 6]
list_to_tuple = tuple(my_list)
print("Converted list to tuple:", list_to_tuple)

# Sorting a tuple (by converting to list first)
sorted_tuple = tuple(sorted(tuple1))
print("Sorted tuple1:", sorted_tuple)

# Creating a tuple with a single element
single_element_tuple = (42,)
print("Single element tuple:", single_element_tuple)

# Example of tuple as a dictionary key
my_dict = {tuple1: "This is tuple1"}
print("Dictionary with tuple as key:", my_dict)
