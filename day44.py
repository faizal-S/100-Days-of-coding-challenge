class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
        print(f'Drove {miles} miles. Total mileage is now {self.mileage}.')

    def display_info(self):
        return f'{self.year} {self.make} {self.model}, Mileage: {self.mileage} miles'

class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f'Added: {car.display_info()}')

    def show_garage(self):
        for car in self.cars:
            print(car.display_info())

my_garage = Garage()
car1 = Car('Toyota', 'Camry', 2020)
car2 = Car('Honda', 'Civic', 2019)

my_garage.add_car(car1)
my_garage.add_car(car2)

car1.drive(150)
car2.drive(200)

my_garage.show_garage()
