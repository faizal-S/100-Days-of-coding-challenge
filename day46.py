class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

# Instantiate the Car objects
blue_car = Car("blue", 20000)
red_car = Car("red", 30000)

# Print the colors and mileage
print(f"The {blue_car.color} car has {blue_car.mileage:,} miles.")
print(f"The {red_car.color} car has {red_car.mileage:,} miles.")
