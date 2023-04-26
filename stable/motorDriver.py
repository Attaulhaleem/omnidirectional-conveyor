import RPi.GPIO as GPIO
import time
import motorshield

motorshield.setup()

data_list = motorshield.getChainedBinaryList([motorshield.CLOCKWISE for _ in range(4)])
motorshield.shiftOut(data_list)

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("Manually exiting program!")
        motorshield.clear()
        GPIO.cleanup()
        raise SystemExit
