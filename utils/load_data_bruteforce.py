import os
from pathlib import Path
import json

project_path = str(Path(__file__).parent.parent)
DATA_FOLDER = "data"
DATA_BRUTEFORCE_FILE = "action_data_bruteforce.json"

def load_data_from_json_file() -> dict:
    """
    Reads data from a JSON file and returns it as a dict for bruteforce algorithm.

    Returns:
        A dict representing the data from the JSON file.
    """

    data_file = os.path.join(project_path, DATA_FOLDER, DATA_BRUTEFORCE_FILE)

    with open(data_file, "r") as json_file:
        data = json.load(json_file)

    return data
