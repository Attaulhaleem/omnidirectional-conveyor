from guizero import App, Box, ButtonGroup, Drawing, PushButton, Slider, Text
import hexagon

""" CALLBACK FUNCTIONS """

# called when button pressed, draw hexagons on screen
def drawHexagons():
    hex_drawing.clear()
    hexagon.path.clear()
    path_text.clear()
    length = len_slider.value
    rows = row_slider.value
    cols = col_slider.value
    flat_top = config_choice.value == "F"
    odd_offset = offset_choice.value == "O"
    fill_color = (red_slider.value, green_slider.value, blue_slider.value)
    drawingPoints = hexagon.generate(length, rows, cols, flat_top, odd_offset)
    for pts in drawingPoints:
        hex_drawing.polygon(pts, color=fill_color, outline=True)
    print(hexagon.coordinates)
    print(hexagon.positions)


def getClickedIndex():
    try:
        return hex_drawing.tk.find_withtag("current")[0] - 1
    except:
        return None


# called when left click on hexagon
def tracePath():
    id = getClickedIndex()
    if id in hexagon.getValidIndexes():
        hexagon.path.append(id)
        path_text.value = hexagon.path


def setCursor():
    id = getClickedIndex()
    if id in hexagon.getValidIndexes():
        hex_drawing.tk.config(cursor="plus")
    else:
        hex_drawing.tk.config(cursor="")


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
text_box = Box(app, width="fill", align="top", border=True)
image_box = Box(app, width="fill", height="fill", align="bottom")

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
start_button = PushButton(config_box, command=drawHexagons, text="Generate")
start_button.font = BODY_FONT

# path text
Text(text_box, text="Path", font=HEADING_FONT, align="left")
path_text = Text(text_box, font=BODY_FONT, align="left")

# hexagon structure
hex_drawing = Drawing(image_box, width="fill", height="fill")

# events
hex_drawing.when_mouse_moved = setCursor
hex_drawing.when_left_button_pressed = tracePath

app.display()
