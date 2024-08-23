print("AAA".find("a"))

# Challenge: Turn Your User Into a L33t H4xor
# Prompt the user for input
user_input = input("Enter some text: ")

# Convert the text into leetspeak using multiple replace() calls
leetspeak = (user_input
             .replace("a", "4")
             .replace("b", "8")
             .replace("e", "3")
             .replace("l", "1")
             .replace("o", "0")
             .replace("s", "5")
             .replace("t", "7"))

# Display the result
print(leetspeak)
