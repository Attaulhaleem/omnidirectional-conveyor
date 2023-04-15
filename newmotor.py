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
    GPIO.output(clock, 0)
    GPIO.output(latch, 0)
    GPIO.output(clock, 1)

    # load data in reverse order
    for i in range(7, -1, -1):
        GPIO.output(clock, 0)
        GPIO.output(data, int(input[i]))
        GPIO.output(clock, 1)

    # put latch up to store data on register
    GPIO.output(clock, 0)
    GPIO.output(latch, 1)
    GPIO.output(clock, 1)


for i in range(8):
    shift_update(1 << i, dataPIN, clockPIN, latchPIN)
    time.sleep(1000)

# PINs final cleaning
GPIO.cleanup()
