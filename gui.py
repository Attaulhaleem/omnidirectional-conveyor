from guizero import App, Box, ButtonGroup, Drawing, PushButton, Slider, Text, error
import hexagon

""" CALLBACK FUNCTIONS """

# called when button pressed, draw hexagons on screen
def drawHexagons():
    drawingPoints = hexagon.generate(50, 3, 4, False, True)
    for i in range(len(drawingPoints)):
        hex_drawing.polygon(drawingPoints[i], color=HEX_COLOR, outline=True)
        hex_drawing.text(
            hexagon.positions[i][0],
            hexagon.positions[i][1],
            text=str(i),
            font=HEADING_FONT,
        )
    print(hexagon.coordinates)
    print(hexagon.positions)


def drawPath():
    global line_ids
    if src_slider.value == dest_slider.value:
        error(title="Error", text="Source and destination cannot be the same!")
        return
    else:
        path = hexagon.getPathIndexes(src_slider.value, dest_slider.value)
        path_text.value = "->".join(map(str, path))
        if line_ids:
            for id in line_ids:
                hex_drawing.delete(id)
            line_ids.clear()
        for i in range(len(path) - 1):
            id = hex_drawing.line(
                hexagon.positions[path[i]][0],
                hexagon.positions[path[i]][1],
                hexagon.positions[path[i + 1]][0],
                hexagon.positions[path[i + 1]][1],
                width=3,
            )
            line_ids.append(id)


""" APP """

# fonts
HEADING_FONT = "Inter Medium"
BODY_FONT = "Inter Regular"

# colors
BG_COLOR = (250, 249, 246)
HEX_COLOR = (29, 109, 134)

# app elements
app = App(title="Omniveyor", bg=BG_COLOR, layout="grid")
app.tk.state("zoomed")  # maximize window
image_box = Box(app, width=450, height=275, border=True, grid=[0, 0])
path_box = Box(app, width=450, height=200, border=True, layout="grid", grid=[0, 1])
path_text = Text(path_box, font=BODY_FONT, grid=[0, 3])

# hexagon structure
hex_drawing = Drawing(image_box, width="fill", height="fill")
line_ids = list()
drawHexagons()

# sliders
Text(path_box, text="Source", font=HEADING_FONT, grid=[0, 0], align="left")
src_slider = Slider(path_box, start=0, end=hexagon.count - 1, grid=[1, 0], align="left")

Text(path_box, text="Destination", font=HEADING_FONT, grid=[0, 1], align="left")
dest_slider = Slider(
    path_box, start=0, end=hexagon.count - 1, grid=[1, 1], align="left"
)

# button for drawing box
start_button = PushButton(
    path_box, command=drawPath, text="Draw Path", grid=[0, 2], align="top"
)
start_button.font = HEADING_FONT


app.display()
