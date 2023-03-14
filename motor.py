import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  # use board pin numberings

# shift register pins
latchPin = 11
dataPin = 13
clockPin = 15

# motor states
FORWARD = (1, 0)
BACKWARD = (0, 1)
RELEASE = (0, 0)

def setup():
    # pin declarations
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)


# format data for writing to shift register
# returns [3B, 4B, 3A, 2B, 1B, 1A, 2A, 4A]  (!) testing needed
def getBinaryList(stateList: list[tuple[int]]):
    if len(stateList) != 3:
        raise Exception("Input list must contain 3 motor states.")
    stateList.append(RELEASE)  # fourth motor is not used
    for state in stateList:
        if state not in (FORWARD, BACKWARD, RELEASE):
            raise Exception("Invalid motor state in input list.")
    motorValues = [val for state in stateList for val in state]  # convert to flat list
    # see shield schematic [M3 and M4 were replaced on my shield] (http://wiki.sunfounder.cc/images/f/ff/L293D_schematic.png)
    shieldConfig = (5, 7, 4, 3, 1, 0, 2, 6)
    return [motorValues[i] for i in shieldConfig]


# write data to shift register
def shiftOut(dataList: list[int]):
    if len(dataList) != 8:
        raise Exception("Input list must contain 8 integers.")
    for d in dataList:
        if d not in (0, 1):
            raise Exception("Input data must be in binary format.")
    GPIO.output(clockPin, GPIO.LOW)
    GPIO.output(latchPin, GPIO.LOW)
    # send serial data
    for d in dataList:
        GPIO.output(dataPin, d)  # write one bit to data pin
        GPIO.output(clockPin, GPIO.LOW)  # pull clock pin LOW
        time.sleep(0.1)  # wait for 100 ms
        GPIO.output(clockPin, GPIO.HIGH)  # pull clock pin HIGH to send rising edge
    # show data on output pins
    GPIO.output(latchPin, GPIO.HIGH)  # pull latch pin HIGH
    time.sleep(0.1)  # wait for 100 ms
    GPIO.output(latchPin, GPIO.LOW)  # pull latch pin LOW


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