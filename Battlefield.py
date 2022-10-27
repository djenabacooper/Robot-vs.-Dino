from robot import Robot
from dinosaur import Dinosaur
class Battlefield:
    def __init__(self):
        self.bot = Robot("Robbie", 100)
        self.dino = Dinosaur("Rex", 20, 100)
        pass
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        pass
    
    def display_welcome(self):
        print("Welcome to the arena!")
        pass

    def battle_phase(self):
        while self.bot.health > 0 or self.dino.health > 0:
            self.bot.attack(self.dino)
            self.dino.dino_attack(self.bot)
        pass

    def display_winner(self):
        champion = ''
        if self.bot.health > 0:
            print(f'{self.bot.robot_name} is the winner!')
        else:
            print(f"The winner is: {self.dino.name}")

        pass

    
