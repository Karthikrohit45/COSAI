from datetime import datetime

class Car:
    def __init__(self, make, model, year):
        """Initialize the Car object with make, model, and year."""
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        """Display details about the car."""
        return f"Car Details:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}"

    def calculate_age(self):
        """Calculate the car's age."""
        current_year = datetime.now().year
        return current_year - self.year

if __name__ == "__main__":
    my_car = Car("Toyota", "Camry", 2015)

    print(my_car.display_details())

    print(f"Car Age: {my_car.calculate_age()} years")
