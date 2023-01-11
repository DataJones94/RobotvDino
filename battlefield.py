from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.robot = Robot("R2",50)
        self.dino = Dinosaur("Kesha",50,100)
        pass
    def run_game(self):
        pass
    
    def display_welcome(self):
        print("Welcome to the showdown!")
    def battle_phase(self):
        pass
    def display_winner(self):
        pass