from motor import *

ACTIONS = {
    "idle": (STATES["release"], STATES["release"], STATES["release"]),
    "up_right": (STATES["release"], STATES["forward"], STATES["backward"]),
    "right": (STATES["forward"], STATES["release"], STATES["backward"]),
    "down_right": (STATES["forward"], STATES["backward"], STATES["release"]),
    "down_left": (STATES["release"], STATES["backward"], STATES["forward"]),
    "left": (STATES["backward"], STATES["release"], STATES["forward"]),
    "up_left": (STATES["backward"], STATES["forward"], STATES["release"]),
    "clockwise": (STATES["forward"], STATES["forward"], STATES["forward"]),
    "anti_clockwise": (STATES["backward"], STATES["backward"], STATES["backward"]),
}


class Module:
    """A module of the OmniVeyor. Manages the 3 motors in the module."""

    # see shield schematic [M3 and M4 were replaced on my shield] (http://wiki.sunfounder.cc/images/f/ff/L293D_schematic.png)
    # output format [3A, 4B, 3B, 2B, 1B, 1A, 2A, 4A]
    PIN_CONFIG = ((5, 4), (6, 3), (0, 2))  # motor pins on shift register output

    def __init__(self, position, action=ACTIONS["idle"]):
        """Initialize a module (containing 3 motors).
        position: module center position in pi camera frame
        action: any action from ACTIONS"""
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
        action: any action in ACTIONS"""
        if action not in ACTIONS.values():
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


mod = Module((0, 0), ACTIONS["anti_clockwise"])
print(mod.sr_data)
mod.set_action(ACTIONS["clockwise"])
print(mod.sr_data)
