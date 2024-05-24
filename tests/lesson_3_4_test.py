"""
Unit testing lessons 3 and 4.
"""

import unittest
from lessons.lesson_3_and_4.main import (  # pylint: disable=import-error
    get_val,        # pylint: disable=import-error
    numbers,        # pylint: disable=import-error
    all_pins,       # pylint: disable=import-error
    set_all_pins,   # pylint: disable=import-error
    set_pin_val,    # pylint: disable=import-error
)


class Lesson3and4TestCase(unittest.TestCase):
    """
    Lessons 3 and 4 test case.
    """

    def test_set_pin_value_off(self):
        """
        Pin value should return 0 after it was updated by
        set_pin_value function
        """
        led = all_pins[0]
        set_pin_val(led, 0)

        led.value = MagicMock()
        led.value.return_value = 0
        
        self.assertEqual(led.value(), 0)

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
        self.assertTupleEqual(numbers[0], (False, False, False, False))

    def test_numbers_7(self):
        """
        Testing numbers dictionary -> key 7
        """
        self.assertIsInstance(numbers[7], tuple)
        self.assertTupleEqual(numbers[7], (False, True, True, True))

    def test_numbers_15(self):
        """
        Testing numbers dictionary -> key 15
        """
        self.assertIsInstance(numbers[15], tuple)
        self.assertTupleEqual(numbers[15], (True, True, True, True))

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
