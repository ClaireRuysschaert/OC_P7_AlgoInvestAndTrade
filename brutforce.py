from dataclasses import dataclass, field
from itertools import combinations
from typing import List, Tuple


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

max_budget = 500

actions_data = [
    (20, 5),
    (30, 10),
    (50, 15),
    (70, 20),
    (60, 17),
    (80, 25),
    (22, 7),
    (26, 11),
    (48, 13),
    (34, 27),
    (42, 17),
    (110, 9),
    (38, 23),
    (14, 1),
    (18, 3),
    (8, 8),
    (4, 12),
    (10, 14),
    (24, 21),
    (114, 18),
]


def calculate_best_actions(
    actions_data: List[Tuple[int, int]], max_budget: int
) -> List[Tuple[Action]]:
    """
    Calculate the best combinations of actions to maximize returns
    within a given budget.

    Args:
        actions_data (List[Tuple[int, int]]): List of tuples containing
        action cost and value percentage.
        max_budget (int): The maximum budget available.

    Returns:
        List[Tuple[int, List[Action]]]: A list of tuples, each containing the
        total value and the list of actions in the combination.

    """
    actions_objects = [
        Action(index, cost, value_percentage)
        for index, (cost, value_percentage) in enumerate(actions_data, start=1)
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


best_combinations = calculate_best_actions(actions_data, max_budget)

print("\nVoici les actions à acheter pour avoir le meilleur rendement: \n")
for i, combination in enumerate(best_combinations):
    print(f"Combination {i + 1}:")
    for action in combination:
        print(action)
    print(f"Coût initial : {sum([action.cost for action in combination])}")
    print(f"Bénéfices : "
          f"{sum([action.expected_value_two_years for action in combination])}")
    print("----")
