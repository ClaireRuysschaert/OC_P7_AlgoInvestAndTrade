import pstats
from pathlib import Path
import os
import sys
import cProfile

project_path = str(Path(__file__).parent.parent)
sys.path.insert(0, project_path)

from brute_force import (  # noqa
    calculate_best_actions as calculate_best_actions_brute_force,
)
from optimized import calculate_best_actions as calculate_best_actions_optimized  # noqa
from utils.load_data_bruteforce import load_data_from_json_file  # noqa
from utils.load_data_optimized import load_data_from_csv_files  # noqa


max_budget = 500
data_bruteforce = load_data_from_json_file()
data_optimized_one, data_optimized_two = load_data_from_csv_files()

cProfile.run(
    "calculate_best_actions_brute_force(data_bruteforce, max_budget)",
    "stats/brute_force_stats",
)
cProfile.run(
    "calculate_best_actions_optimized(data_optimized_one, max_budget)",
    "stats/optimized_stats",
)

my_profile_stat_path = os.path.join(project_path, "stats", "optimized_stats")
stats = pstats.Stats(my_profile_stat_path)
stats.sort_stats("cumulative")
stats.print_stats()
