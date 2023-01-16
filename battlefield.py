from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot("R2",50)
        self.dino = Dinosaur("Kesha",100,50)
        pass

    #Master Method
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        pass
    
    def display_welcome(self):
        print("Welcome to the showdown!")

    def battle_phase(self):
        # until health for 1 player has fallen to/below 0
        while self.dino.health > 0 and self.robot.health > 0:
            # each player attacks the other
            self.dino.attack(self.robot)
            self.robot.attack(self.dino)
 
    def display_winner(self):
       if self.robot.health <= 0:
        print(f"Game Concluded: The winner is {self.dino.name}!")
       else:
        print(f"Game Concluded: The winner is {self.robot.name}!")
       pass