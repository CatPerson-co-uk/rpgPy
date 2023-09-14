from dataclasses import dataclass
from random import choice

from enemies import enemies

@dataclass
class player:

    name: str
    health: int = 100
    attack: int = 10
    defense: int = 0
    level: int = 1

    def __post_init__(self):
        self.maxHealth = self.health
        self.name = self.name.capitalize()

    def __str__(self):
        return f"{self.name} has {self.health} HP left."
    
    def fight(self, target):
        target.health -= self.attack - target.defense
        print(f"{self.name} attacked {target.name} for {self.attack - target.defense} damage!")
        print(target)


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



main()