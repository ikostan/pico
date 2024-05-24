"""
Unit testing lessons 3 and 4.
"""

import unittest
from lessons.lesson_3_and_4.main import (  # pylint: disable=import-error
    get_val,  # pylint: disable=import-error
    numbers,  # pylint: disable=import-error
)


class Lesson3and4TestCase(unittest.TestCase):
    """
    Lessons 3 and 4 test case.
    """

    def test_numbers_data_type(self):
        """
        Testing numbers dictionary -> datatype should be dict
        """
        self.assertIsInstance(numbers, dict)

    def test_numbers_0(self):
        """
        Testing numbers dictionary -> key 0
        """
        self.assertIsInstance(numbers[0], tuple)

    def test_get_val_return_type(self):
        """
        Testing get_val function.
        Return type should be int.
        :return:
        """
        n_val = True
        result = get_val(n_val)
        expected = type(1)
        msg = f'n_val: {n_val}, result: {result}, expected: {expected}'
        self.assertIsInstance(result, int, msg)

    def test_get_val_true(self):
        """
        Testing get_val function.
        True input should be converted into 1.
        :return:
        """
        n_val = True
        result = get_val(n_val)
        expected = 1
        msg = f'n_val: {n_val}, result: {result}, expected: {expected}'
        self.assertEqual(result, expected, msg)

    def test_get_val_false(self):
        """
        Testing get_val function.
        False input should be converted into 0.
        :return:
        """
        n_val = False
        result = get_val(n_val)
        expected = 0
        msg = f'n_val: {n_val}, result: {result}, expected: {expected}'
        self.assertEqual(result, expected, msg)


if __name__ == '__main__':
    unittest.main()
