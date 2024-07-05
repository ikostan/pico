"""
Test suite for lesson 9 and 10.
"""

import unittest
from unittest.mock import MagicMock
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

    def test_analog_out_freq(self):
        """
        Mocking and testing analogOut.freq()
        :return:
        """
        f = 1000
        analogOut.freq = MagicMock()
        analogOut.freq(f)
        analogOut.freq.return_value = f
        self.assertEqual(analogOut.freq(), f)

    def test_analog_out_duty_u16(self):
        """
        Mocking and testing analogOut.duty_u16()
        :return:
        """
        v = 0
        analogOut.freq = MagicMock()
        analogOut.duty_u16(v)
        analogOut.duty_u16.return_value = v
        self.assertEqual(analogOut.duty_u16(), v)

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
        self.assertEqual(PIN_NUM, 16)

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
