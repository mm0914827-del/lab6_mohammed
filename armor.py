import random

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)


def main():
    armor_1 = Armor("reallystrongg helmet", 50)
    print(armor_1.name)
    print(armor_1.max_block)
    print(armor_1.block())

if __name__ == "__main__":
    main()

