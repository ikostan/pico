"""
Test suite for lesson 11.
"""

import unittest
from unittest.mock import MagicMock
# pylint: disable=import-error
from lessons.lesson_11.main import (
    PIN_NUM,
    analogOut,
    STEPS,
    MAX_READ_VAL,
    CONSTANT
)


class Lesson11TestCase(unittest.TestCase):
    """
    Test case for lesson 11.
    """
    def test_pin_num_value(self):
        """
        PIN_NUM value should be equal to 16.
        :return:
        """
        self.assertEqual(PIN_NUM, 16)

    def test_pin_num_data_type(self):
        """
        PIN_NUM data type should be int.
        :return:
        """
        self.assertIsInstance(PIN_NUM, int)

    def test_steps_value(self):
        """
        STEPS value should be equal to 50.
        :return:
        """
        self.assertEqual(STEPS, 50)

    def test_steps_data_type(self):
        """
        STEPS data type should be int.
        :return:
        """
        self.assertIsInstance(STEPS, int)

    def test_analog_out_duty_u16(self):
        """
        Mocking and testing analogOut.duty_u16()
        :return:
        """
        v = 0
        analogOut.duty_u16 = MagicMock()
        analogOut.duty_u16(v)
        analogOut.duty_u16.return_value = v
        self.assertEqual(analogOut.duty_u16(), v)

    def test_max_read_val_value(self):
        """
        MAX_READ_VAL value should be equal to 65550.
        :return:
        """
        self.assertEqual(MAX_READ_VAL, 65550)

    def test_max_read_val_data_type(self):
        """
        MAX_READ_VAL data type should be int.
        :return:
        """
        self.assertIsInstance(MAX_READ_VAL, int)

    def test_constant_value(self):
        """
        CONSTANT value should be equal to 1.248336.
        :return:
        """
        self.assertEqual(CONSTANT, 1.248336)

    def test_constant_data_type(self):
        """
        CONSTANT data type should be float.
        :return:
        """
        self.assertIsInstance(CONSTANT, float)


if __name__ == '__main__':
    unittest.main()
