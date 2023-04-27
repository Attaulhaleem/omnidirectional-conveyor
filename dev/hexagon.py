from math import sqrt, floor

# CONSTANTS
SQRT_3 = sqrt(3)


class Hexagon:
    def __init__(self, length, x, y, is_flat_top, coord, id):
        self.is_flat_top = is_flat_top
        self.id = id
        self.coord = coord
        self.set_diffs()
        self.set_drawing_points(length, x, y)
        self.set_center_position(length, x, y)

    def set_diffs(self):
        if self.is_flat_top:
            self.diffs = {
                "up_right": (1, -0.5),
                "down_right": (1, 0.5),
                "down": (0, 1),
                "down_left": (-1, 0.5),
                "up_left": (-1, -0.5),
                "up": (0, -1),
            }
        else:
            self.diffs = {
                "up_right": (0.5, -1),
                "right": (1, 0),
                "down_right": (0.5, 1),
                "down_left": (-0.5, 1),
                "left": (-1, 0),
                "up_left": (-0.5, -1),
            }

    def set_drawing_points(self, length, x, y):
        if self.is_flat_top:
            self.points = [
                (x, y + 0.5 * SQRT_3 * length),
                (x + 0.5 * length, y),
                (x + 1.5 * length, y),
                (x + 2 * length, y + 0.5 * SQRT_3 * length),
                (x + 1.5 * length, y + SQRT_3 * length),
                (x + 0.5 * length, y + SQRT_3 * length),
            ]
        else:
            self.points = [
                (x + 0.5 * SQRT_3 * length, y),
                (x, y + 0.5 * length),
                (x, y + 1.5 * length),
                (x + 0.5 * SQRT_3 * length, y + 2 * length),
                (x + SQRT_3 * length, y + 1.5 * length),
                (x + SQRT_3 * length, y + 0.5 * length),
            ]

    def set_center_position(self, length, x, y):
        if self.is_flat_top:
            self.position = (
                floor(x + length),
                floor(y + 0.5 * SQRT_3 * length),
            )
        else:
            self.position = (
                floor(x + 0.5 * SQRT_3 * length),
                floor(y + length),
            )

    def get_direction(self, goal):
        c2 = goal.coord
        c1 = self.coord
        dx = c2[0] - c1[0]
        dy = c2[1] - c1[1]
        for key, diff in self.diffs.items():
            # use absolute difference for float comparison
            if abs(dx - diff[0]) < 0.1 and abs(dy - diff[1]) < 0.1:
                return key
        return None

    def is_neighbor(self, other):
        if self.get_direction(other) is None:
            return False
        else:
            return True
