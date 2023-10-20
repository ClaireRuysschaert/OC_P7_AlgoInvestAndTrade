from pathlib import Path
import os
import csv

project_path = str(Path(__file__).parent.parent)
DATA_FOLDER = "data"
DATA_FILE_ONE = "dataset1_Python+P7.csv"
DATA_FILE_TWO = "dataset2_Python+P7.csv"


def load_data_from_csv_files() -> list[list]:
    """
    Reads data from two CSV files and returns them as lists of lists.

    Returns:
        Two lists of lists representing the data from the CSV files.
    """
    data_file_one = os.path.join(project_path, DATA_FOLDER, DATA_FILE_ONE)
    data_file_two = os.path.join(project_path, DATA_FOLDER, DATA_FILE_TWO)

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

    return data_one, data_two
