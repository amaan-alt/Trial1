# Parent class
class Vehicle:
    def move(self):
        pass  # Placeholder, will be overridden

# Child classes
class Car(Vehicle):
    def move(self):
        print("Car is driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Plane is flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Boat is sailing ⛵")

# Create objects
car = Car()
plane = Plane()
boat = Boat()

# Demonstrate polymorphism
for v in [car, plane, boat]:
    v.move()
