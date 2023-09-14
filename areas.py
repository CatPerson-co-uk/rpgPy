from dataclasses import dataclass
import csv

@dataclass
class area:
    placeName: str
    description: str
    # enemies: list
    # items: list

    def __post_init__(self):
        self.placeName = self.placeName.capitalize()
        self.description = self.description.capitalize()

    def __str__(self):
        return f"{self.placeName}: {self.description}"
    
    



areas = {}
with open("data/areaData.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        areas[row[0]] = area(*row[0:])
