import unittest
from app.create_dataset_average import filter_student_with_scored_test, filter_test_status_scoring_scored
import os
import pandas as pd

path = os.path.dirname(os.path.dirname(__file__))


class TestCreateDatasetAverage(unittest.TestCase):

    def test_filter_student_with_scored_test(self):
        class_file = pd.read_csv(path + '/app/files/class_file_load_correct.csv')
        self.assertFalse(((filter_student_with_scored_test(class_file))['has_student_with_scored_test'] != 1).any())

    def test_filter_test_status_scoring_scored(self):
        test_file = pd.read_csv(path + '/app/files/test_file_load.csv')
        self.assertFalse(((filter_test_status_scoring_scored(test_file))['test_status'] != 'SCORING_SCORED').any())


if __name__ == '__main__':
    unittest.main()

