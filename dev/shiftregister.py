import RPi.GPIO as GPIO
from time import sleep


class ShiftRegister:
    def __init__(
        self, data_pin=11, clock_pin=13, latch_pin=15, daisy_chain=10, delay=0.001
    ):
        self.data_pin = data_pin
        self.clock_pin = clock_pin
        self.latch_pin = latch_pin
        self.daisy_chain = daisy_chain
        self.delay = delay
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup((latch_pin, data_pin, clock_pin), GPIO.OUT)
        GPIO.output((latch_pin, data_pin, clock_pin), GPIO.LOW)
        self.clear()

    def pulse(self, pin):
        GPIO.output(pin, GPIO.LOW)
        sleep(self.delay)
        GPIO.output(pin, GPIO.HIGH)
        sleep(self.delay)
        GPIO.output(pin, GPIO.LOW)
        sleep(self.delay)

    def shiftOut(self, data_list):
        """Writes data to shift register(s)"""
        if len(data_list) != 8 * self.daisy_chain:
            raise Exception(
                "Input data must contain {} bytes!".format(self.daisy_chain)
            )
        for d in data_list:
            if d not in (0, 1):
                raise Exception("Input data must be in binary format.")
        # send serial data
        for d in data_list:
            GPIO.output(self.data_pin, d)  # write one bit to data pin
            self.pulse(self.clock_pin)
        # show data on output
        self.pulse(self.latch_pin)
        # save current output of shift register
        self.output = data_list

    def clear(self):
        self.shiftOut([0 for _ in range(self.daisy_chain * 8)])
