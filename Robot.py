
from weapon import Weapon
class Robot:
    def __init__(self, robot_name, health):
        self.robot_name = robot_name
        self.health = health
        self.attack_weapon = Weapon('Laser', 20)
        pass

    def attack(self, dino_attacked):
        dino_attacked.health -= self.attack_weapon.attack_power
        print(f'{dino_attacked.name} is loosing strenghth! Health points: {dino_attacked.health}')


        #create logic for a dino to loose health value based on robot attack
        #Battlefield.battle_phase.dino.health - Battlefield.battle_phase.bot.active_weapon
        #print(Battlefield.battle_phase.dino.health)
        pass