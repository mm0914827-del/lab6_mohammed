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

    def show_stats(self):
        """Prints current player stats."""
        print(f"--- {self.name} ---")
        print(f"Points: {self.points} | Energy: {self.energy}%\n")


# --- TEST YOUR CLASS HERE ---
if __name__ == "__main__":
    player1 = HoopPlayer("LeBron", 90)
    player1.show_stats()

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
# --- TEST YOUR CLASS HERE ---
if __name__ == "__main__":
    # Create two players to test the move
    pf = PowerForward("Giannis", 80, 95)
    pg = PointGuard("Luka", 85, 90)
    defender = HoopPlayer("Defender", 70)

    # Show initial stats
    pf.show_stats()

    # Test the special move!
    pf.post_move(defender)
    pf.show_stats()
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