from math import sqrt, floor

# CONSTANTS
SQRT_3 = sqrt(3)

# accessible variables
FLAT_TOP = None
ODD_OFFSET = None
coordinates = list()
positions = list()
path = list()
count = 0

# returns points for drawing hexagon, populates positions and coordinates
def generate(length: int, rows: int, cols: int, flat_top: bool, odd_offset: bool):
    global coordinates, positions, FLAT_TOP, ODD_OFFSET
    coordinates.clear()
    positions.clear()
    FLAT_TOP = flat_top
    ODD_OFFSET = odd_offset
    L = length
    drawingPoints = list()
    for row in range(rows):
        for col in range(cols):
            if flat_top:
                if not col % 2 == odd_offset and row == 0 and rows > 1:
                    continue
                X = col * 1.5 * L
                Y = row * SQRT_3 * L
                Y += 0.5 * SQRT_3 * L if col % 2 == odd_offset else 0
                drawingPoints.append(
                    [
                        (X, Y + 0.5 * SQRT_3 * L),
                        (X + 0.5 * L, Y),
                        (X + 1.5 * L, Y),
                        (X + 2 * L, Y + 0.5 * SQRT_3 * L),
                        (X + 1.5 * L, Y + SQRT_3 * L),
                        (X + 0.5 * L, Y + SQRT_3 * L),
                    ]
                )
                coordinates.append((col, row if col % 2 == odd_offset else row - 0.5))
                positions.append((floor(X + L), floor(Y + 0.5 * SQRT_3 * L)))
                count += 1
            else:
                if not row % 2 == odd_offset and col == 0 and cols > 1:
                    continue
                X = col * SQRT_3 * L
                X += 0.5 * SQRT_3 * L if row % 2 == odd_offset else 0
                Y = row * 1.5 * L
                drawingPoints.append(
                    [
                        (X + 0.5 * SQRT_3 * L, Y),
                        (X, Y + 0.5 * L),
                        (X, Y + 1.5 * L),
                        (X + 0.5 * SQRT_3 * L, Y + 2 * L),
                        (X + SQRT_3 * L, Y + 1.5 * L),
                        (X + SQRT_3 * L, Y + 0.5 * L),
                    ]
                )
                coordinates.append((col if row % 2 == odd_offset else col - 0.5, row))
                positions.append((floor(X + 0.5 * SQRT_3 * L), floor(Y + L)))
                count += 1
    return drawingPoints


# find index of hexagon nearest to cursor
def findNearestIndex(mouse_pos):
    if len(mouse_pos) != 2:
        raise Exception("Mouse position must be a set of 2 integers.")
    for pos in positions:
        if len(pos) != 2:
            raise Exception("List must contain sets of 2 integers only.")
    dists = list()
    for pos in positions:
        dx = mouse_pos[0] - pos[0]
        dy = mouse_pos[1] - pos[1]
        dists.append(dx**2 + dy**2)
    return dists.index(min(dists))


# returns True if two hexagons are neighbors
def areNeighbors(index_1, index_2):
    if FLAT_TOP:
        diffs = [(0, 1), (-1, 0.5), (-1, -0.5), (0, -1), (1, -0.5), (1, 0.5)]
    else:
        diffs = [(0.5, 1), (-0.5, 1), (-1, 0), (-0.5, -1), (0.5, -1), (1, 0)]
    c1 = coordinates[index_1]
    c2 = coordinates[index_2]
    diff = (c1[0] - c2[0], c1[1] - c2[1])
    if diff in diffs:
        return True
    else:
        return False
