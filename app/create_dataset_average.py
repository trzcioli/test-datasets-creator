import pandas as pd
import os
path = os.path.dirname(os.path.dirname(__file__))


def filter_student_with_scored_test(class_file):
    return class_file.loc[class_file['has_student_with_scored_test'] == 1]


def filter_test_status_scoring_scored(test_file):
    return test_file[(test_file.test_status == 'SCORING_SCORED')]


def group_by_class_and_mean_of_overall_score(test_data):
    return test_data.groupby('class_id') \
        .agg({'overall_score': 'mean'}) \
        .rename(columns={'overall_score': 'avg_class_test_overall_score'}) \
        .reset_index()


def create_dataset_average(path):
    test_file = pd.read_csv(path + '/app/files/test_file_load.csv')
    class_file = pd.read_csv(path + '/app/files/class_file_load_correct.csv')

    class_with_scored = filter_student_with_scored_test(class_file)
    class_data = class_with_scored[['id', 'name', 'teaching_hours']] \
        .rename(index=str, columns={'id': 'class_id', 'name': 'class_name'})

    test_data = filter_test_status_scoring_scored(test_file)
    test_data = test_data[['class_id', 'created_at', 'authorized_at', 'overall_score']]\
        .rename(index=str, columns={'created_at': 'test_created_at', 'authorized_at': 'test_authorized_at'})

    group_by_class = group_by_class_and_mean_of_overall_score(test_data)
    test_overall_score = pd.merge(class_data, group_by_class,
                                  on='class_id', how='outer')
    test_overall_score.to_csv(path + '/app/files/test_average_scores.csv', index=False)

    return test_overall_score


create_dataset_average(path)
