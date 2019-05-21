from load_files import load_files
from create_dataset_utilization import create_dataset_utilization
from create_dataset_average import create_dataset_average
from load_datasets_to_database import load_datasets_to_database
import os


def main():
    path = '/'.join(os.path.abspath(__file__).split('/')[:-2])
    load_files(path)
    create_dataset_utilization(path)
    create_dataset_average(path)
    load_datasets_to_database()


if __name__ == '__main__':
    main()
