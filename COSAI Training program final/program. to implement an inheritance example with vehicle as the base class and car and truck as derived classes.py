class Vehicle:
    def __init__(self, make, model, year):
        """Initialize the Vehicle with common attributes."""
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        """Display details about the vehicle."""
        return f"Vehicle Details:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}"

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        """Initialize the Car with additional attributes."""
        super().__init__(make, model, year)
        self.doors = doors

    def display_details(self):
        """Display details about the car."""
        return f"{super().display_details()}\nDoors: {self.doors}"

class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        """Initialize the Truck with additional attributes."""
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def display_details(self):
        """Display details about the truck."""
        return f"{super().display_details()}\nPayload Capacity: {self.payload_capacity} tons"


if __name__ == "__main__":
    
    my_car = Car("Honda", "Civic", 2020, 4)
    print(my_car.display_details())
    
    print()  

    my_truck = Truck("Ford", "F-150", 2018, 1.5)
    print(my_truck.display_details())
