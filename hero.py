import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, health=100): 
        self.name = name
        self.health = health
        self.abilities = []
        self.armors = []

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total_damage = sum(ability.attack() for ability in self.abilities)
        return total_damage

    def defend(self):
        total_block = sum(armor.block() for armor in self.armors)
        return total_block

    def take_damage(self, damage):
        net_damage = max(0, damage - self.defend())
        self.health -= net_damage
        return self.health

    def is_alive(self):
        return self.health > 0