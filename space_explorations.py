# Amir Abu Hani
# This is the first creating module.  this module has the spaceship class with attributes and 2 functions.
# __str__ function provides spaceship string representation
# spaceship_details function return the spaceship details, to save it later in json file
class Spaceship:
    def __init__(self, name, fuel, health):
        self.name = name
        self.fuel = 200
        self.health = health

    def __str__(self):
        return self.name + " is using " + str(self.fuel) + " liters of fuel and " + self.health + " health"

    def spaceship_details(self):
        return {
            "name": self.name,
            "fuel": self.fuel,
            "health": self.health
        }
