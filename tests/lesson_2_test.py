"""
Test suite for lesson 2.
"""

import unittest
from unittest.mock import MagicMock
from lessons.lesson_2.main import (  # pylint: disable=import-error
    LED
)


class Lesson2TestCase(unittest.TestCase):
    """
    Testing led functionality by mocking Pin methods
    """

    def test_led_on(self):
        """
        Mock the led.value() function and return 1 always
        :return:
        """
        LED.value = MagicMock()
        LED.on()
        LED.value.return_value = 1
        self.assertEqual(LED.value(), 1)

    def test_led_off(self):
        """
        Mock the led.value() function and return 0 always
        :return:
        """
        LED.value = MagicMock()
        LED.off()
        LED.value.return_value = 0
        self.assertEqual(LED.value(), 0)


if __name__ == '__main__':
    unittest.main()
