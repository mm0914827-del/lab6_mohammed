from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("Enter ability name: ")
        max_damage = int(input("Enter max damage: "))
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("Enter weapon name: ")
        max_damage = int(input("Enter max damage: "))
        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("Enter armor name: ")
        max_block = int(input("Enter max block: "))
        return Armor(name, max_block)

    def create_hero(self):
        name = input("Enter hero name: ")
        health = int(input("Enter hero health: "))
        hero = Hero(name, health)
        
        while True:
            choice = input("Add ability (a), weapon (w), armor (r), or done (d): ").lower()
            if choice == 'a':
                hero.add_ability(self.create_ability())
            elif choice == 'w':
                hero.add_weapon(self.create_weapon())
            elif choice == 'r':
                hero.add_armor(self.create_armor())
            elif choice == 'd':
                break
            else:
                print("Invalid choice. Please try again.")
        
        return hero

    def build_team_one(self):
        team_name = input("Enter Team One's name: ")
        self.team_one = Team(team_name)
        
        num_heroes = int(input(f"How many heroes for {team_name}? "))
        for _ in range(num_heroes):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        team_name = input("Enter Team Two's name: ")
        self.team_two = Team(team_name)
        
        num_heroes = int(input(f"How many heroes for {team_name}? "))
        for _ in range(num_heroes):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)
        self.team_two.attack(self.team_one)

    def show_stats(self):
        if not self.team_one and not self.team_two:
            print("No teams to show stats for.")
            return

        if self.team_one:
            print(f"\n{self.team_one.name} Stats:")
            self.team_one.stats()
        else:
            print("\nTeam One not created.")

        if self.team_two:
            print(f"\n{self.team_two.name} Stats:")
            self.team_two.stats()
        else:
            print("\nTeam Two not created.")

        # Determine winner if both teams exist
        if not self.team_one or not self.team_two:
            return

        team_one_living = len(self.team_one.get_living_heroes())
        team_two_living = len(self.team_two.get_living_heroes())

        if team_one_living > team_two_living:
            print(f"\n{self.team_one.name} wins!")
        elif team_two_living > team_one_living:
            print(f"\n{self.team_two.name} wins!")
        else:
            print("\nIt's a draw!")

if __name__ == "__main__":
            game_is_running = True
            arena = Arena()
            arena.build_team_one()
            arena.build_team_two()

            while game_is_running:
                arena.team_battle()
                arena.show_stats()
                play_again = input("Play Again? Y or N: ")

                if play_again.lower() == "n":
                    game_is_running = False
                    print("Thanks for playing!")
                else:
                    arena.team_one.revive_heroes()
                    arena.team_two.revive_heroes()