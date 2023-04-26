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

    def update_sr_data(self):
        """Chain the individual module bytes to be written to shift register(s)."""
        chained_data = list()
        for module in self.modules:
            chained_data.append(module.sr_byte)
        # first motor data must be sent last
        chained_data.reverse()
        # flatten list
        chained_data = [bit for byte in chained_data for bit in byte]
        self.sr_data = chained_data

    def actuate(self):
        """Actuate the Omniveyor motors according to their assigned states."""
        self.update_sr_data()
        # self.sr.shift_out(self.sr_data)


omni = Omniveyor(10, [(0, 0) for _ in range(10)])
omni.actuate()
print(omni)
