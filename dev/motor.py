# valid motor states
STATES = {"forward": (1, 0), "backward": (0, 1), "release": (0, 0)}


class Motor:
    """A motor in the Omniveyor. Manages the motor pins, state, and its position on the pi camera."""

    def __init__(self, pins, position, state=STATES["release"]):
        """Initialize a motor.

        Args:
            pins (tuple[int, int]): (forward_pin, backward_pin) on Shift Register output.
            position (tuple[int, int]): (x, y) position in pi camera frame.
            state (tuple[int, int], optional): Any state in STATES. Defaults to STATES["release"].
        """
        self.pins = pins
        self.position = position
        self.set_state(state)

    def __str__(self):
        """Get a description of the Motor object and its associated properties.

        Returns:
            str: A string containing the Motor object properties.
        """
        return "Motor [pins: {}, position: {}, state: {}]".format(
            self.pins, self.position, self.state
        )

    def set_state(self, state):
        """Set any Motor state.

        Args:
            state (tuple[int, int]): Any state in STATES.

        Raises:
            Exception: State is not in STATES.
        """
        if state not in STATES.values():
            raise Exception("Invalid motor state!")
        self.state = state
