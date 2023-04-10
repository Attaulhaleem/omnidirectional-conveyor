from guizero import App, Box, Drawing, PushButton, Slider, Text, error
import hexagon

""" CALLBACK FUNCTIONS """

# called when button pressed, draw hexagons on screen
def drawHexagons():
    drawingPoints = hexagon.generate(50, 3, 4, False, True, 0, 0)
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
        if line_ids:
            for id in line_ids:
                hex_drawing.delete(id)
            line_ids.clear()
        path_text.value = ""
        return
    else:
        path = hexagon.getPathIndexes(src_slider.value, dest_slider.value)
        path_text.value = " --> ".join(map(str, path))
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
settings_box = Box(app, width=450, height=200, border=True, layout="grid", grid=[0, 1])
sliders_box = Box(settings_box, border=True, layout="grid", grid=[0, 0])
button_box = Box(settings_box, border=True, layout="grid", grid=[1, 0])
path_box = Box(settings_box, border=True, layout="grid", grid=[0, 1])

# hexagon structure
hex_drawing = Drawing(image_box, width="fill", height="fill")
line_ids = list()
drawHexagons()

# sliders
Text(sliders_box, text="Source", font=HEADING_FONT, grid=[0, 0])
src_slider = Slider(sliders_box, start=0, end=hexagon.count - 1, grid=[1, 0])

Text(sliders_box, text="Destination", font=HEADING_FONT, grid=[0, 1])
dest_slider = Slider(sliders_box, start=0, end=hexagon.count - 1, grid=[1, 1])

# button for drawing box
start_button = PushButton(
    button_box,
    width="fill",
    height="fill",
    command=drawPath,
    text="Draw Path",
    grid=[0, 0],
)
start_button.font = HEADING_FONT

# path
Text(path_box, text="Path", font=HEADING_FONT, grid=[0, 0])
path_text = Text(path_box, font=BODY_FONT, grid=[1, 0])


app.display()
