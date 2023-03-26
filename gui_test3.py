from guizero import App, Drawing
from math import sqrt

app = App(title="Test")

drawing = Drawing(app, width="fill", height="fill")

L = 40
ROWS = 4
COLS = 5
CONFIG = "POINTY_TOP"

for col in range(COLS):
    for row in range(ROWS):
        if CONFIG == "FLAT_TOP" and COLS > 1 and row == 0 and not col % 2:
            continue
        if CONFIG == "POINTY_TOP" and ROWS > 1 and col == 0 and not row % 2:
            continue
        offsetX = 3 / 2 * L if CONFIG == "POINTY_TOP" and row % 2 else 0
        offsetY = sqrt(3) / 2 * L if CONFIG == "FLAT_TOP" and col % 2 else 0
        X = col * 3 / 2 * L + offsetX
        Y = row * sqrt(3) * L + offsetY
        hexagon = drawing.polygon(
            [
                [X, Y + sqrt(3) / 2 * L],
                [X + L / 2, Y],
                [X + 3 / 2 * L, Y],
                [X + 2 * L, Y + sqrt(3) / 2 * L],
                [X + 3 / 2 * L, Y + sqrt(3) * L],
                [X + L / 2, Y + sqrt(3) * L],
            ],
            color="orange",
            outline=True,
            outline_color="black",
        )

app.display()
