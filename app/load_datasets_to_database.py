import sqlite3
import pandas as pd
import os


def create_connection(path):
    try:
        conn = sqlite3.connect(path + 'TestDB.db')
        return conn
    except sqlite3.Error as e:
        print(e)


def load_datasets_to_database():
    path = os.path.dirname(os.path.dirname(__file__))

    test_utilization = pd.read_csv(path + '/app/files/test_utilization.csv')
    test_average_scores = pd.read_csv(path + '/app/files/test_average_scores.csv')

    conn = create_connection(path)

    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS test_utilization
                 ('class_id', 'class_name', 'teaching_hours', 'test_id', 'test_level',
                  'test_created_at', 'test_authorized_at', 'class_test_number')''')


    c.execute('''CREATE TABLE IF NOT EXISTS test_average_scores
    ('class_id', 'class_name', 'teaching_hours', 'avg_class_test_overall_score')''')

    c.execute('''DELETE FROM test_utilization''')
    c.execute('''DELETE FROM test_average_scores''')

    test_utilization.to_sql('test_utilization', conn, if_exists='append', index=False)
    test_average_scores.to_sql('test_average_scores', conn, if_exists='append', index=False)

    conn.commit()


load_datasets_to_database()

