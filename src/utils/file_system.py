# Standard imports
import os
import pandas as pd


def save_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def read_file_as_dataframe(file_path):
    return pd.read_csv(os.path.join(file_path))
