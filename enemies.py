from dataclasses import dataclass
import csv, os


@dataclass
class enemy:
    name: str
    health: int
    attack: int
    defense: int
    level: int = 1


    def __post_init__(self):
        self.maxHealth = self.health
        self.name = self.name.capitalize()

        self.health = int(round(self.health))
        self.attack = int(round(self.attack))
        self.defense = int(round(self.defense))


    def __str__(self):
        return f"{self.name} has {self.health} HP left."
    
    def fight(self, target):
        target.health -= self.attack - target.defense
        print(f"{self.name} attacked {target.name} for {self.attack - target.defense} damage!")
        print(target)
    


script_dir = os.path.dirname(__file__)
rel_path = "data/enemyData.csv"
abs_file_path = os.path.join(script_dir, rel_path)

enemies = {}
with open(abs_file_path, "r") as f:
    reader = csv.reader(f, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        enemies[row[0]] = enemy(*row[0:])
