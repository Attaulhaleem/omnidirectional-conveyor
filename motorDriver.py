import RPi.GPIO as GPIO
import time
import motor

GPIO.setwarnings(False)  # remove pin usage warnings
motor.setup()

daisy_chain = 5
state_list = [[motor.FORWARD, motor.FORWARD, motor.FORWARD] for i in range(daisy_chain)]
data_list = motor.getChainedBinaryList(daisy_chain, state_list)
motor.shiftOut(daisy_chain, data_list)
time.sleep(100)

GPIO.cleanup()
