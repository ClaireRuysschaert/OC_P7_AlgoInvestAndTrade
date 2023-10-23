from typing import List, Tuple
from utils.load_data_optimized import load_data_from_csv_files
from dataclasses import dataclass, field


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


MAX_BUDGET = 500
data_one, data_two = load_data_from_csv_files()


def calculate_best_actions(
    data: List[List[str | float]], max_budget: int
) -> Tuple[str, float, float, float]:
    """
    Using an optimized approach (Knapsack), determine the optimal combination of actions
    to maximize returns within a specified budget.

    Args:
        data (List[List[str | float]]): List of lists containing action data with name,
        action cost and profit
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
        for name, price, profit in data if float(price) > 0
    ]

    # Sort actions by profit
    actions_objects.sort(key=lambda x: x.profit, reverse=True)

    selected_actions: List[Action] = []
    remaining_budget = max_budget
    portfolio_value = 0

    # Select actions that fit within the budget and maximize the portfolio value
    for action in actions_objects:
        if action.price <= remaining_budget:
            # Calculate portfolio value with the current action
            potential_actions: List[Action] = selected_actions + [action]
            potential_budget = remaining_budget - action.price
            potential_portfolio_value = sum(
                [act.expected_value_two_years for act in potential_actions]
            )

            # Check if adding the current action increases portfolio value
            if potential_portfolio_value > portfolio_value:
                selected_actions.append(action)
                remaining_budget = potential_budget
                portfolio_value = potential_portfolio_value

    invested_amount = round(max_budget - potential_budget, 2)
    portfolio_value = round(portfolio_value, 2)
    profit_two_years = round(portfolio_value - invested_amount, 2)

    return selected_actions, invested_amount, portfolio_value, profit_two_years


if __name__ == "__main__":
    (
        best_combination,
        invested_amount,
        portfolio_value_two_years,
        profit_two_years,
    ) = calculate_best_actions(data_one, MAX_BUDGET)
    print("----")
    print("Dataset 1")
    print("----")
    print(f"Voici les {len(best_combination)} noms des actions à")
    print("acheter pour avoir le meilleur rendement: \n")
    for action in best_combination:
        print(action)
    print(f"Coût initial : {invested_amount} euros")
    print(f"Valeur du portefeuille après 2 ans : {portfolio_value_two_years} euros")
    print(f"Bénéfices : {profit_two_years} euros")
    print("----")

    (
        best_combination,
        invested_amount,
        portfolio_value_two_years,
        profit_two_years,
    ) = calculate_best_actions(data_two, MAX_BUDGET)
    print("----")
    print("Dataset 2")
    print("----")
    print(f"Voici les {len(best_combination)} noms des actions à acheter")
    print("pour avoir le meilleur rendement: \n")
    for action in best_combination:
        print(action)
    print(f"Coût initial : {invested_amount} euros")
    print("Valeur du portefeuille après 2 ans : ")
    print(f"{portfolio_value_two_years} euros")
    print(f"Bénéfices : {profit_two_years} euros")
    print("----")
