import unittest
from app.create_dataset_average import filter_student_with_scored_test
import os
import pandas as pd

path = os.path.dirname(os.path.dirname(__file__))


class TestCreateDatasetAverage(unittest.TestCase):

    def test_filter_student_with_scored_test(self):
        class_file = pd.read_csv(path + '/app/files/class_file_load_correct.csv')
        self.assertFalse(((filter_student_with_scored_test(class_file))['has_student_with_scored_test'] != 1).any())


if __name__ == '__main__':
    unittest.main()

