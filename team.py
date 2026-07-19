import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def get_living_heroes(self):
        return [hero for hero in self.heroes if hero.is_alive()]

    def attack(self, other_team):
        living_heroes = self.get_living_heroes()
        living_opponents = other_team.get_living_heroes()
        for hero in living_heroes:
            if living_opponents:
                hero.attack(random.choice(living_opponents))

    def stats(self):
        for hero in self.heroes:
            print(f"{hero.name} - Kills: {hero.kills}, Deaths: {hero.deaths}")
                