from pathlib import Path
import sys

project_path = str(Path(__file__).parent.parent)
sys.path.insert(0, project_path)

import timeit # noqa
from utils.load_data_bruteforce import load_data_from_json_file # noqa
from utils.load_data_optimized import load_data_from_csv_files # noqa
from brute_force import calculate_best_actions as calculate_best_actions_brute_force # noqa
from optimized import calculate_best_actions as calculate_best_actions_optimized # noqa

max_budget = 500

data_bruteforce = load_data_from_json_file()
data_optimized = load_data_from_csv_files()


def measure_execution_time_by_execution_number(
    data: dict | list, max_budget: int
) -> None:
    """
    Measures the average time it takes to execute the calculate_best_actions()
    function over multiple iterations using the timeit module.

    Args:
        data (dict | list): Dictionary or list containing action data.
        max_budget (int): The maximum budget available.
    """
    if type(data) is dict:
        ten_executions = timeit.timeit(
            "calculate_best_actions_brute_force({}, {})".format(data, max_budget),
            globals=globals(),
            number=10,
        )
        hundred_executions = timeit.timeit(
            "calculate_best_actions_brute_force({}, {})".format(data, max_budget),
            globals=globals(),
            number=100,
        )
        thousand_executions = timeit.timeit(
            "calculate_best_actions_brute_force({}, {})".format(data, max_budget),
            globals=globals(),
            number=1000,
        )
        print("\nTemps moyen de l'exécution de l'algorithme brute force: ")
    else:
        ten_executions = timeit.timeit(
            "calculate_best_actions_optimized({}, {})".format(data[0], max_budget),
            globals=globals(),
            number=10,
        )
        hundred_executions = timeit.timeit(
            "calculate_best_actions_optimized({}, {})".format(data[0], max_budget),
            globals=globals(),
            number=100,
        )
        thousand_executions = timeit.timeit(
            "calculate_best_actions_optimized({}, {})".format(data[0], max_budget),
            globals=globals(),
            number=1000,
        )
        print("\nTemps moyen de l'exécution de l'algorithme optimisé: ")
    print(f"Pour 10 exécutions {ten_executions}")
    print(f"Pour 100 exécutions {hundred_executions}")
    print(f"Pour 1000 exécutions {thousand_executions}")


measure_execution_time_by_execution_number(data_bruteforce, max_budget)
measure_execution_time_by_execution_number(data_optimized, max_budget)
