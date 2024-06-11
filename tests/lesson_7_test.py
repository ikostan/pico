"""
Test suite for lesson 7 and 8.
"""

import unittest
from lessons.lesson_7_and_8.main import (  # pylint: disable=import-error
    # all_led_off,
    value_to_color,
    # turn_led_on,
    converter
)


class Lesson7TestCase(unittest.TestCase):
    """
    Test case for lesson 7 and 8.
    """

    def test_value_to_color_return_type(self):
        """
        Return type should be string.
        :return:
        """
        expected = type("YELLOW")
        test_val = 80
        result = value_to_color(test_val)
        t = type(result)
        msg = f'expected: {expected}, results: {t}, test_val: {test_val}'
        self.assertIsInstance(result, str, msg)

    def test_value_to_color_red_min(self):
        """
        95 should correspond to red color.
        :return:
        """
        expected = "RED"
        test_val = 95
        result = value_to_color(test_val)
        msg = f'expected: {expected}, results: {result}, test_val: {test_val}'
        self.assertEqual(result, expected, msg)

    def test_value_to_color_red_max(self):
        """
        100 should correspond to red color.
        :return:
        """
        expected = "RED"
        test_val = 100
        result = value_to_color(test_val)
        msg = f'expected: {expected}, results: {result}, test_val: {test_val}'
        self.assertEqual(result, expected, msg)

    def test_value_to_color_red_mid(self):
        """
        97 should correspond to red color.
        :return:
        """
        expected = "RED"
        test_val = 97
        result = value_to_color(test_val)
        msg = f'expected: {expected}, results: {result}, test_val: {test_val}'
        self.assertEqual(result, expected, msg)

    def test_value_to_color_yellow_min(self):
        """
        80 should correspond to yellow color.
        :return:
        """
        expected = "YELLOW"
        test_val = 80
        result = value_to_color(test_val)
        msg = f'expected: {expected}, results: {result}, test_val: {test_val}'
        self.assertEqual(result, expected, msg)

    def test_value_to_color_yellow_max(self):
        """
        94 should correspond to yellow color.
        :return:
        """
        expected = "YELLOW"
        test_val = 94
        result = value_to_color(test_val)
        msg = f'expected: {expected}, results: {result}, test_val: {test_val}'
        self.assertEqual(result, expected, msg)

    def test_value_to_color_yellow_mid(self):
        """
        87 should correspond to yellow color.
        :return:
        """
        expected = "YELLOW"
        test_val = 87
        result = value_to_color(test_val)
        msg = f'expected: {expected}, results: {result}, test_val: {test_val}'
        self.assertEqual(result, expected, msg)

    def test_value_to_color_green_min(self):
        """
        Zero should correspond to green color.
        :return:
        """
        expected = "GREEN"
        test_val = 0
        result = value_to_color(test_val)
        msg = f'expected: {expected}, results: {result}, test_val: {test_val}'
        self.assertEqual(result, expected, msg)

    def test_value_to_color_green_max(self):
        """
        79 should correspond to green color.
        :return:
        """
        expected = "GREEN"
        test_val = 79
        result = value_to_color(test_val)
        msg = f'expected: {expected}, results: {result}, test_val: {test_val}'
        self.assertEqual(result, expected, msg)

    def test_value_to_color_green_mid(self):
        """
        40 should correspond to green color.
        :return:
        """
        expected = "GREEN"
        test_val = 40
        result = value_to_color(test_val)
        msg = f'expected: {expected}, results: {result}, test_val: {test_val}'
        self.assertEqual(result, expected, msg)

    def test_converter_max(self):
        """
        Converter output should be 100 for read pin value 65535.
        :return:
        """
        read_value = 65535
        val = converter(read_value)
        expected = 100
        msg = f"read_value: {read_value}, val{val}, expected: {expected}"
        self.assertEqual(val, expected, msg)

    def test_converter_min(self):
        """
        Converter output should be 0 for read pin value 0.
        :return:
        """
        read_value = 0
        val = converter(read_value)
        expected = 0
        msg = f"read_value: {read_value}, val{val}, expected: {expected}"
        self.assertEqual(val, expected, msg)

    def test_converter_mid_range_50(self):
        """
        Converter output should be 50 for read pin value 32768.
        :return:
        """
        read_value = 32768
        val = converter(read_value)
        expected = 50
        msg = f"read_value: {read_value}, val{val}, expected: {expected}"
        self.assertEqual(val, expected, msg)

    def test_converter_mid_range_49(self):
        """
        Converter output should be 49 for read pin value 32767.
        :return:
        """
        read_value = 32767
        val = converter(read_value)
        expected = 49
        msg = f"read_value: {read_value}, val{val}, expected: {expected}"
        self.assertEqual(val, expected, msg)

    def test_converter_return_type(self):
        """
        Converter output type should be integer.
        :return:
        """
        read_value = 0
        val = converter(read_value)
        t = type(val)
        expected = type(0)
        msg = f"read_value: {read_value}, val{val}, t: {t}, expected: {expected}"
        self.assertIsInstance(val, int, msg)


if __name__ == '__main__':
    unittest.main()
