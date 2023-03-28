from guizero import App, Box, ButtonGroup, Drawing, PushButton, Slider, Text
from math import sqrt, floor

SQRT_3 = sqrt(3)
HEADING_FONT = "Inter Medium"
BODY_FONT = "Inter Regular"

app = App(title="Omniveyor", bg=(250, 249, 246))
app.tk.state("zoomed")
sliders_box = Box(app, width="fill", align="top")
config_box = Box(app, width="fill", align="top", border=True)
image_box = Box(app, width="fill", height="fill", align="bottom")
drawing = Drawing(image_box, width="fill", height="fill")

hPos = []
hInd = []


def drawHexagons():
    drawing.clear()
    L = lengthSlider.value
    ROWS = rowSlider.value
    COLS = columnSlider.value
    FLAT_TOP = True if config.value == "F" else False
    ODD_OFFSET = True if offset.value == "O" else False
    FILL_COLOR = (redSlider.value, greenSlider.value, blueSlider.value)
    for row in range(ROWS):
        for col in range(COLS):
            if FLAT_TOP:
                if not col % 2 == ODD_OFFSET and row == 0 and ROWS > 1:
                    continue
                X = col * 1.5 * L
                Y = row * SQRT_3 * L
                Y += 0.5 * SQRT_3 * L if col % 2 == ODD_OFFSET else 0
                coordinates = [
                    (X, Y + 0.5 * SQRT_3 * L),
                    (X + 0.5 * L, Y),
                    (X + 1.5 * L, Y),
                    (X + 2 * L, Y + 0.5 * SQRT_3 * L),
                    (X + 1.5 * L, Y + SQRT_3 * L),
                    (X + 0.5 * L, Y + SQRT_3 * L),
                ]
                hInd.append([col, row if col % 2 == ODD_OFFSET else row - 0.5])
                hPos.append([floor(X + L), floor(Y + 0.5 * SQRT_3 * L)])
            else:
                if not row % 2 == ODD_OFFSET and col == 0 and COLS > 1:
                    continue
                X = col * SQRT_3 * L
                X += 0.5 * SQRT_3 * L if row % 2 == ODD_OFFSET else 0
                Y = row * 1.5 * L
                coordinates = [
                    (X + 0.5 * SQRT_3 * L, Y),
                    (X, Y + 0.5 * L),
                    (X, Y + 1.5 * L),
                    (X + 0.5 * SQRT_3 * L, Y + 2 * L),
                    (X + SQRT_3 * L, Y + 1.5 * L),
                    (X + SQRT_3 * L, Y + 0.5 * L),
                ]
                hInd.append([col if row % 2 == ODD_OFFSET else col - 0.5, row])
                hPos.append([floor(X + 0.5 * SQRT_3 * L), floor(Y + 0.5 * SQRT_3 * L)])

            drawing.polygon(
                coordinates,
                color=FILL_COLOR,
                outline=True,
                outline_color="black",
            )
    print(hInd)
    print(hPos)


def tracePath(event_data):
    print("mouse position =", event_data.x, event_data.y)


Text(sliders_box, text="Size", font=HEADING_FONT, align="left")
lengthSlider = Slider(sliders_box, start=20, end=50, align="left")
Text(sliders_box, text="Rows", font=HEADING_FONT, align="left")
rowSlider = Slider(sliders_box, start=1, end=20, align="left")
Text(sliders_box, text="Cols", font=HEADING_FONT, align="left")
columnSlider = Slider(sliders_box, start=1, end=20, align="left")

blueSlider = Slider(sliders_box, start=0, end=255, align="right")
Text(sliders_box, text="Blue", font=HEADING_FONT, color="blue", align="right")
greenSlider = Slider(sliders_box, start=0, end=255, align="right")
Text(sliders_box, text="Green", font=HEADING_FONT, color="green", align="right")
redSlider = Slider(sliders_box, start=0, end=255, align="right")
Text(sliders_box, text="Red", font=HEADING_FONT, color="red", align="right")
redSlider.value, greenSlider.value, blueSlider.value = (29, 109, 134)
lengthSlider.value = 50
rowSlider.value, columnSlider.value = 3, 4

Text(config_box, text="Orientation", font=HEADING_FONT, align="left")
config = ButtonGroup(
    config_box,
    options=[["Flat Top", "F"], ["Pointy Top", "P"]],
    selected="P",
    horizontal=True,
    align="left",
)
config.font = BODY_FONT


offset = ButtonGroup(
    config_box,
    options=[["Even", "E"], ["Odd", "O"]],
    selected="O",
    horizontal=True,
    align="right",
)
offset.font = BODY_FONT
Text(config_box, text="Offset", font=HEADING_FONT, align="right")

start = PushButton(config_box, command=drawHexagons, text="Generate")
start.font = BODY_FONT


drawing.when_left_button_pressed = tracePath

app.display()
