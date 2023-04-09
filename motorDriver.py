import RPi.GPIO as GPIO
import time
import motor

GPIO.setwarnings(False)  # remove pin usage warnings

motor.setup()

# motor.shiftOut([0, 0, 0, 0, 0, 0, 0, 1])
# time.sleep(1000)

# run motor test
for state in motor.SampleStates:
    motorData = motor.getBinaryList(state)
    motor.shiftOut(motorData)
    time.sleep(5)  # wait for 5s

GPIO.cleanup()
