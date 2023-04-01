from guizero import App, Box, ButtonGroup, Drawing, PushButton, Slider, Text
import hexagon

""" CALLBACK FUNCTIONS """

# called when button pressed, draw hexagons on screen
def drawHexagons():
    drawing.clear()
    length = len_slider.value
    rows = row_slider.value
    cols = col_slider.value
    flat_top = config_choice.value == "F"
    odd_offset = offset_choice.value == "O"
    fill_color = (red_slider.value, green_slider.value, blue_slider.value)
    drawingPoints = hexagon.generate(length, rows, cols, flat_top, odd_offset)
    for pts in drawingPoints:
        drawing.polygon(
            pts,
            color=fill_color,
            outline=True,
            outline_color="black",
        )
    print(hexagon.coordinates)
    print(hexagon.positions)


# called on left click on hexagon drawing
def tracePath(event_data):
    mouse_pos = (event_data.x, event_data.y)
    index = hexagon.findNearestIndex(mouse_pos)
    print("Clicked Hexagon: ", hexagon.positions[index][0], hexagon.positions[index][1])


""" APP """

# fonts
HEADING_FONT = "Inter Medium"
BODY_FONT = "Inter Regular"

# colors
BG_COLOR = (250, 249, 246)

# app elements
app = App(title="Omniveyor", bg=BG_COLOR)
# app.tk.state("zoomed")  # maximize window
sliders_box = Box(app, width="fill", align="top")
config_box = Box(app, width="fill", align="top", border=True)
image_box = Box(app, width="fill", height="fill", align="bottom")
drawing = Drawing(image_box, width="fill", height="fill")

# length, row, col sliders
Text(sliders_box, text="Size", font=HEADING_FONT, align="left")
len_slider = Slider(sliders_box, start=20, end=50, align="left")
Text(sliders_box, text="Rows", font=HEADING_FONT, align="left")
row_slider = Slider(sliders_box, start=1, end=20, align="left")
Text(sliders_box, text="Cols", font=HEADING_FONT, align="left")
col_slider = Slider(sliders_box, start=1, end=20, align="left")
# default values
len_slider.value = 50
row_slider.value, col_slider.value = (3, 4)

# RGB sliders
blue_slider = Slider(sliders_box, start=0, end=255, align="right")
Text(sliders_box, text="Blue", font=HEADING_FONT, color="blue", align="right")
green_slider = Slider(sliders_box, start=0, end=255, align="right")
Text(sliders_box, text="Green", font=HEADING_FONT, color="green", align="right")
red_slider = Slider(sliders_box, start=0, end=255, align="right")
Text(sliders_box, text="Red", font=HEADING_FONT, color="red", align="right")
# default values
red_slider.value, green_slider.value, blue_slider.value = (29, 109, 134)

# orientation choice
Text(config_box, text="Orientation", font=HEADING_FONT, align="left")
config_choice = ButtonGroup(
    config_box,
    options=[["Flat Top", "F"], ["Pointy Top", "P"]],
    selected="P",
    horizontal=True,
    align="left",
)
config_choice.font = BODY_FONT

# offset choice
offset_choice = ButtonGroup(
    config_box,
    options=[["Even", "E"], ["Odd", "O"]],
    selected="O",
    horizontal=True,
    align="right",
)
offset_choice.font = BODY_FONT
Text(config_box, text="Offset", font=HEADING_FONT, align="right")

# button for generating hexagons
start = PushButton(config_box, command=drawHexagons, text="Generate")
start.font = BODY_FONT

# events
drawing.when_left_button_pressed = tracePath

app.display()
