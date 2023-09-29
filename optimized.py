import csv 
import os
from dataclasses import dataclass, field
from pathlib import Path

project_path = str(Path(__file__).parent)


@dataclass
class Action:
    name: str
    cost: int
    value_percentage: int
    expected_value_two_years: int = field(init=False)

    def __post_init__(self):
        self.expected_value_two_years = int(
            self.cost + (self.cost * int((self.value_percentage) / 100))
        )

    def __str__(self):
        return f"Action-{self.name}"


max_budget = 500
data_file = os.path.join(project_path, "dataset1_Python+P7.csv")


with open(data_file, "r") as csvfile:
    reader = csv.reader(csvfile)
    # Skip the header
    next(reader)
    data = list(reader)
