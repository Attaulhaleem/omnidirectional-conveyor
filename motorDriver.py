import RPi.GPIO as GPIO
import time
import motor

motor.setup()

data_list = motor.getChainedBinaryList([motor.CLOCKWISE for _ in range(4)])
motor.shiftOut(data_list)

try:
    time.sleep(1)
except KeyboardInterrupt:
    print("Manually exiting program!")
    GPIO.cleanup()
    raise SystemExit
