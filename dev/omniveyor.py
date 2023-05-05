from shift_register import ShiftRegister
from hexagon import SQRT_3, Hexagon
from queue import Queue
from module import *
import time


class Omniveyor:
    def __init__(self):
        self.create_hexagons(50, 3, 3, False, False, 10, 10)
        self.num_of_modules = len(self.hexagons)
        # workaround
        positions = [(0, 0) for _ in range(self.num_of_modules)]
        if len(positions) != self.num_of_modules:
            raise Exception(
                "Positions must contain data for {} modules!".format(
                    self.num_of_modules
                )
            )
        self.modules = [Module(positions[i]) for i in range(self.num_of_modules)]
        self.sr1 = ShiftRegister(11, 13, 15, 5)
        self.sr2 = ShiftRegister(3, 5, 7, 3)
        self.sr1.clear()
        self.sr2.clear()
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
        # self.update_module_actions()
        self.update_sr_data()
        self.sr1.shift_out(self.sr_data[0:40])
        self.sr2.shift_out(self.sr_data[40:64])

    def update_module_actions(self):
        for module in self.modules:
            # module is idle if not located under package
            if not module.is_below_package(self.bbox):
                module.set_action(ACTIONS["idle"])
            # get first movement
            try:
                movement = self.get_path_indexes()[0:2]
            except:
                continue
            start = movement[0]
            goal = movement[1]
            # get direction for movement
            dir = self.hexagons[start].get_direction(self.hexagons[goal])
            # continue if direction does not exist
            if dir is None:
                continue
            module.set_action(ACTIONS[dir])

    def create_hexagons(
        self, length, rows, cols, is_flat_top, is_odd_offset, startx, starty
    ):
        count = 0
        self.hexagons = []
        if is_flat_top:
            for col in range(cols):
                for row in range(rows):
                    is_offset = col % 2 == is_odd_offset
                    # continue if no hexagon due to offset
                    if not is_offset and row == 0 and rows > 1:
                        continue
                    # compute where to place hexagon
                    X = startx + col * 1.5 * length
                    Y = starty + row * SQRT_3 * length
                    Y += 0.5 * SQRT_3 * length if is_offset else 0
                    coord = (col, row if is_offset else row - 0.5)
                    # give a unique id to each hexagon
                    id = count if is_offset else count + rows - 2 * row
                    # increment total num of hexagons
                    count += 1
                    # create hexagon
                    self.hexagons.append(Hexagon(length, X, Y, is_flat_top, coord, id))
        else:
            for row in range(rows):
                for col in range(cols):
                    is_offset = row % 2 == is_odd_offset
                    # continue if no hexagon due to offset
                    if not is_offset and col == 0 and cols > 1:
                        continue
                    # compute where to place hexagon
                    X = startx + col * SQRT_3 * length
                    X += 0.5 * SQRT_3 * length if is_offset else 0
                    Y = starty + row * 1.5 * length
                    coord = (col if is_offset else col - 0.5, row)
                    # give a unique id to each hexagon
                    id = count if is_offset else count + cols - 2 * col
                    # increment total num of hexagons
                    count += 1
                    # create hexagon
                    self.hexagons.append(Hexagon(length, X, Y, is_flat_top, coord, id))
        self.hexagons.sort(key=lambda h: h.id)

    # returns all neighbors for a hexagon index
    def get_neighbors(self, index):
        neighbors = []
        for i in range(len(self.hexagons)):
            if self.hexagons[i].is_neighbor(self.hexagons[index]):
                neighbors.append(i)
        return neighbors

    def get_nearest_index(self, mouse_pos):
        if len(mouse_pos) != 2:
            raise Exception("Position must be a set of 2 integers!")
        min_dist = float("inf")
        for i, hexagon in enumerate(self.hexagons):
            dx = mouse_pos[0] - hexagon.position[0]
            dy = mouse_pos[1] - hexagon.position[1]
            dist = dx**2 + dy**2
            if dist < min_dist:
                min_dist = dist
                index = i
        return index

    def get_path_indexes(self, start, goal):
        frontier = Queue()
        frontier.put(start)
        came_from = dict()
        # path A->B stored as came_from[B] == A
        came_from[start] = None
        while not frontier.empty():
            current = frontier.get()
            if current == goal:
                break
            for next in self.get_neighbors(current):
                if next not in came_from:
                    frontier.put(next)
                    came_from[next] = current
        current = goal
        path = list()
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        return path


if __name__ == "__main__":
    omni = Omniveyor()
    for i in range(omni.num_of_modules):
        omni.modules[i].set_action(ACTIONS["clockwise"])
        print(omni.modules[i].sr_byte)
    omni.actuate()
    time.sleep(60)
