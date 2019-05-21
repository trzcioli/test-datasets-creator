from app.load_files import load_files
from app.create_dataset_utilization import create_dataset_utilization
from app.create_dataset_average import create_dataset_average
from app.load_datasets_to_database import load_datasets_to_database
import os

path = os.path.dirname(os.path.dirname(__file__))


def main():
    load_files()
    create_dataset_utilization(path)
    create_dataset_average(path)
    load_datasets_to_database()

