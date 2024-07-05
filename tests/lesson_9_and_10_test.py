"""
Test suite for lesson 9 and 10.
"""

import unittest
# pylint: disable=import-error
from lessons.lesson_9_and_10.main import (
    VoltageError,
    analogOut,
    PIN_NUM
)


class Lesson9And10TestCase(unittest.TestCase):
    """
    Test case for lesson 9 and 10.
    """

    def test_pin_num_data_type(self):
        """
        PIN_NUM data type should be int.
        :return:
        """
        self.assertIsInstance(PIN_NUM, int)

    def test_pin_num_value(self):
        """
        PIN_NUM value should be 16.
        :return:
        """
        self.assertIsEqual(PIN_NUM, 16)

    def test_voltage_error(self):
        """
        Verify VoltageError message.
        :return:
        """
        user_input = 5
        err = f"Invalid voltage value -> {user_input}."
        with self.assertRaises(VoltageError) as e:
            raise VoltageError(f"Invalid voltage value -> {user_input}.")

        self.assertEqual(str(e.exception), err)


if __name__ == '__main__':
    unittest.main()
