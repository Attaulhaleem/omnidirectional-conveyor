import RPi.GPIO as GPIO
import time

# define PINs according to cabling
dataPIN = 11
latchPIN = 13
clockPIN = 15

# delay for level change (seconds)
delay = 0.01

# set pins to putput
GPIO.setmode(GPIO.BOARD)
GPIO.setup((dataPIN, latchPIN, clockPIN), GPIO.OUT)
GPIO.output((dataPIN, latchPIN, clockPIN), GPIO.LOW)


def pulse_clock():
    GPIO.output(clockPIN, GPIO.LOW)
    time.sleep(delay)
    GPIO.output(clockPIN, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(clockPIN, GPIO.LOW)
    time.sleep(delay)


def pulse_latch():
    GPIO.output(latchPIN, GPIO.LOW)
    time.sleep(delay)
    GPIO.output(latchPIN, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(latchPIN, GPIO.LOW)
    time.sleep(delay)


# define shift register update function
def shift_update(input):
    # put latch down to start data sending
    # GPIO.output(clock, 0)
    # GPIO.output(latchPIN, 0)
    # time.sleep(0.01)
    # GPIO.output(clock, 1)

    # load data in reverse order
    for i in range(7, -1, -1):
        # GPIO.output(clock, 0)
        # time.sleep(0.01)
        GPIO.output(dataPIN, int(input[i]))
        pulse_clock()
        # time.sleep(0.01)
        # GPIO.output(clock, 1)
        # time.sleep(0.01)


def clear(bytes):
    for _ in range(bytes):
        for i in range(7, -1, -1):
            GPIO.output(dataPIN, GPIO.LOW)
            pulse_clock()
    pulse_latch()


# def shift_latch(clock, latch):
#     # put latch up to store data on register
#     # GPIO.output(clock, 0)
#     GPIO.output(latch, 1)
#     time.sleep(0.1)
#     # GPIO.output(clock, 1)


clear(4)
shift_update([0, 0, 1, 0, 0, 0, 0, 0])
shift_update([0, 0, 1, 0, 0, 0, 0, 0])
shift_update([0, 0, 0, 0, 0, 0, 0, 1])
shift_update([0, 0, 1, 0, 0, 1, 0, 0])
pulse_latch()
time.sleep(1000)

# PINs final cleaning
GPIO.cleanup()
