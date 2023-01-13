from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot("R2",50)
        self.dino = Dinosaur("Kesha",50,100)
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
        while self.robot.health < 50:
         if self.dino.attack(self.robot): 
            print("R2 attacks Kesha!")

         elif self.dino.health < 100:
            self.robot.attack(self.dino) 
            print("Kesha attacks R2!")
            break
        
    #  while (self.robot.health > 0 or self.dino.health > 0):
 
    def display_winner(self):
       if self.robot.health <= 0:
        print("Game Concluded: The winner is Ke$ha!")
       else:
        print("Game Concluded: The winner is R2!")

         
        pass