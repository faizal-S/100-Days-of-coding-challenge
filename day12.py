num = float(input("Enter a positive number: "))
while num <= 0:
   print("That's not a positive number!")
   num = float(input("Enter a positive number: "))





user_name = input("Enter your name: ")

#if no capital letter is found initially
has_capital = False

# Check each character in the name
for char in user_name:
    if char.isupper():
        has_capital = True
        break

if not has_capital:
    print(False)
else:
    print(True)
