# Simple script to determine if a user can drive a car

# Get user input
age = int(input("Please enter your age: "))
has_license = input("Do you have a driver's license? (yes/no): ").strip().lower()

# Determine if the user can drive
if age >= 18:
    if has_license == 'yes':
        print("You are eligible to drive.")
    else:
        print("You need a driver's license to drive.")
elif age >= 16 and has_license == 'yes':
    print("You are a provisional driver. Check local laws for driving eligibility.")
else:
    print("Sorry, you are not eligible to drive.")

# Check for specific conditions with logical operators
if age < 16 or not (has_license == 'yes'):
    print("You are not eligible to drive based on age or license status.")

# Alternative message for age over 65 and still having a license
if age > 65 and has_license == 'yes':
    print("You are eligible to drive but remember to stay safe and check for any additional requirements.")

print("Thank you for using the driving eligibility checker.")
