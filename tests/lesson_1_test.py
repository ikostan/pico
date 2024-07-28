"""
Test suite for lesson 1.
"""

import unittest
from unittest.mock import MagicMock
from lessons.lesson_1.main import (
    LED,
    toggle_is_on,
    toggle_led,
    check_toggle_val
)


class Lesson1TestCase(unittest.TestCase):
    """
    Testing led functionality by mocking Pin methods
    """

    def test_check_toggle_val_0(self):
        """
        Pass 0 as a parameter.
        No errors.
        Returns None.
        :return:
        """
        t = check_toggle_val(0)
        self.assertIsNone(t)

    def test_check_toggle_val_1(self):
        """
        Pass 1 as a parameter.
        No errors.
        Returns None.
        :return:
        """
        t = check_toggle_val(1)
        self.assertIsNone(t)

    def test_check_toggle_val_type_error(self):
        """
        Pass string as a parameter.
        Verify exception text.
        :return:
        """
        val = '0'
        err = f"Invalid parameter type: {type(val)}! Only integers allowed."
        with self.assertRaises(TypeError) as e:
            check_toggle_val(val)
        self.assertEqual(str(e.exception), err)

    def test_toggle_led_off(self):
        """
        Turn LED off.
        Check function return value is None.
        Check led return value.
        :return:
        """
        t = toggle_led(0)
        LED.value = MagicMock()
        LED.value(0)
        LED.value.return_value = 0
        self.assertEqual(LED.value(), 0)
        self.assertIsNone(t)

    def test_toggle_led_on(self):
        """
        Turn LED on.
        Check function return value is None.
        Check led return value.
        :return:
        """
        t = toggle_led(1)
        LED.value = MagicMock()
        LED.value(1)
        LED.value.return_value = 1
        self.assertEqual(LED.value(), 1)
        self.assertIsNone(t)

    def test_toggle_led_error(self):
        """
        Pass invalid param value.
        Verify error.
        :return:
        """
        val = 3
        err = f"Invalid parameter: {val}! Only 1 and 0 allowed."

        with self.assertRaises(ValueError) as e:
            toggle_led(3)

        self.assertEqual(str(e.exception), err)

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
