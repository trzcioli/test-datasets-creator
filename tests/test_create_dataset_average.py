import unittest
from app.create_dataset_average import filter_student_with_scored_test, filter_test_status_scoring_scored, \
    group_by_class_and_mean_of_overall_score
import os
import pandas as pd
import numpy as np

path = os.path.dirname(os.path.dirname(__file__))


class TestCreateDatasetAverage(unittest.TestCase):

    def test_filter_student_with_scored_test(self):
        class_file = pd.read_csv(path + '/app/files/class_file_load_correct.csv')
        self.assertFalse(((filter_student_with_scored_test(class_file))['has_student_with_scored_test'] != 1).any())

    def test_filter_test_status_scoring_scored(self):
        test_file = pd.read_csv(path + '/app/files/test_file_load.csv')
        self.assertFalse(((filter_test_status_scoring_scored(test_file))['test_status'] != 'SCORING_SCORED').any())

    def test_count_avg_class_test_overall_score(self):
        test_file = pd.read_csv(path + '/app/files/test_file_load.csv')
        only_one_class = test_file.loc[test_file['class_id'] == 5]
        only_with_overall_score = only_one_class.dropna(subset=['overall_score'])
        avg_expected = np.asarray(only_with_overall_score.overall_score.values, dtype=float).mean()
        calc_mean = group_by_class_and_mean_of_overall_score(only_with_overall_score)
        avg_actual = calc_mean.avg_class_test_overall_score
        self.assertEqual(avg_expected, float(avg_actual))


if __name__ == '__main__':
    unittest.main()

