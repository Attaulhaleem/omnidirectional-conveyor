import RPi.GPIO as GPIO
import time
import motor

motor.setup()

data_list = motor.getChainedBinaryList(motor.SampleStates)
motor.shiftOut(data_list)
time.sleep(100)

GPIO.cleanup()
