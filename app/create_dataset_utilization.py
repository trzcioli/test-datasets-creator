import pandas as pd


def create_dataset_utilization(path):
    test_file = pd.read_csv(path + '/app/files/test_file_load.csv')
    class_file = pd.read_csv(path + '/app/files/class_file_load_correct.csv')

    class_data = class_file[['id', 'name', 'teaching_hours']]\
        .rename(index=str, columns={'id': 'class_id', 'name': 'class_name'})

    test_data = test_file[['id', 'class_id', 'test_level_id', 'created_at', 'authorized_at']]\
        .rename(index=str, columns={'id': 'test_id', 'test_level_id': 'test_level',
                                    'created_at': 'test_created_at', 'authorized_at': 'test_authorized_at'})

    test_and_class_merge = pd.merge(class_data, test_data[pd.notnull(test_data.test_authorized_at)],
                                    on='class_id', how='right')

    test_and_class_merge['class_test_number'] = test_and_class_merge.groupby(by=['class_id']).cumcount() + 1
    test_and_class_merge.to_csv(path + '/app/files/test_utilization.csv', index=False)

    return test_and_class_merge

