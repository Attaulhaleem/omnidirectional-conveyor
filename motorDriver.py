import RPi.GPIO as GPIO
import time
import motor

GPIO.setwarnings(False)  # remove pin usage warnings

motor.setup()

state_list = [
    motor.UP_RIGHT,
    motor.RIGHT,
    motor.DOWN_RIGHT,
    motor.DOWN_LEFT,
    motor.LEFT,
    motor.UP_LEFT,
    motor.UP_RIGHT,
    motor.RIGHT,
    motor.DOWN_RIGHT,
    motor.DOWN_LEFT,
]

data_list = motor.getChainedBinaryList(state_list)
motor.shiftOut(data_list)
time.sleep(100)

GPIO.cleanup()
