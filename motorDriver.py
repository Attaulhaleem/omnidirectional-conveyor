import RPi.GPIO as GPIO
import time
import motor

GPIO.setwarnings(False)  # remove pin usage warnings
GPIO.setmode(GPIO.BOARD)  # use board pin numberings

# shift register pins
latchPin = 11
dataPin = 13
clockPin = 15

# pin declarations
GPIO.setup(latchPin, GPIO.OUT)
GPIO.setup(dataPin, GPIO.OUT)
GPIO.setup(clockPin, GPIO.OUT)

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


for state in motor.SampleStates:
    motorData = motor.getBinaryList(state)
    print(state)
    print(motorData)
    shiftOut(motorData)
    time.sleep(10)
