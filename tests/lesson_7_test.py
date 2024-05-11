import unittest
from lessons.lesson_7.lesson_7 import (  # pylint: disable=import-error
    all_led_off,
    value_to_color,
    turn_led_on,
    converter
)


class Lesson7TestCase(unittest.TestCase):
    """
    Test case for lesson 7.
    """

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

    def test_converter_type(self):
        """
        Converter output type should be integer.
        :return:
        """
        read_value = 0
        val = converter(read_value)
        t = type(val)
        expected = type(0)
        msg = f"read_value: {read_value}, val{val}, t: {t}, expected: {expected}"
        self.assertEqual(t, expected, msg)


if __name__ == '__main__':
    unittest.main()
