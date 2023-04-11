import RPi.GPIO as GPIO
import time

# use board pin numberings
GPIO.setmode(GPIO.BOARD)

# shift register pins
latch_pin = 11
data_pin = 13
clock_pin = 15

# daisy chained shift registers
daisy_chain = 10

# motor states
FORWARD = (1, 0)
BACKWARD = (0, 1)
RELEASE = (0, 0)

# module states
IDLE = [RELEASE, RELEASE, RELEASE]
UP_RIGHT = [RELEASE, FORWARD, BACKWARD]
RIGHT = [FORWARD, RELEASE, BACKWARD]
DOWN_RIGHT = [FORWARD, BACKWARD, RELEASE]
DOWN_LEFT = [RELEASE, BACKWARD, FORWARD]
LEFT = [BACKWARD, RELEASE, FORWARD]
UP_LEFT = [BACKWARD, FORWARD, RELEASE]


def setup():
    """
    Pin Declarations (DS, SH, ST)
    """
    GPIO.setup(latch_pin, GPIO.OUT)
    GPIO.setup(data_pin, GPIO.OUT)
    GPIO.setup(clock_pin, GPIO.OUT)


def getSingleBinaryList(state_list):
    """
    Format data for writing to single shift register
    """
    if len(state_list) != 3:
        raise Exception("Input list must contain 3 motor states.")
    # fourth motor is not used
    state_list.append(RELEASE)
    for state in state_list:
        if state not in (FORWARD, BACKWARD, RELEASE):
            raise Exception("Invalid motor state in input list.")
    # convert to flat list
    motor_values = [val for state in state_list for val in state]
    # see shield schematic [M3 and M4 were replaced on my shield] (http://wiki.sunfounder.cc/images/f/ff/L293D_schematic.png)
    # output format [3A, 4B, 3B, 2B, 1B, 1A, 2A, 4A]
    shield_config = (4, 7, 5, 3, 1, 0, 2, 6)
    return [motor_values[i] for i in shield_config]


def getChainedBinaryList(state_list):
    """
    Format data for writing to daisy chained shift registers
    """
    if len(state_list) != daisy_chain:
        raise Exception("State list must contain {} sub lists.".format(daisy_chain))
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
    if len(data_list) != 8 * daisy_chain:
        raise Exception("Input list must contain {} integers.".format(8 * daisy_chain))
    for d in data_list:
        if d not in (0, 1):
            raise Exception("Input data must be in binary format.")
    GPIO.output(clock_pin, GPIO.LOW)
    GPIO.output(latch_pin, GPIO.LOW)
    # send serial data
    for d in data_list:
        GPIO.output(data_pin, d)  # write one bit to data pin
        GPIO.output(clock_pin, GPIO.LOW)  # pull clock pin LOW
        time.sleep(0.01)  # wait for 10 ms
        GPIO.output(clock_pin, GPIO.HIGH)  # pull clock pin HIGH to send rising edge
    # show data on output pins
    GPIO.output(latch_pin, GPIO.HIGH)  # pull latch pin HIGH
    time.sleep(0.01)  # wait for 10 ms
    GPIO.output(latch_pin, GPIO.LOW)  # pull latch pin LOW


# def writeMotors():
#     # list for storing current states of motor
#     current_state = [IDLE_STATE for _ in range(10)]
#     return


SampleStates = [
    [RELEASE, RELEASE, RELEASE],
    [FORWARD, RELEASE, RELEASE],
    [RELEASE, FORWARD, RELEASE],
    [RELEASE, RELEASE, FORWARD],
    [RELEASE, RELEASE, RELEASE],
    [BACKWARD, RELEASE, RELEASE],
    [RELEASE, BACKWARD, RELEASE],
    [RELEASE, RELEASE, BACKWARD],
    [RELEASE, RELEASE, RELEASE],
    [FORWARD, FORWARD, RELEASE],
    [RELEASE, FORWARD, FORWARD],
    [FORWARD, RELEASE, FORWARD],
    [RELEASE, RELEASE, RELEASE],
    [BACKWARD, BACKWARD, RELEASE],
    [RELEASE, BACKWARD, BACKWARD],
    [BACKWARD, RELEASE, BACKWARD],
    [RELEASE, RELEASE, RELEASE],
    [FORWARD, FORWARD, FORWARD],
    [RELEASE, RELEASE, RELEASE],
    [BACKWARD, BACKWARD, BACKWARD],
    [RELEASE, RELEASE, RELEASE],
]

ChainedSampleStates = [
    [FORWARD, FORWARD, FORWARD],
    [BACKWARD, BACKWARD, BACKWARD],
    [FORWARD, FORWARD, FORWARD],
    [BACKWARD, BACKWARD, BACKWARD],
    [FORWARD, FORWARD, FORWARD],
    [BACKWARD, BACKWARD, BACKWARD],
    [FORWARD, FORWARD, FORWARD],
    [BACKWARD, BACKWARD, BACKWARD],
    [FORWARD, FORWARD, FORWARD],
    [RELEASE, RELEASE, RELEASE],
]
