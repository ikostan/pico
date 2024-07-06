"""
Test suite for lesson 12.
"""

import io
from contextlib import redirect_stdout
import unittest
# from unittest.mock import MagicMock
# pylint: disable=import-error
from lessons.lesson_12.main import (
    colors,
    pins,
    pwms,
    calc_pwm,
    pwms_off,
    initial_setup,
    led_on,
    # get_color
)


class Lesson12TestCase(unittest.TestCase):
    """
    Test case for lesson 12.
    """

    def test_colors_data_type(self):
        """
        colors data type should be dictionary.
        :return:
        """
        self.assertIsInstance(colors, dict)

    def test_pins_data_type(self):
        """
        pins data type should be dictionary.
        :return:
        """
        self.assertIsInstance(pins, dict)

    def test_pwms_data_type(self):
        """
        pwms data type should be tuple.
        :return:
        """
        self.assertIsInstance(pwms, tuple)

    def test_calc_pwm_0(self):
        """
        Pass 0 as color_value.
        Result should be 0.
        :return:
        """
        color_value = 0
        self.assertEqual(calc_pwm(color_value), 0)

    def test_calc_pwm_255(self):
        """
        Pass 255 as color_value.
        Result should be 65550.
        :return:
        """
        color_value = 255
        self.assertEqual(calc_pwm(color_value), 65550)

    def test_calc_pwm_165(self):
        """
        Pass 165 as color_value.
        Result should be 42414.
        :return:
        """
        color_value = 165
        self.assertEqual(calc_pwm(color_value), 42414)

    def test_pwms_off_returns_none(self):
        """
        pwms_off should return none.
        :return:
        """
        self.assertIsNone(pwms_off())

    def test_initial_setup_returns_none(self):
        """
        initial_setup should return none.
        :return:
        """
        self.assertIsNone(initial_setup())

    def test_led_on_print_debug_red(self):
        """
        Test that led_on prints proper debug line
        for red color.
        Source:
        https://stackoverflow.com/questions/69036159/how-to-write-python-unit-test-for-the-print-statement
        :return:
        """
        color: str = 'red'  # color RGB values 255, 0, 0
        txt: str = f"\nDEBUG -> R: {65550}, G: {0}, B: {0}\n"

        f = io.StringIO()
        with redirect_stdout(f):
            led_on(color)

        self.assertTrue(txt in f.getvalue())

    def test_led_on_print_debug_white(self):
        """
        Test that led_on prints proper debug line
        for white color.
        Source:
        https://stackoverflow.com/questions/69036159/how-to-write-python-unit-test-for-the-print-statement
        :return:
        """
        color: str = 'white'  # color RGB values 255, 255, 255
        txt: str = f"\nDEBUG -> R: {65550}, G: {65550}, B: {65550}\n"

        f = io.StringIO()
        with redirect_stdout(f):
            led_on(color)

        self.assertTrue(txt in f.getvalue())


if __name__ == '__main__':
    unittest.main()
