from app.io.input import read_from_file_builtin, read_from_file_pandas
import unittest
import os
import pandas as pd


class TestReadFromFile(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_file.txt'
        self.test_csv = 'test_file.csv'
        with open(self.test_file, 'w') as f:
            f.write('Hello, World!')
        self.test_data = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        self.test_data.to_csv(self.test_csv, index=False)

    def tearDown(self):
        os.remove(self.test_file)
        os.remove(self.test_csv)

    # read_from_file_builtin tests
    def test_read_existing_file(self):
        content = read_from_file_builtin(self.test_file)
        self.assertEqual(content, 'Hello, World!')

    def test_read_non_existing_file(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_builtin('non_existing_file.txt')

    def test_read_empty_file(self):
        with open(self.test_file, 'w') as f:
            pass
        content = read_from_file_builtin(self.test_file)
        self.assertEqual(content, '')

    # read_from_file_pandas tests
    def test_read_existing_csv(self):
        df = read_from_file_pandas(self.test_csv)
        pd.testing.assert_frame_equal(df, self.test_data)

    def test_read_non_existing_csv(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_pandas('non_existing_file.csv')

    def test_read_empty_csv(self):
        with open(self.test_csv, 'w') as f:
            pass
        with self.assertRaises(pd.errors.EmptyDataError):
            read_from_file_pandas(self.test_csv)


if __name__ == '__main__':
    unittest.main()
