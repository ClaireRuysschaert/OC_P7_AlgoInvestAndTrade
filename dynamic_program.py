from dataclasses import dataclass, field
from typing import List
from utils.load_data_optimized import load_data_from_csv_files


@dataclass
class Action:
    name: str
    price: int
    profit: int
    expected_value_two_years: float = field(init=False)

    def __post_init__(self):
        self.price = int(self.price * 100)
        self.profit = int(self.profit * 100)
        self.expected_value_two_years = float(
            self.price + (self.price * float((self.profit) / 100))
        )
        self.expected_value_two_years = round(self.expected_value_two_years, 2)

    def __str__(self):
        return f"{self.name} - Price: {self.price/100} - Profit: {self.profit/100}"

    def __repr__(self):
        return str(self)


@dataclass
class ActionSet:
    action_list: List[Action]

    @property
    def total_profits(self):
        return sum([action.profit for action in self.action_list])

    def __str__(self):
        return (
            f"Total profits: {self.total_profits/100}\n"
            + f"Total price: {sum([action.price for action in self.action_list])}\n"
            + "----Details----\n"
            + "\n".join([str(action) for action in self.action_list])
        )

    def __add__(self, other: "ActionSet"):
        if isinstance(other, Action):
            return ActionSet(self.action_list + [other])
        elif isinstance(other, ActionSet):
            return ActionSet(self.action_list + other.action_list)

    def __radd__(self, other: "ActionSet"):
        return self.__add__(other)


data_one, data_two = load_data_from_csv_files()

actions_list = [
    Action(
        name,
        float(price),
        float(profit),
    )
    for name, price, profit in data_one if float(price) > 0
]
BUDGET = 50000
dynamic_table = [
    [ActionSet([]) for _ in range(BUDGET + 1)] for _ in range(len(actions_list) + 1)
]


def knapsack(action_list: List[Action], budget):
    # For each possible size of the knapsack
    for action_index in range(1, len(action_list) + 1):
        # For each possible budget, find the ActionSet with the maximum profit
        # for the current knapsack size
        previous_action_index = action_index - 1
        previous_action = action_list[previous_action_index]
        for current_budget in range(1, budget + 1):
            # If the current action can fit in the knapsack
            if previous_action.price <= current_budget:
                # If the current action is more profitable than the previous action
                if (
                    previous_action.profit
                    + dynamic_table[previous_action_index][
                        current_budget - previous_action.price
                    ].total_profits
                    > dynamic_table[previous_action_index][current_budget].total_profits
                ):
                    # Add the current action to the ActionSet
                    dynamic_table[action_index][current_budget] = dynamic_table[
                        previous_action_index
                    ][current_budget - previous_action.price] + ActionSet(
                        [previous_action]
                    )
                else:
                    # Add the previous action to the ActionSet
                    dynamic_table[action_index][current_budget] = dynamic_table[
                        previous_action_index
                    ][current_budget]
            else:
                # Add the previous action to the ActionSet
                dynamic_table[action_index][current_budget] = dynamic_table[
                    previous_action_index
                ][current_budget]

    return dynamic_table[-1][-1]


print(knapsack(actions_list, BUDGET))
