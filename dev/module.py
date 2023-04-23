from motor import *

# ACTIONS = {
#     "idle": (RELEASE, RELEASE, RELEASE),
#     "up_right": (RELEASE, FORWARD, BACKWARD),
#     "right": (FORWARD, RELEASE, BACKWARD),
#     "down_right": (FORWARD, BACKWARD, RELEASE),
#     "down_left": (RELEASE, BACKWARD, FORWARD),
#     "left": (BACKWARD, RELEASE, FORWARD),
#     "up_left": (BACKWARD, FORWARD, RELEASE),
#     "clockwise": (FORWARD, FORWARD, FORWARD),
#     "anti_clockwise": (BACKWARD, BACKWARD, BACKWARD),
# }

IDLE = (RELEASE, RELEASE, RELEASE)
UP_RIGHT = (RELEASE, FORWARD, BACKWARD)
RIGHT = (FORWARD, RELEASE, BACKWARD)
DOWN_RIGHT = (FORWARD, BACKWARD, RELEASE)
DOWN_LEFT = (RELEASE, BACKWARD, FORWARD)
LEFT = (BACKWARD, RELEASE, FORWARD)
UP_LEFT = (BACKWARD, FORWARD, RELEASE)
CLOCKWISE = (FORWARD, FORWARD, FORWARD)
ANTI_CLOCKWISE = (BACKWARD, BACKWARD, BACKWARD)

VALID_ACTIONS = (
    IDLE,
    UP_RIGHT,
    RIGHT,
    DOWN_RIGHT,
    DOWN_LEFT,
    LEFT,
    UP_LEFT,
    CLOCKWISE,
    ANTI_CLOCKWISE,
)


class Module:
    """A module of the OmniVeyor. Manages the 3 motors in the module."""

    # see shield schematic [M3 and M4 were replaced on my shield] (http://wiki.sunfounder.cc/images/f/ff/L293D_schematic.png)
    # output format [3A, 4B, 3B, 2B, 1B, 1A, 2A, 4A]
    PIN_CONFIG = ((5, 4), (6, 3), (0, 2))  # motor pins on shift register output

    def __init__(self, position, action=IDLE):
        """Initialize a module (containing 3 motors).
        position: module center position in pi camera frame
        action: any action from VALID_ACTIONS"""
        self.position = position
        self.motors = [
            Motor(self.PIN_CONFIG[i], self.get_motor_positions(position)[i])
            for i in range(3)
        ]
        self.set_action(action)

    def get_motor_positions(self, position):
        """Find the 3 motor positions from the module position.
        position: module center position in pi camera frame"""
        return ((0, 0), (0, 0), (0, 0))

    def set_action(self, action):
        """Set module action (and corresponding motor states).
        action: tuple of three motor states"""
        if action not in VALID_ACTIONS:
            raise Exception("Invalid module action!")
        for i, motor in enumerate(self.motors):
            motor.set_state(action[i])
        # set action before encoding data for SR
        self.action = action
        self.encode_sr_data()

    def encode_sr_data(self):
        """Encode the current module action as data for writing to shift register."""
        # initialize empty byte
        data_list = [0 for _ in range(8)]
        for motor in self.motors:
            for i in range(2):
                data_list[motor.pins[i]] = motor.state[i]
        self.sr_data = data_list

    def get_underlying_motors(self, bounding_box):
        """Get module motors which are currently under the package"""
        pass


mod = Module((0, 0), ANTI_CLOCKWISE)
print(mod.sr_data)
mod.set_action(CLOCKWISE)
print(mod.sr_data)
