import unittest
from app.create_dataset_utilization import create_dataset_utilization
import os
import pandas as pd


path = os.path.dirname(os.path.dirname(__file__))


class TestCreateDatasetUtilization(unittest.TestCase):

    def test_isnull_test_authorized_at(self):
        self.assertFalse(pd.isnull(create_dataset_utilization(path)['test_authorized_at']).any())


if __name__ == '__main__':
    unittest.main()
