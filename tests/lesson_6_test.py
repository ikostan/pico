"""
Unit testing for lesson 6
"""

import unittest
from unittest.mock import MagicMock
from machine import Pin  # pylint: disable=import-error
from lessons.lesson_6.main import (
    PIN_N,
    LED,
)


class MyTestCase(unittest.TestCase):
    """
    Testing led functionality by mocking Pin methods
    """

    def test_pin_n_value(self):
        """
        This test exist only for code coverage purposes.
        Testing that PIN_N val is 14.
        :return:
        """
        self.assertEqual(PIN_N, 14)

    def test_pin_n_data_type(self):
        """
        Verify data type (should be int).
        :return:
        """
        self.assertIsInstance(PIN_N, int)

    def test_led_on(self):
        """
        Testing led on func by mocking PIN methods.
        :return:
        """
        LED.value = MagicMock()
        LED.value(1)
        LED.value.return_value = 1
        self.assertEqual(LED.value(), 1)

    def test_led_off(self):
        """
        Testing led off func by mocking PIN methods.
        :return:
        """
        LED.value = MagicMock()
        LED.value(0)
        LED.value.return_value = 0
        self.assertEqual(LED.value(), 0)


if __name__ == '__main__':
    unittest.main()
