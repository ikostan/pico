import unittest
from unittest.mock import MagicMock
from lessons.lesson_5.main import (
    pin_read,  # pylint: disable=import-error
    SLOPE,     # pylint: disable=import-error
    X_MIN,     # pylint: disable=import-error
)


class Lesson5TestCase(unittest.TestCase):
    def test_voltage_0(self):
        """
        Reading Analog Voltage -> min value is 96
        Should be converted to 0 volt
        """
        pin_read.read_u16 = MagicMock()
        pin_read.read_u16.return_value = 96
        X = pin_read.read_u16()  # pylint: disable=E1111
        v = (SLOPE * X) - (SLOPE * X_MIN)
        self.assertEqual(v, 0)

    def test_voltage_mid_value(self):
        """
        Reading Analog Voltage -> mid-value
        Should be converted to 1.65 volt
        """
        pin_read.read_u16 = MagicMock()
        pin_read.read_u16.return_value = (65535 - 96) / 2
        X = pin_read.read_u16()  # pylint: disable=E1111
        v = (SLOPE * X) - (SLOPE * X_MIN)
        self.assertEqual(round(v, 2), 1.65)

    def test_voltage_3_3(self):
        """
        Reading Analog Voltage -> max value is 65535
        Should be converted to 3.3 volt
        """
        pin_read.read_u16 = MagicMock()
        pin_read.read_u16.return_value = 65535
        X = pin_read.read_u16()  # pylint: disable=E1111
        v = (SLOPE * X) - (SLOPE * X_MIN)
        self.assertEqual(v, 3.3)


if __name__ == '__main__':
    unittest.main()
