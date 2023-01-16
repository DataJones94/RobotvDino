from weapons import Weapon

class Dinosaur:
    def __init__(self, name, attack_power, health):
        self.name = name
        self.attack_power = attack_power
        self.health = health
        pass
    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"{self.name} attacks {robot.name} with {robot.active_weapon.name}. {robot.name} has {robot.health} health points left." )
        pass