from dataclasses import dataclass
from random import choice
import sys

from enemies import enemies
from areas import areas

@dataclass
class player:

    name: str
    health: int = 100
    attack: int = 10
    defense: int = 0
    level: int = 1

    items: list = None

    def __post_init__(self):
        self.maxHealth = self.health
        self.name = self.name.capitalize()

    def __str__(self):
        return f"{self.name} has {self.health} HP left."
    

    def adventure(self):
        pass

    def fight(self, target):
        target.health -= self.attack - target.defense
        print(f"{self.name} attacked {target.name} for {self.attack - target.defense} damage!")
        print(target)

    def levelUp(self):
        healthGain = choice([10, 15, 20])
        attackGain = choice([1, 2, 3])
        defenseGain = choice([1, 2, 3])
        print(f"You leveled up! You gained {healthGain} health, {attackGain} attack, and {defenseGain} defense!")
        self.health += healthGain
        self.attack += attackGain
        self.defense += defenseGain
        self.level += 1


def fight(user, target): 
    user.fight(target)
    if target.health > 0:
        target.fight(user)

    if target.health <= 0:
        print(f"{target.name} has been defeated!")
    elif user.health <= 0:
        print(f"{user.name} has been defeated!")


def battle(user, target):
    print(f"You have encountered a {target.name}!")
    action = ""
    while user.health > 0 and target.health > 0:
        action = input("What do you want to do? (Attack, Defend, Run): ").lower()
        if action == "attack":
            fight(user, target)
        elif action == "defend":
            pass
        elif action == "run":
            pass
        else:
            print("Invalid action. Try again.")


def main():        
    user = player(input("Enter your name: "))
    print(f"\nWelcome, {user.name}!")
    print(f"Your stats are: {user.health} HP, {user.attack} attack, {user.defense} defense.")
    print("You are level 1.")
    print("Good luck!\n")

    action = input("What do you want to do? (Adventure, Quit): ").lower()
    while action != "quit":
        if action == "adventure":
            pass
        else:
            print("Invalid action. Try again.")
        action = input("What do you want to do? (Adventure, Quit): ").lower()
    print("Thanks for playing!")
    sys.exit()
    




main()