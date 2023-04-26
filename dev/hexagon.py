from math import sqrt, floor

# CONSTANTS
SQRT_3 = sqrt(3)


class Hexagon:
    def __init__(self, length, x, y, is_flat_top, coord, id):
        self.is_flat_top = is_flat_top
        self.id = id
        self.coord = coord
        self.set_drawing_points(length, x, y, is_flat_top)
        self.set_center_position(length, x, y, is_flat_top)

    def set_drawing_points(self, length, x, y, is_flat_top):
        if is_flat_top:
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

    def set_center_position(self, length, x, y, is_flat_top):
        if is_flat_top:
            self.position = (
                floor(x + length),
                floor(y + 0.5 * SQRT_3 * length),
            )
        else:
            self.position = (
                floor(x + 0.5 * SQRT_3 * length),
                floor(y + length),
            )

    def is_neighbor(self, other):
        if self.is_flat_top:
            diffs = [(0, 1), (-1, 0.5), (-1, -0.5), (0, -1), (1, -0.5), (1, 0.5)]
        else:
            diffs = [(0.5, 1), (-0.5, 1), (-1, 0), (-0.5, -1), (0.5, -1), (1, 0)]
        c1 = self.coord
        c2 = other.coord
        dx = c1[0] - c2[0]
        dy = c1[1] - c2[1]
        for diff in diffs:
            # use absolute difference for float comparison
            if abs(dx - diff[0]) < 0.1 and abs(dy - diff[1]) < 0.1:
                return True
        return False
