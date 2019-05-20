import unittest
from app.load_files import load_file, modify_class_file
import os

path = os.path.dirname(os.path.dirname(__file__))


class TestLoadFiles(unittest.TestCase):

    def test_load_test_level_file_num_of_cols(self):
        self.assertEqual(5, load_file('test_level', path).shape[1])

    def test_load_test_file_num_of_cols(self):
        self.assertEqual(17, load_file('test', path).shape[1])

    def test_load_class_file_num_of_cols(self):
        self.assertEqual(9, load_file('class', path).shape[1])

    def test_load_test_level_file_num_of_rows(self):
        self.assertEqual(5, load_file('test_level', path).shape[0])

    def test_load_test_file_num_of_rows(self):
        self.assertEqual(13039, load_file('test', path).shape[0])

    def test_load_class_file_num_of_rows(self):
        self.assertEqual(615, load_file('class', path).shape[0])

    def test_if_class_file_correct_without_slash(self):
        class_file = modify_class_file(path)
        self.assertFalse(32 in class_file.id.values)

    def test_if_class_file_correct_without_non_ascii_signs(self):
        class_file = modify_class_file(path)
        self.assertFalse(621 in class_file.id.values)


if __name__ == '__main__':
    unittest.main()
