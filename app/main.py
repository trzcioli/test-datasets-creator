from load_files import load_files
from create_dataset_utilization import create_dataset_utilization
from create_dataset_average import create_dataset_average
from load_datasets_to_database import load_datasets_to_database
import os
import argparse


def main():
    path = '/'.join(os.path.abspath(__file__).split('/')[:-2])

    parser = argparse.ArgumentParser()
    parser.add_argument("-lf", "--load_files", help="load csv files from input_files",  action='store_true')
    parser.add_argument("-cuti", "--create_dataset_utilization", help="create dataset utilization",  action='store_true')
    parser.add_argument("-cavg", "--create_dataset_average", help="create dataset average",  action='store_true')
    parser.add_argument("-ld", "--load_datasets_to_database", help="load datasets to database",  action='store_true')
    args = parser.parse_args()

    if not any(vars(args).values()):
        load_files(path)
        create_dataset_utilization(path)
        create_dataset_average(path)
        load_datasets_to_database(path)
    elif args.load_files:
        load_files(path)
    elif args.create_dataset_utilization:
        create_dataset_utilization(path)
    elif args.create_dataset_average:
        create_dataset_average(path)
    elif args.load_datasets_to_database:
        load_datasets_to_database(path)


if __name__ == '__main__':
    main()
