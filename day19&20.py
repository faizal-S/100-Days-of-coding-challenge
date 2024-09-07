
# Get user inputs
print("Please fill out the following form:")

# Input grade
grade = float(input("Enter your school grade in percentage: "))

# Input age
age = int(input("Enter your age: "))

# Input location
location = input("Enter your location: ").strip()

# Print collected information
print("\nYou have entered the following details:")
print(f"Grade: {grade}%")
print(f"Age: {age}")
print(f"Location: {location}")

# Determine eligibility
if grade < 50:
    print("Not Eligible: Your grade is below the required threshold.")
elif location.lower() != "nigeria":
    print("Not Eligible: Location is not Nigeria.")
else:
    print("Eligible: You meet the criteria.")
