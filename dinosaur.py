
class Dinosaur:
    def __init__(self, dino_name, dino_attack_power, dino_health):
        self.name = dino_name
        self.attack_power = dino_attack_power
        self.health = dino_health
        pass

    def dino_attack(self, robot_attacked):
        robot_attacked.health -= self.attack_power
        print(f'{robot_attacked.robot_name} is going into "Sleep-mode"! Health points: {robot_attacked.health}')

        pass