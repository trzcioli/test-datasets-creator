import pandas as pd
import os

path = os.path.dirname(os.path.dirname(__file__))


def load_file(file_name, path):
    file = pd.read_csv(path + '/input_files/' + file_name + '.csv', delimiter=';')
    file.to_csv(path + '/app/files/' + file_name + '_file_load.csv', index=False)
    return file


def correct_class_file(path):
    class_file = pd.read_csv(path + '/app/files/class_file_load.csv', delimiter=',')
    class_file_modify = class_file[~class_file['name'].str.contains(r'[\x5B-\x5E]+')]
    class_file_modify = class_file_modify[~class_file_modify['name'].str.contains(r'[^\x00-\x7F]+')]
    class_file_modify.to_csv(path + '/app/files/class_file_load_correct.csv', index=False)
    return class_file_modify


def load_files():
    load_file('test', path)
    load_file('test_level', path)
    load_file('class', path)
    correct_class_file(path)


load_files()
