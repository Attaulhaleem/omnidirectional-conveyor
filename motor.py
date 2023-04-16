import RPi.GPIO as GPIO
import time

# use board pin numberings
GPIO.setmode(GPIO.BOARD)

# shift register pins
data_pin = 11
clock_pin = 13
latch_pin = 15

# motor states
FORWARD = (1, 0)
BACKWARD = (0, 1)
RELEASE = (0, 0)

# module states
IDLE = [RELEASE, RELEASE, RELEASE, RELEASE]
UP_RIGHT = [RELEASE, FORWARD, BACKWARD, RELEASE]
RIGHT = [FORWARD, RELEASE, BACKWARD, RELEASE]
DOWN_RIGHT = [FORWARD, BACKWARD, RELEASE, RELEASE]
DOWN_LEFT = [RELEASE, BACKWARD, FORWARD, RELEASE]
LEFT = [BACKWARD, RELEASE, FORWARD, RELEASE]
UP_LEFT = [BACKWARD, FORWARD, RELEASE, RELEASE]
CLOCKWISE = [FORWARD, FORWARD, FORWARD, RELEASE]
ANTI_CLOCKWISE = [BACKWARD, BACKWARD, BACKWARD, RELEASE]


def setup():
    """
    Pin Declarations (DS, SH, ST)
    """
    GPIO.setup((latch_pin, data_pin, clock_pin), GPIO.OUT)
    GPIO.output((latch_pin, data_pin, clock_pin), GPIO.LOW)
    clear(10)


def pulse(pin, delay=0.001):
    GPIO.output(pin, GPIO.LOW)
    time.sleep(delay)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(delay)


def getSingleBinaryList(state_list):
    """
    Format data for writing to single shift register
    """
    print(state_list)
    if len(state_list) != 4:
        raise Exception("Input list must contain 4 motor states.")
    for state in state_list:
        if state not in (FORWARD, BACKWARD, RELEASE):
            raise Exception("Invalid motor state in input list.")
    # convert to flat list
    motor_values = [val for state in state_list for val in state]
    # see shield schematic [M3 and M4 were replaced on my shield] (http://wiki.sunfounder.cc/images/f/ff/L293D_schematic.png)
    # output format [3A, 4B, 3B, 2B, 1B, 1A, 2A, 4A]
    shield_config = (4, 7, 5, 3, 1, 0, 2, 6)
    print([motor_values[i] for i in shield_config])
    return [motor_values[i] for i in shield_config]


def getChainedBinaryList(state_list):
    """
    Format data for writing to daisy chained shift registers
    """
    motor_values = list()
    for sub_list in state_list:
        motor_values.append(getSingleBinaryList(sub_list))
    # first motor values must be sent last
    motor_values.reverse()
    # convert to flat list
    motor_values = [val for sub_list in motor_values for val in sub_list]
    return motor_values


def shiftOut(data_list):
    """
    Writes data to shift register
    """
    for d in data_list:
        if d not in (0, 1):
            raise Exception("Input data must be in binary format.")
    # send serial data
    for d in data_list:
        GPIO.output(data_pin, d)  # write one bit to data pin
        pulse(clock_pin)
    # show data on output
    pulse(latch_pin)


def clear(bytes):
    shiftOut([0 for _ in range(bytes * 8)])


SampleStates = [
    IDLE,
    UP_RIGHT,
    RIGHT,
    DOWN_RIGHT,
    DOWN_LEFT,
    LEFT,
    UP_LEFT,
    CLOCKWISE,
    ANTI_CLOCKWISE,
]

ChainedSampleStates = [CLOCKWISE for _ in range(10)]
