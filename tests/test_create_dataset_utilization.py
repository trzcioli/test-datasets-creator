import unittest
from app.create_dataset_utilization import create_dataset_utilization
import os
import pandas as pd


path = os.path.dirname(os.path.dirname(__file__))


class TestCreateDatasetUtilization(unittest.TestCase):

    def test_isnull_test_authorized_at(self):
        self.assertFalse(pd.isnull(create_dataset_utilization(path)['test_authorized_at']).any())

    def test_numbering_elem_of_class(self):
        df = create_dataset_utilization(path)
        df = df.loc[df['class_id'] == 1]
        list_class_num = [x for x in df['class_test_number']]
        self.assertTrue(list_class_num, [1, 2, 3])

    def test_cols_header(self):
        dataset_utilization = create_dataset_utilization(path)
        cols_names = ['class_id', 'class_name', 'teaching_hours', 'test_id', 'test_level',
                      'test_created_at', 'test_authorized_at', 'class_test_number']
        self.assertEqual(cols_names, list(dataset_utilization.columns.values))


if __name__ == '__main__':
    unittest.main()
