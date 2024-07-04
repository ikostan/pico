"""
Test suite for lesson 1.
"""

import unittest
from unittest.mock import MagicMock
# pylint: disable=import-error
from lessons.lesson_1.main import (
    LED,
    toggle_is_on
)


class Lesson1TestCase(unittest.TestCase):
    """
    Testing led functionality by mocking Pin methods
    """

    def test_toggle_is_on_0(self):
        """
        Testing toggle_is_on function.
        Should return 1 when input param is 0.
        :return:
        """
        self.assertEqual(toggle_is_on(0), 1)

    def test_toggle_is_on_1(self):
        """
        Testing toggle_is_on function.
        Should return 0 when input param is 1.
        :return:
        """
        self.assertEqual(toggle_is_on(1), 0)

    def test_toggle_is_on_error(self):
        """
        Testing toggle_is_on function.
        Should return error when input param is invalid.
        :return:
        """
        val = 2
        err = f"Invalid parameter: {val}! Only 1 and 0 allowed."

        with self.assertRaises(ValueError) as e:
            toggle_is_on(val)

        self.assertEqual(str(e.exception), err)

    def test_led_on(self):
        """
        Mock the led.value() function and return 1 always
        :return:
        """
        LED.value = MagicMock()
        LED.value(1)
        LED.value.return_value = 1
        self.assertEqual(LED.value(), 1)

    def test_led_off(self):
        """
        Mock the led.value() function and return 0 always
        :return:
        """
        LED.value = MagicMock()
        LED.value(0)
        LED.value.return_value = 0
        self.assertEqual(LED.value(), 0)


if __name__ == '__main__':
    unittest.main()
