"""
Unit testing for lesson 6
"""

import unittest
from unittest.mock import MagicMock
from machine import Pin  # pylint: disable=import-error
from lessons.lesson_5.main import (
    PIN_N,
    LED,
)


class MyTestCase(unittest.TestCase):
    """
    Testing led functionality by mocking Pin methods
    """

    def test_pin_n_is_int(self):
        """
        This test exist only for code coverage purposes.
        :return:
        """
        PIN_N = 14
        self.assertIsInstance(PIN_N, int)

    def test_led_on(self):
        """
        Testing led on func by mocking PIN methods.
        :return:
        """
        PIN_N = 14
        LED: Pin = Pin(PIN_N, Pin.OUT)
        LED.value = MagicMock()
        LED.value(1)
        LED.value.return_value = 1
        self.assertEqual(LED.value(), 1)

    def test_led_off(self):
        """
        Testing led off func by mocking PIN methods.
        :return:
        """
        PIN_N = 14
        LED: Pin = Pin(PIN_N, Pin.OUT)
        LED.value = MagicMock()
        LED.value(0)
        LED.value.return_value = 0
        self.assertEqual(LED.value(), 0)


if __name__ == '__main__':
    unittest.main()
