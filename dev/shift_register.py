import RPi.GPIO as GPIO
from time import sleep


class ShiftRegister:
    """Class for writing data to daisy-chained 74HC595 shift register(s)."""

    def __init__(self, data_pin, clock_pin, latch_pin, daisy_chain, delay=0.001):
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
        """Give a rising edge to a pin."""
        GPIO.output(pin, GPIO.LOW)
        sleep(self.delay)
        GPIO.output(pin, GPIO.HIGH)
        sleep(self.delay)
        GPIO.output(pin, GPIO.LOW)
        sleep(self.delay)

    def shift_out(self, data_list):
        """MSB first shift out and latch data to shift register(s)."""
        # 1st bit in data_list is sent first
        # reverse to send LSB first
        data_list.reverse()
        # input validation
        if len(data_list) != self.daisy_chain * 8:
            raise Exception(
                "Input data must contain {} bytes!".format(self.daisy_chain)
            )
        for d in data_list:
            if d not in (0, 1):
                raise Exception("Input data must be in binary format.")
        # send serial data
        for d in data_list:
            # write one bit to data pin
            GPIO.output(self.data_pin, d)
            self.pulse(self.clock_pin)
        # show data on output
        self.pulse(self.latch_pin)
        # save current output of shift register
        self.output = data_list

    def clear(self):
        """Clear the output of shift register(s)."""
        self.shift_out([0 for _ in range(self.daisy_chain * 8)])


if __name__ == "__main__":
    sr1 = ShiftRegister(11, 13, 15, 5)
    sr2 = ShiftRegister(3, 5, 7, 5)
    data_list = []
    for _ in range(5):
        data_list.extend([0, 1, 1, 0, 0, 0, 0, 1])
    sr1.shift_out(data_list)
    sr2.shift_out(data_list)

    while True:
        try:
            sleep(1)
        except KeyboardInterrupt:
            print("Manually exiting program!")
            sr1.clear()
            sr2.clear()
            GPIO.cleanup()
            raise SystemExit
