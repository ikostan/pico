"""
This is machine module stubb.
Created for testing purposes only.
"""
# machine stubb

class Pin():
    """
    A pin object is used to control I/O pins
    (also known as GPIO - general-purpose input/output).
    Pin objects are commonly associated with a physical pin that can drive
    an output voltage and read input voltages. The pin class has methods to
    set the mode of the pin (IN, OUT, etc) and methods to get and set the
    digital logic level. For analog control of a pin, see the ADC class.
    """
    OUT = 1

    def __init__(self, value, pin_type):
        """
        Re-initialise the pin using the given parameters.
        Only those arguments that are specified will be set.
        The rest of the pin peripheral state will remain unchanged.
        See the constructor documentation for details of the arguments.
        :param value:
        :param pin_type:
        """
        print('created Pin', value, pin_type)

    def on(self):
        """
        Set pin to “1” output level.
        :return:
        """
        print("pin on")

    def off(self):
        """
        Set pin to “0” output level.
        :return:
        """
        print("pin off")

    def value(self, val):
        """
        This method allows to set and get the value of the pin,
        depending on whether the argument x is supplied or not.
        :param val:
        :return:
        """
        print(f"pin value is {val}")

    def toggle(self):
        """
        n/a
        :return:
        """
        pass


class PWM():
    """
    This class provides pulse width modulation output.
    """
    pfreq = 50
    pduty = 77

    def __init__(self, value):
        """
        Modify settings for the PWM object. See the above
        constructor for details about the parameters.
        :param value:
        """
        print('created PWM with value ', value)

    def freq(self, value):
        """
        Get or set the current frequency of the PWM output.
        With no arguments the frequency in Hz is returned.
        With a single value argument the frequency is set to that value in Hz.
        The method may raise a ValueError if the frequency is outside the valid range.
        :param value:
        :return:
        """
        print('frequency')
        self.pfreq = value
        return value

    def duty(self, value):
        """
        n/a
        :param value:
        :return:
        """
        print('duty')
        self.pduty = value
        return value


class ADC():
    """
    The ADC class provides an interface to analog-to-digital converters,
    and represents a single endpoint that can sample a continuous voltage
    and convert it to a discrete value.
    """
    # fake ADC to Digital convertor
    pin = 0

    def __init__(self, pin):
        """
        Apply the given settings to the ADC. Only those arguments that are
        specified will be changed. See the ADC constructor above for what the arguments are.
        :param pin:
        """
        self.pin = pin

    def read(self):
        """
        n/a
        :return:
        """
        return 1024

    def read_16(self):
        """
        Take an analog reading and return an integer in the range 0-65535.
        The return value represents the raw reading taken by the ADC, scaled
        such that the minimum value is 0 and the maximum value is 65535.
        :return:
        """
        pass

    def read_uv(self):
        """
        Take an analog reading and return an integer value with units of micro volts.
        It is up to the particular port whether or not this value is calibrated,
        and how calibration is done.
        :return:
        """
        pass


class I2C():
    """
    I2C is a two-wire protocol for communicating between devices.
    At the physical level it consists of 2 wires: SCL and SDA,
    the clock and data lines respectively.

    I2C objects are created attached to a specific bus.
    They can be initialised when created, or initialised later on.

    Printing the I2C object gives you information about its configuration.
    """
    def __init__(self, id=None, sda=None, scl=None):
        pass
