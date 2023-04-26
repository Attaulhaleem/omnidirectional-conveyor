# from shiftregister import ShiftRegister
from module import *


class Omniveyor:
    """A configurable conveyor consisting of multiple modules."""

    def __init__(self, num_of_modules, positions):
        """Initialize an Omniveyor.

        Args:
            num_of_modules (integer): Number of concatenated modules in the conveyor.
            positions (list[tuple(int, int)]): Module center positions in pi camera frame.

        Raises:
            Exception: Length of error does not match number of modules.
        """
        self.num_of_modules = num_of_modules
        if len(positions) != num_of_modules:
            raise Exception(
                "Positions must contain data for {} modules!".format(num_of_modules)
            )
        self.modules = [Module(positions[i]) for i in range(num_of_modules)]
        # self.sr = ShiftRegister(11, 13, 15, num_of_modules)
        # self.sr.clear()


omni = Omniveyor(10, [(0, 0) for _ in range(10)])
print(omni)
