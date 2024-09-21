import random

# A few strings and tuples
greetings = "Hello, Welcome to the Enchanted Forest!"
adjectives = ("mysterious", "ancient", "forgotten", "hidden")
creatures = ("dragon", "unicorn", "goblin", "fairy")
places = ("cave", "castle", "meadow", "lake")

# Function to create a mysterious message
def create_mysterious_message():
    # Randomly select elements from tuples
    adj = random.choice(adjectives)
    creature = random.choice(creatures)
    place = random.choice(places)

    # Format the message
    message = f"Once upon a time, in a {adj} land, a {creature} lived in a {place}."
    return message

# Create a list to store multiple messages
mystery_messages = []

# Generate 5 mysterious messages
for _ in range(5):
    mystery_messages.append(create_mysterious_message())

# Function to display messages
def display_messages(messages):
    print(greetings)
    print("\nHere are some mysterious tales:\n")
    for i, msg in enumerate(messages):
        print(f"{i + 1}. {msg}")

# Display the generated messages
display_messages(mystery_messages)

# Creating a tuple of all messages
message_tuple = tuple(mystery_messages)

# A final twist: print the tuple
print("\nMystery messages in tuple format:")
print(message_tuple)

# Unusual end
if len(message_tuple) % 2 == 0:
    print("An odd adventure awaits!")
else:
    print("The mystery deepens...")

