from pathlib import Path
import sys

project_path = str(Path(__file__).parent.parent)
sys.path.insert(0, project_path)

import time # noqa
import matplotlib.pyplot as plt # noqa
from brute_force import calculate_best_actions as calculate_best_actions_brute_force # noqa
from optimized import calculate_best_actions as calculate_best_actions_optimized # noqa
from utils.load_data_bruteforce import load_data_from_json_file # noqa
from utils.load_data_optimized import load_data_from_csv_files # noqa


def measure_execution_time_by_time(data: dict | list, max_budget: int) -> None:
    """
    Measures the total time it takes to execute the calculate_best_actions()
    function once using the time module.

    Args:
        data (dict|list): Dictionary or list containing action data.
        max_budget (int): The maximum budget available.
    """
    start_time = time.time()
    if type(data) is dict:
        calculate_best_actions_brute_force(data, max_budget)
    else:
        calculate_best_actions_optimized(data, max_budget)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time


data_sizes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# data_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
brute_force_times = []
optimized_times = []
data_one_opti, data_two_opti = load_data_from_csv_files()
data_bruteforce = load_data_from_json_file()

data_bruteforce_hundred = {}
for i in range(1, 101):
    data_bruteforce_hundred[f"Action-{i}"] = data_bruteforce[
        f"Action-{i%len(data_bruteforce) or 1}"
    ]


for size in data_sizes:
    data = {}
    print(f"{size=}", end="\r")
    for key, value in list(data_bruteforce_hundred.items())[:size]:
        data[key] = value

    max_budget = 500

    brute_force_time = measure_execution_time_by_time(data, max_budget)
    brute_force_times.append(brute_force_time)

for size in data_sizes:
    data = data_one_opti[:size]
    max_budget = 500

    optimized_time = measure_execution_time_by_time(data, max_budget)
    optimized_times.append(optimized_time)

plt.plot(data_sizes, brute_force_times, label="Brute Force")
plt.plot(data_sizes, optimized_times, label="Optimized")
plt.xlabel("Data Size")
plt.ylabel("Execution Time (s)")
plt.legend()
plt.show()
