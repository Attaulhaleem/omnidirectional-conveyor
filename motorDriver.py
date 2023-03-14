import RPi.GPIO as GPIO
import time
import motor

GPIO.setwarnings(False)  # remove pin usage warnings

motor.setup()

# run motor test
for state in motor.SampleStates:
    motorData = motor.getBinaryList(state)
    motor.shiftOut(motorData)
    time.sleep(5)  # wait for 5s

GPIO.cleanup()