# valid motor states
STATES = {"forward": (1, 0), "backward": (0, 1), "release": (0, 0)}


class Motor:
    """Class for defining a motor on the OmniVeyor.
    Manages the motor pins, state, and position on the pi camera."""

    def __init__(self, pins, position, state=STATES["release"]):
        """Initialize a motor.
        pins: (forward_pin, backward_pin) on shift register
        position: (x, y) position in pi camera frame
        state: any state from STATES"""
        self.pins = pins
        self.position = position
        self.set_state(state)

    def __str__(self):
        """Return motor properties as a string."""
        return "Motor [pins: {}, position: {}, state: {}]".format(
            self.pins, self.position, self.state
        )

    def set_state(self, state):
        """Set motor state.
        state: any state from STATES"""
        if state not in STATES.values():
            raise Exception("Invalid motor state!")
        self.state = state
