from dataclasses import dataclass
from random import choice
import csv, sys

from enemies import enemies
from areas import areas

@dataclass
class player:

    name: str
    health: int = 100
    maxHealth: int = 100
    attack: int = 10
    defense: int = 0
    level: int = 1

    items: list = None
    location: str = "home"

    def __post_init__(self):
        self.name = self.name.capitalize()
        if self.items is None:
            self.items = {}
        self.health = int(self.health)
        self.attack = int(self.attack)
        self.defense = int(self.defense)


    def __str__(self):
        return f"{self.name} has {self.health}/{self.maxHealth} HP left."
    

    def adventure(self):
        pass

    def fight(self, target):
        target.health -= self.attack - target.defense
        print(f"{self.name} attacked {target.name} for {self.attack - target.defense} damage!\n")
        print(target)

    def levelUp(self):
        healthGain = choice([10, 15, 20])
        attackGain = choice([1, 2, 3])
        defenseGain = choice([1, 2, 3])
        print(f"You leveled up! You gained {healthGain} health, {attackGain} attack, and {defenseGain} defense!\n")
        print(f"You are now level {self.level + 1}!\n")
        self.maxHealth += healthGain
        self.health += healthGain
        self.attack += attackGain
        self.defense += defenseGain
        self.level += 1

    def viewStats(self):
        print(f"\nYour stats are: {self.health}/{self.maxHealth} HP, {self.attack} attack, {self.defense} defense.")
        print(f"You are level {self.level}.")
        print(f"You are at: {self.location}.\n")

    def saveGame(self, file="data/playerData.csv"):
        with open(file,"r") as f:
            reader = csv.reader(f, delimiter=",")
            rows = list(reader)
        with open(file, "w") as f:
            writer = csv.writer(f, delimiter=",")
            for row in rows:
                if row[0] == self.name:
                    row = [self.name, self.health, self.maxHealth, self.attack, self.defense, self.level, self.location]
                    print("Saved game!")
                writer.writerow(row)



def readPlayerData(file):
    rows = []
    with open(file, "r") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            for i in range(0, len(row)):
                try:
                   row[i] = int(row[i])
                except ValueError:
                    pass
                print(row[i])
            rows.append(row)
    if len(rows) == 0:
        return None
    else:
        return rows



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
    playerSave = readPlayerData("data/playerData.csv")
    print("Welcome to the game!")

    loading = True
    while loading is True:
        ifLoadSave = input("Do you want to load a save? (Y/N): ").lower()
        if ifLoadSave == "y" and playerSave is None:
            print("You have not got a save!")
        elif ifLoadSave == "y":
            print("Here are your saves:")
            for row in playerSave:
                print(f"Save: \"{row[0]}\"")
            selectedSave = input("Which save do you want to load? ").capitalize()
            for row in playerSave:
                if row[0] == selectedSave:
                    user = player(*row[0:])
                    print(f"Welcome back, {user.name}!")
                    print(f"Your stats are: {user.health} HP, {user.attack} attack, {user.defense} defense.")
                    print(f"You are level {user.level}.")
                    print(f"You are at: {user.location}.\n")
                    loading = False


        elif ifLoadSave == "n":
            userName = input("What is your name? ")
            user = player(userName)
            print(f"Welcome, {user.name}!")
            print(f"Your stats are: {user.health} HP, {user.attack} attack, {user.defense} defense.")
            print("You are level 1.")
            print("Good luck!\n")
            loading = False
        else:
            print("Invalid input. Try again.")

    actions = {"view stats": user.viewStats, "save": user.saveGame, "quit": sys.exit, "adventure": user.adventure, "levelup": user.levelUp}
    while True:
        action = input("What do you want to do? (Adventure, View Stats, Save, Quit): ").lower()
        if action in actions:
            actions[action]()
            
        else:
            print("Invalid action. Try again.")




main()