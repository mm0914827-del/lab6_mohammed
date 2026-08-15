import random

class HoopPlayer:
    def __init__(self, name, shooting_power):
        self.name = name
        self.points = 0
        self.energy = 100  # Start at full stamina
        self.shooting_power = shooting_power

    def keep_energy_in_range(self):
        """Encapsulation method: keeps energy between 0 and 100."""
        if self.energy < 0:
            self.energy = 0
        elif self.energy > 100:
            self.energy = 100

    def shoot_ball(self, defender):
        """Basic jump shot: uses energy and can score 2 or 3 points."""
        energy_cost = 10
        if self.energy < energy_cost:
            print(f"❌ {self.name} is too tired to shoot!\n")
            return

        self.energy -= energy_cost
        accuracy = random.randint(1, 100)

        if accuracy <= self.shooting_power:
            points_scored = 3 if accuracy >= 85 else 2
            self.points += points_scored
            print(f"🏀 {self.name} hits a jump shot for {points_scored} points!")
        else:
            print(f"🚫 {self.name} misses the shot.")

        self.keep_energy_in_range()
        print(f"Remaining energy: {self.energy}%\n")

    def show_stats(self):
        """Prints current player stats."""
        print(f"--- {self.name} ---")
        print(f"Points: {self.points} | Energy: {self.energy}%\n")


# (Removed inline test; tests consolidated at bottom)

class PowerForward(HoopPlayer):
    def __init__(self, name, shooting_power, post_power):
        # Call the parent class (HoopPlayer) constructor
        super().__init__(name, shooting_power)
        self.post_power = post_power  # Extra detail for Kind 1!

    def post_move(self, opponent):
        """Special Move: Uses heavy energy to guarantee big points inside."""
        if self.energy >= 30:
            self.energy -= 30
            points_scored = 4
            self.points += points_scored
            self.keep_energy_in_range()
            print(f"💪 {self.name} uses BULLY BALL on {opponent.name}!")
            print(f"Scored {points_scored} points! Remaining energy: {self.energy}%\n")
        else:
            print(f"❌ {self.name} is too tired to execute a post move!\n")
class PointGuard(HoopPlayer):
    def __init__(self, name, shooting_power, speed):
        # Inherit parent attributes
        super().__init__(name, shooting_power)
        self.speed = speed  # Extra detail for Kind 2!

    def crossover_drive(self, opponent):
        """Special Move: Uses low energy for a fast 2-point layup."""
        energy_cost = 15
        if self.energy >= energy_cost:
            self.energy -= energy_cost
            points_scored = 2
            self.points += points_scored
            self.keep_energy_in_range()
            print(f"⚡ {self.name} blows past {opponent.name} with a CROSSOVER & DRIVE!")
            print(f"Scored {points_scored} points! Remaining energy: {self.energy}%\n")
        else:
            print(f"❌ {self.name} is too winded to pull off a crossover!\n")
class BasketballCourt:
    def __init__(self):
        # Lineup of 4 players (2 Power Forwards, 2 Point Guards)
        self.lineup = [
            PowerForward("Giannis", 80, 95),
            PowerForward("LeBron", 88, 90),
            PointGuard("Curry", 95, 99),
            PointGuard("Kyrie", 92, 98)
        ]
        self.user_player = None
        self.cpu_player = None

    def display_lineup(self):
        """Prints all players available to pick."""
        print("\n====== 🏀 1-ON-1 HOOPS ROSTER 🏀 ======")
        for index, player in enumerate(self.lineup, start=1):
            player_type = type(player).__name__
            print(f"{index}. {player.name} ({player_type}) - Shooting: {player.shooting_power}")
        print("=======================================\n")

    def select_players(self):
        """Lets the user pick a player and picks a random CPU opponent."""
        self.display_lineup()

        try:
            choice = int(input("Pick your player number (1-4): ")) - 1
            if choice < 0 or choice >= len(self.lineup):
                raise ValueError
        except ValueError:
            print("Invalid selection. Defaulting to player 1.")
            choice = 0

        self.user_player = self.lineup[choice]

        # CPU selection logic (picks anyone left on roster)
        available_opponents = [p for p in self.lineup if p is not self.user_player]
        self.cpu_player = random.choice(available_opponents)

        print(f"🔥 MATCHUP SET: {self.user_player.name} VS {self.cpu_player.name}! 🔥\n")

    def play_turn(self, attacker, defender):
        """Executes a single turn for either the user or CPU."""
        print(f"--- 🏀 {attacker.name}'s Turn ---")

        # If it's the User's turn, show the action menu
        if attacker == self.user_player:
            print("1. Jump Shot (Basic Attack)")
            print("2. Special Move")
            print("3. Rest (Recover +20 Energy)")
            choice = input("Choose an action (1-3): ")

            if choice == "1":
                attacker.shoot_ball(defender)
            elif choice == "2":
                if isinstance(attacker, PowerForward):
                    attacker.post_move(defender)
                elif isinstance(attacker, PointGuard):
                    attacker.crossover_drive(defender)
            elif choice == "3":
                attacker.energy = min(100, attacker.energy + 20)
                print(f"🔋 {attacker.name} rested and restored energy to {attacker.energy}%!\n")
            else:
                print("Invalid choice! Turn skipped.\n")

        # If it's the CPU's turn, pick randomly based on energy
        else:
            if attacker.energy >= 30:
                action = random.choice(["shoot", "special"])
            else:
                action = random.choice(["shoot", "rest"])

            if action == "shoot":
                attacker.shoot_ball(defender)
            elif action == "special":
                if isinstance(attacker, PowerForward):
                    attacker.post_move(defender)
                elif isinstance(attacker, PointGuard):
                    attacker.crossover_drive(defender)
            else:
                attacker.energy = min(100, attacker.energy + 20)
                print(f"🔋 {attacker.name} rested and restored energy to {attacker.energy}%!\n")


# --- TEST YOUR CLASSES HERE ---
if __name__ == "__main__":
    pf = PowerForward("Giannis", 80, 95)
    pg = PointGuard("Curry", 95, 99)

    print("--- PRE-GAME STATS ---")
    pf.show_stats()
    pg.show_stats()

    print("--- SPECIAL MOVES TEST ---")
    pf.post_move(pg)
    pg.crossover_drive(pf)

    print("--- POST-MOVE STATS ---")
    pf.show_stats()
    pg.show_stats()

    court = BasketballCourt()
    court.select_players()