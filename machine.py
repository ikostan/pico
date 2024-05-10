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

    def off(self)
        """
        Set pin to “0” output level.
        :return: 
        """
        print("pin off")


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
    # fake ADC to Digital convertor
    pin = 0

    def __init__(self, pin):
        self.pin = pin

    def read(self):
        return 1024


class I2C():

    def __init__(id=None, sda=None, scl=None):
        pass
