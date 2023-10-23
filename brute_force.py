from dataclasses import dataclass, field
from itertools import combinations
from typing import List, Tuple
from utils.load_data_bruteforce import load_data_from_json_file


@dataclass
class Action:
    index: int
    cost: int
    value_percentage: int
    expected_value_two_years: int = field(init=False)

    def __post_init__(self):
        self.expected_value_two_years = int(
            self.cost + (self.cost * (self.value_percentage / 100))
        )

    def __str__(self):
        return f"Action-{self.index}"


MAX_BUDGET = 500

data = load_data_from_json_file()


def calculate_best_actions(data: dict, max_budget: int) -> List[Tuple[Action]]:
    """
    Using a brute force approach, determine the optimal combination of actions
    to maximize returns within a specified budget.

    Args:
        data (dict): Dictionary containing action data with keys as action names.
        action cost and value percentage.
        max_budget (int): The maximum budget available.

    Returns:
        List[Tuple[int, List[Action]]]: A list of tuples, each containing the
        total value and the list of actions in the combination.

    """
    actions_objects = [
        Action(
            name,
            cost_profit["Coût par action (en euros)"],
            cost_profit["Bénéfice (après 2 ans)"],
        )
        for name, cost_profit in data.items()
    ]

    best_combinations = []
    best_value = 0

    # Iterate over all possible combinations of actions
    for i in range(1, len(actions_objects) + 1):
        for combination in combinations(actions_objects, i):
            # Check if the sum of the costs of the actions in the combination
            # is less than or equal to the maximum budget
            total_cost = sum([action.cost for action in combination])
            if total_cost <= max_budget:
                total_value = sum(
                    [action.expected_value_two_years for action in combination]
                )
                # Check if the total value is greater than or equal to the best
                # value found so far
                if total_value > best_value:
                    best_combinations = [combination]
                    best_value = total_value
                elif total_value == best_value:
                    best_combinations.append(combination)

    return best_combinations


if __name__ == "__main__":
    best_combinations = calculate_best_actions(data, MAX_BUDGET)

    print("\nVoici les actions à acheter pour avoir le meilleur rendement: \n")
    for i, combination in enumerate(best_combinations, start=1):
        print(f"Combination {i}:")
        for action in combination:
            print(action)
        print(f"Coût initial : {sum([action.cost for action in combination])}")
        print(
            f"Bénéfices : "
            f"{sum([action.expected_value_two_years for action in combination])}"
        )
        print("----")
