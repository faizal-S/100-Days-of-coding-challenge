# 1. Create an empty dictionary named captains.
captains = {}

# 2. Enter the data into the dictionary.
captains['Enterprise'] = 'Picard'
captains['Voyager'] = 'Janeway'
captains['Defiant'] = 'Sisko'

# 3. Check if "Enterprise" and "Discovery" exist as keys in the dictionary.
if "Enterprise" not in captains:
    captains["Enterprise"] = "unknown"

if "Discovery" not in captains:
    captains["Discovery"] = "unknown"

# 4. Display the ship and captain names contained in the dictionary.
for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}.")

# 5. Delete "Discovery" from the dictionary.
if "Discovery" in captains:
    del captains["Discovery"]

# 6. Bonus: Create the same dictionary using dict() with initial values.
captains_bonus = dict([
    ('Enterprise', 'Picard'),
    ('Voyager', 'Janeway'),
    ('Defiant', 'Sisko')
])

# Display the bonus dictionary
for ship, captain in captains_bonus.items():
    print(f"The {ship} is captained by {captain}.")
