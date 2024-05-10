"""
Unit testing lessons 3 and 4.
"""

import unittest
from lessons.lesson_3_and_4.lesson_3_and_4 import get_val  # pylint: disable=import-error


class Lesson3and4TestCase(unittest.TestCase):
    """
    Lessons 3 and for test case.
    """
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
