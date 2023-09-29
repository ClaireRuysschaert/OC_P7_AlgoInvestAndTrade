from typing import List, Tuple
import csv 
import os
from dataclasses import dataclass, field
from pathlib import Path

project_path = str(Path(__file__).parent)
DATA_FILE_ONE = "dataset1_Python+P7.csv"
DATA_FILE_TWO = "dataset2_Python+P7.csv"

@dataclass
class Action:
    name: str
    price: float
    profit: float
    expected_value_two_years: float = field(init=False)

    def __post_init__(self):
        self.expected_value_two_years = float(
            self.price + (self.price * float((self.profit) / 100))
        )
        self.expected_value_two_years = round(self.expected_value_two_years, 2)

    def __str__(self):
        return f"Action-{self.name}"


max_budget = 500
data_file_one = os.path.join(project_path, DATA_FILE_ONE)
data_file_two = os.path.join(project_path, DATA_FILE_TWO)


with open(data_file_one, "r") as csvfile:
    reader = csv.reader(csvfile)
    # Skip the header
    next(reader)
    data_one = list(reader)

with open(data_file_two, "r") as csvfile:
    reader = csv.reader(csvfile)
    # Skip the header
    next(reader)
    data_two = list(reader)

def calculate_best_actions(data: List[Tuple[str, float, float]], max_budget: int) -> Tuple[str, float, float, float]:
    """
    Using an optimized approach (Knapsack), determine the optimal combination of actions
    to maximize returns within a specified budget. 

    Args:
        data (List[List[str, float]]): List of lists containing action data with name, action cost and profit
        max_budget (int): The maximum budget available.

    Returns:
        List[Tuple[int, List[Action]]]: A list of tuples, each containing the
        total value and the list of actions in the combination.

    """
    actions_objects = [
        Action(
            name,
            float(price), 
            float(profit),
        )
        for name, price, profit in data
    ]
    
    # Sort actions by profit
    actions_objects.sort(key=lambda x: x.profit, reverse=True)
    
    selected_actions = []
    remaining_budget = max_budget
    portfolio_value = 0
    
    # Select actions that fit within the budget and maximize the portfolio value
    for action in actions_objects:
        if action.price <= remaining_budget:
            # Calculate portfolio value with the current action
            potential_actions = selected_actions + [action]
            potential_budget = remaining_budget - action.price
            potential_portfolio_value = sum(
                [act.expected_value_two_years for act in potential_actions]
            )
            
            # Check if adding the current action increases portfolio value
            if potential_portfolio_value > portfolio_value:
                selected_actions.append(action)
                remaining_budget = potential_budget
                portfolio_value = potential_portfolio_value
                
                # Remove actions that are now less profitable than the current one
                updated_selected_actions = []
                for act in selected_actions:
                    if act.profit >= action.profit:
                        updated_selected_actions.append(act)
                selected_actions = updated_selected_actions
    
    invested_amount = round(max_budget - potential_budget, 2)
    portfolio_value = round(portfolio_value, 2)
    profit_two_years = round(portfolio_value - invested_amount, 2)
    
    return selected_actions, invested_amount, portfolio_value, profit_two_years
    

best_combination, invested_amount, portfolio_value_two_years, profit_two_years = calculate_best_actions(data_one, max_budget)
print("----")
print("Dataset 1")
print("----")
print(f"Voici les {len(best_combination)} noms des actions à acheter pour avoir le meilleur rendement: \n")
print(best_combination)
print(f"Coût initial : {invested_amount} euros")
print(f"Valeur du portefeuille après 2 ans : {portfolio_value_two_years} euros")
print(f"Bénéfices : {profit_two_years} euros")
print("----")

best_combination, invested_amount, portfolio_value_two_years, profit_two_years = calculate_best_actions(data_two, max_budget)
print("----")
print("Dataset 2")
print("----")
print(f"Voici les {len(best_combination)} noms des actions à acheter pour avoir le meilleur rendement: \n")
print(best_combination)
print(f"Coût initial : {invested_amount} euros")
print(f"Valeur du portefeuille après 2 ans : {portfolio_value_two_years} euros")
print(f"Bénéfices : {profit_two_years} euros")
print("----")
