from hexagon import SQRT_3, Hexagon
from queue import Queue


class HexGrid:
    def __init__(self, length, rows, cols, startx, starty, is_flat_top, is_odd_offset):
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
                    id = count if not is_offset else count + rows - 1 - 2 * row
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
                    id = count if not is_offset else count + cols - 1 - 2 * col
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
        came_from = dict()  # path A->B stored as came_from[B] == A
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
