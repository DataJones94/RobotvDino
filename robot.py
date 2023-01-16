
from weapons import Weapon


class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.active_weapon = Weapon("Astro Blaster", 10)
        pass

    def attack(self, dino):      
        dino.health -= self.active_weapon.attack_power
        print(f"{self.name} attacks {dino.name} with {self.active_weapon.name}. {dino.name} has {dino.health} health points left.")
        pass
    