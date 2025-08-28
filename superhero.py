# Parent class: Superhero
class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power  # attribute

    def show_power(self):
        print(f"{self.name} has the power of {self.power}.")

# Child class: FlyingHero inherits from Superhero
class FlyingHero(Superhero):
    def move(self):
        print(f"{self.name} is flying through the sky! ✈️")

# Child class: StrongHero inherits from Superhero
class StrongHero(Superhero):
    def move(self):
        print(f"{self.name} is running super fast! 🏃‍♂️💨")

# Create objects
hero1 = FlyingHero("SkyMan", "Flight")
hero2 = StrongHero("PowerGirl", "Super Strength")

# Show powers
hero1.show_power()  # inherited method
hero2.show_power()

# Demonstrate polymorphism
hero1.move()  # FlyingHero move
hero2.move()  # StrongHero move
