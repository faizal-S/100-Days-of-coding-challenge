class Car:
    def __init__(self, color, mileage):
        """
        Initializes a new instance of the Car class.

        Parameters:
        color (str): The color of the car.
        mileage (int): The initial mileage of the car in miles.
        """
        self.color = color  # Sets the color of the car
        self.mileage = mileage  # Sets the initial mileage of the car

    def drive(self, miles):
        """
        Adds miles to the car's mileage.

        Parameters:
        miles (int): The number of miles to add to the current mileage.
        """
        if miles < 0:
            print("You cannot drive a negative distance!")
        else:
            self.mileage += miles  # Increases the mileage by the given miles
            print(f"You drove {miles} miles. New mileage: {self.mileage:,} miles.")

# Instantiate a car with 0 miles
my_car = Car("green", 0)

# Print the initial mileage
print(f"The {my_car.color} car has {my_car.mileage:,} miles.")

# Drive the car for 100 miles
my_car.drive(100)

# Print the updated mileage
print(f"The {my_car.color} car now has {my_car.mileage:,} miles.")
