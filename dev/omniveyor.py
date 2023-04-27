# from shiftregister import ShiftRegister
from module import *
from hexgrid import HexGrid


class Omniveyor:
    """A configurable conveyor consisting of multiple modules."""

    def __init__(self):
        """Initialize an Omniveyor.

        Args:
            positions (list[tuple(int, int)]): Module center positions in pi camera frame.

        Raises:
            Exception: Length of error does not match number of modules.
        """
        positions = [(0, 0) for _ in range(10)]
        self.grid = HexGrid(50, 3, 4, False, True, 10, 10)
        self.num_of_modules = len(self.grid.hexagons)
        if len(positions) != self.num_of_modules:
            raise Exception(
                "Positions must contain data for {} modules!".format(
                    self.num_of_modules
                )
            )
        self.modules = [Module(positions[i]) for i in range(self.num_of_modules)]
        # self.sr = ShiftRegister(11, 13, 15, self.num_of_modules)
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

    def set_module_states(self):
        for module in self.modules:
            # continue if module is not located under package
            if module.get_underlying_motors() is None:
                continue
            # find the next action of the module
            # next_action = self.grid.get_path_indexes()[:]


omni = Omniveyor()
omni.actuate()
print(omni)
