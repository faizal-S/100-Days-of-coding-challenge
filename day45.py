class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def bark(self):
        return f"{self.name} says Woof!"

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"

    def sit(self):
        return f"{self.name} sits down."

    def roll_over(self):
        return f"{self.name} rolls over."

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Coat Color: {self.coat_color}"

    def birthday(self):
        self.age += 1
        return f"Happy Birthday, {self.name}! You are now {self.age} years old."

def main():
    philo = Dog("Philo", 5, "brown")
    print(f"{philo.name}'s coat is {philo.coat_color}.")
    print(philo.bark())
    print(philo.fetch("ball"))
    print(philo.sit())
    print(philo.roll_over())
    print(philo.display_info())
    print(philo.birthday())
    print(philo.display_info())

if __name__ == "__main__":
    main()
