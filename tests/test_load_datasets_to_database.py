import unittest
import sqlite3
import pandas as pd
import os

path = os.path.dirname(os.path.dirname(__file__))


class TestLoadDatasetsToDatabase(unittest.TestCase):

    def test_num_of_rows_in_test_utilization_database(self):
        test_utilization = pd.read_csv(path + '/app/files/test_utilization.csv')
        conn = sqlite3.connect(path + '/db/TestDB.db')
        c = conn.cursor()
        c.execute(''' SELECT * from test_utilization''')
        self.assertEqual(test_utilization.shape[0], len(c.fetchall()))

    def test_num_of_rows_in_average_scores_database(self):
        test_average_scores = pd.read_csv(path + '/app/files/test_average_scores.csv')
        conn = sqlite3.connect(path + '/db/TestDB.db')
        c = conn.cursor()
        c.execute(''' SELECT * from test_average_scores''')
        self.assertEqual(test_average_scores.shape[0], len(c.fetchall()))

    def test_data_in_database(self):
        test_average_scores = pd.read_csv(path + '/app/files/test_average_scores.csv')
        only_48 = test_average_scores.loc[test_average_scores['class_id'] == 48]
        conn = sqlite3.connect(path + '/db/TestDB.db')
        c = conn.cursor()
        c.execute(''' SELECT * from test_average_scores where class_id=48''')
        row = [item for item in c.fetchall()[0]]
        self.assertEqual(only_48.values.tolist(), [row])


if __name__ == '__main__':
    unittest.main()
