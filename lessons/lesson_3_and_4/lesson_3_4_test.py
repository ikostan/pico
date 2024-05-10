import unittest
from lessons.lesson_3_and_4.lesson_3_and_4 import get_val


class MyTestCase(unittest.TestCase):
    def test_get_val_true(self):
        n_val = True
        result = get_val(n_val)
        expected = 1
        msg = f'n_val: {n_val}, result: {result}, expected: {expected}'
        self.assertEqual(result, expected, msg)

    def test_get_val_false(self):
        n_val = False
        result = get_val(n_val)
        expected = 0
        msg = f'n_val: {n_val}, result: {result}, expected: {expected}'
        self.assertEqual(result, expected, msg)


if __name__ == '__main__':
    unittest.main()
