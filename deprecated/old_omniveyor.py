# from shift_register import ShiftRegister
from module import *
from hex_grid import HexGrid

# TODO: merge HexGrid into Omniveyor


class Omniveyor:
    def __init__(self):
        positions = [(0, 0) for _ in range(10)]
        self.hex_grid = HexGrid(50, 3, 4, False, True, 10, 10)
        self.num_of_modules = len(self.hex_grid.hexagons)
        if len(positions) != self.num_of_modules:
            raise Exception(
                "Positions must contain data for {} modules!".format(
                    self.num_of_modules
                )
            )
        self.modules = [Module(positions[i]) for i in range(self.num_of_modules)]
        # self.sr = ShiftRegister(11, 13, 15, self.num_of_modules)
        # self.sr.clear()
        # !!! implement this function to get box location and size
        # self.bbox = get_bounding_box()
        # workaround
        self.bbox = (0, 0)

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
        self.update_module_actions()
        self.update_sr_data()
        # self.sr.shift_out(self.sr_data)

    def update_module_actions(self):
        for module in self.modules:
            # module is idle if not located under package
            if not module.is_below_package(self.bbox):
                module.set_action(ACTIONS["idle"])
            # get first movement
            try:
                movement = self.hex_grid.get_path_indexes()[0:2]
            except:
                continue
            start = movement[0]
            goal = movement[1]
            # get direction for movement
            dir = self.hex_grid.hexagons[start].get_direction(
                self.hex_grid.hexagons[goal]
            )
            # continue if direction does not exist
            if dir is None:
                continue
            module.set_action(ACTIONS[dir])
