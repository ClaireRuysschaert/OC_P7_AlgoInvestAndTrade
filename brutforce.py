from typing import List, Tuple

actions = [
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
max_budget = 500


def brute_force(actions: List[Tuple[int, int]], max_budget: int) -> Tuple[int, int, List[int]]:
    """
    Maximise the value of the client's portfolio after two years with the given actions and maximum budget.
    
    This algorithm uses a brute-force approach to try all possible combinations of actions, ensuring that:
    - Each action can be bought only once.
    - The client doesn't exceed the maximum budget.
    - The client can't buy a fraction of an action.
    - The client can't sell an action.

    Args:
        actions (List[Tuple[int, int]]): Each tuple contains (cost per action in euros, value per action after two years in percentage).
        max_budget (int): Client's maximum budget in euros.
    
    Returns:
        Tuple[int, int, List[int]]: A tuple containing the following information:
            - Invested amount in euros.
            - Value of the portfolio after two years in euros.
            - List of indices of the best actions to buy.
     
    """
    calculated_actions = []
    
    # Calculate the expected value after two years for each action
    for action_number, action in enumerate(actions, start=1):
        calculated_actions.append(
            (action_number, action[0], (action[0] + (action[0] * (action[1] / 100))))
        )
    # Sort actions by expected value in descending order
    calculated_actions.sort(key=lambda x: x[2], reverse=True)

    best_combination = []
    invested_amount = 0
    value_of_portfolio_two_years = 0

    # Select actions that fit within the budget and maximize the portfolio value
    for action_number, action_cost, action_two_years in calculated_actions:
        if action_cost <= max_budget:
            best_combination.append(action_number)
            invested_amount += action_cost
            max_budget -= action_cost
            value_of_portfolio_two_years += action_two_years

    return  int(invested_amount), int(value_of_portfolio_two_years), best_combination


invested_amount, value_of_portfolio_two_years, best_combination = brute_force(actions, max_budget)

print(f"Invested amount : {int(invested_amount)} euros")
print(f"Value of the portfolio after two years : {int(value_of_portfolio_two_years)} euros")
print(f"Best actions to buy : {best_combination}")
