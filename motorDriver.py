import RPi.GPIO as GPIO
import time
import motor

motor.setup()

data_list = motor.getChainedBinaryList([motor.CLOCKWISE for _ in range(4)])
motor.shiftOut(data_list)
time.sleep(100)

GPIO.cleanup()
