import RPi.GPIO as GPIO
import time

# define PINs according to cabling
dataPIN = 11
latchPIN = 13
clockPIN = 15

# set pins to putput
GPIO.setmode(GPIO.BOARD)
GPIO.setup((dataPIN, latchPIN, clockPIN), GPIO.OUT)

# define shift register update function
def shift_update(input, data, clock, latch):
    # put latch down to start data sending
    # GPIO.output(clock, 0)
    GPIO.output(latch, 0)
    time.sleep(0.01)
    # GPIO.output(clock, 1)

    # load data in reverse order
    for i in range(7, -1, -1):
        GPIO.output(clock, 0)
        time.sleep(0.01)
        GPIO.output(data, int(input[i]))
        time.sleep(0.01)
        GPIO.output(clock, 1)
        time.sleep(0.01)


def shift_latch(clock, latch):
    # put latch up to store data on register
    # GPIO.output(clock, 0)
    GPIO.output(latch, 1)
    time.sleep(0.1)
    # GPIO.output(clock, 1)


shift_update([0, 0, 1, 0, 0, 1, 0, 0], dataPIN, clockPIN, latchPIN)
shift_update([0, 0, 1, 0, 0, 1, 0, 0], dataPIN, clockPIN, latchPIN)
shift_update([0, 0, 1, 0, 0, 1, 0, 0], dataPIN, clockPIN, latchPIN)
shift_latch(clockPIN, latchPIN)
time.sleep(1000)

# PINs final cleaning
GPIO.cleanup()
