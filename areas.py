from dataclasses import dataclass
import csv, os

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
    
    

script_dir = os.path.dirname(__file__)
rel_path = "data/areaData.csv"
abs_file_path = os.path.join(script_dir, rel_path)

areas = {}
with open(abs_file_path, "r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        areas[row[0]] = area(*row[0:])