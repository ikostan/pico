"""
Test suite for lesson 13.
"""

import unittest
# pylint: disable=import-error
from lessons.lesson_13.main import (
    led_red,
)


class Lesson13TestCase(unittest.TestCase):
    """
    Test case for lesson 13.
    """
    def test_led_red_duty_u16(self):
        """
        Mocking and testing analogOut.duty_u16()
        :return:
        """
        f = 1000
        led_red.freq = MagicMock()
        led_red.freq(f)
        led_red.freq.return_value = f
        self.assertEqual(led_red.freq(), f)


if __name__ == '__main__':
    unittest.main()
