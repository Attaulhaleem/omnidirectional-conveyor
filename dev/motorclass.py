import RPi.GPIO as GPIO
import time


class Motor:
    FORWARD = (1, 0)
    BACKWARD = (0, 1)
    RELEASE = (0, 0)

    def __init__(self, position):
        self.state = self.RELEASE
        self.position = position  # position on picam

    def set_state(self, state):
        if state not in (self.FORWARD, self.BACKWARD, self.RELEASE):
            raise Exception("Invalid motor state!")
        self.state = state


class Module:
    IDLE = [Motor.RELEASE, Motor.RELEASE, Motor.RELEASE, Motor.RELEASE]
    UP_RIGHT = [Motor.RELEASE, Motor.FORWARD, Motor.BACKWARD, Motor.RELEASE]
    RIGHT = [Motor.FORWARD, Motor.RELEASE, Motor.BACKWARD, Motor.RELEASE]
    DOWN_RIGHT = [Motor.FORWARD, Motor.BACKWARD, Motor.RELEASE, Motor.RELEASE]
    DOWN_LEFT = [Motor.RELEASE, Motor.BACKWARD, Motor.FORWARD, Motor.RELEASE]
    LEFT = [Motor.BACKWARD, Motor.RELEASE, Motor.FORWARD, Motor.RELEASE]
    UP_LEFT = [Motor.BACKWARD, Motor.FORWARD, Motor.RELEASE, Motor.RELEASE]
    CLOCKWISE = [Motor.FORWARD, Motor.FORWARD, Motor.FORWARD, Motor.RELEASE]
    ANTI_CLOCKWISE = [Motor.BACKWARD, Motor.BACKWARD, Motor.BACKWARD, Motor.RELEASE]

    def __init__(
        self,
        motor_positions,
    ):
        if len(motor_positions) != 3:
            raise Exception("Each module must have 3 motor positions!")
        self.motors = (Motor(motor_positions[i]) for i in range(3))
        self.action = self.IDLE

    def set_state(self, action):
        self.action = action

    def __get_underlying_motors(self, bounding_box):
        """Get module motors which are currently under the package"""
        pass

    def get_binary_list(state_list):
        """Format data for writing byte to shift register"""
        print(state_list)
        if len(state_list) != 4:
            raise Exception("Input list must contain 4 motor states.")
        for state in state_list:
            if state not in (Motor.FORWARD, Motor.BACKWARD, Motor.RELEASE):
                raise Exception("Invalid motor state in input list.")
        # convert to flat list
        motor_values = [val for state in state_list for val in state]
        # see shield schematic [M3 and M4 were replaced on my shield] (http://wiki.sunfounder.cc/images/f/ff/L293D_schematic.png)
        # output format [3A, 4B, 3B, 2B, 1B, 1A, 2A, 4A]
        shield_config = (4, 7, 5, 3, 1, 0, 2, 6)
        return [motor_values[i] for i in shield_config]


class Omniveyor:
    def __init__(self, data_pin, clock_pin, latch_pin, modules):
        self.data_pin = data_pin
        self.clock_pin = clock_pin
        self.latch_pin = latch_pin
        self.modules = modules
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup((latch_pin, data_pin, clock_pin), GPIO.OUT)
        GPIO.output((latch_pin, data_pin, clock_pin), GPIO.LOW)

    def pulse(pin, delay=0.001):
        GPIO.output(pin, GPIO.LOW)
        time.sleep(delay)
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(delay)

    def getChainedBinaryList(state_list):
        """Format data for writing multiple bytes to daisy-chained shift registers"""
        motor_values = list()
        for sub_list in state_list:
            motor_values.append(Module.getSingleBinaryList(sub_list))
        # first motor values must be sent last
        motor_values.reverse()
        # convert to flat list
        motor_values = [val for sub_list in motor_values for val in sub_list]
        return motor_values

    def shiftOut(self, data_list):
        """Writes data to shift register(s)"""
        for d in data_list:
            if d not in (0, 1):
                raise Exception("Input data must be in binary format.")
        # send serial data
        for d in data_list:
            GPIO.output(self.data_pin, d)  # write one bit to data pin
            self.pulse(self.clock_pin)
        # show data on output
        self.pulse(self.latch_pin)

    def clear(self):
        self.shiftOut([0 for _ in range(self.modules * 8)])

    SampleStates = [
        Module.CLOCKWISE,
        Module.ANTI_CLOCKWISE,
        Module.UP_RIGHT,
        Module.RIGHT,
        Module.DOWN_RIGHT,
        Module.DOWN_LEFT,
        Module.LEFT,
        Module.UP_LEFT,
        Module.IDLE,
    ]


omniveyor = Omniveyor(11, 13, 15, 10)
data_list = omniveyor.getChainedBinaryList([Module.CLOCKWISE for _ in range(4)])
omniveyor.shiftOut(data_list)
