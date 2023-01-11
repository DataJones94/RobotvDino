
from weapons import Weapon

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.active_weapon = Weapon("Astro Blaster", 10)
        pass

    def attack(self, dinosaur):
        pass