import random

from ability import Ability

class Weapon(Ability):
    def __init__(self, name, max_damage):
        super().__init__(name, max_damage)

    def attack(self):
        return random.randint(0, self.max_damage)