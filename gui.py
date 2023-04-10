from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import hexagon
from videofeed import LabelVideoFeed

# FONTS
TITLE_FONT = ("TkHeadingFont", 35)
SUBTITLE_FONT = ("TkTextFont", 18)
HEADING_FONT = ("TkHeadingFont", 14)
BODY_FONT = ("TkTextFont", 10)

# IMAGE SIZES
TITLE_ICON_SIZE = (120, 120)
HEADING_ICON_SIZE = (50, 50)
BUTTON_ICON_SIZE = (30, 30)

""" WINDOW """
root = Tk()
root.state("zoomed")

main_frame = ttk.Frame(root, padding=10)
# define style for frame templates
normal_frame_style = ttk.Style()
normal_frame_style.configure("Normal.TFrame", padding=5)

""" TITLE """
title_frame = ttk.Frame(main_frame, style="Normal.TFrame")

# load and resize title image
title_image = Image.open("app/assets/hex_box_blue.png")
title_image = title_image.resize(TITLE_ICON_SIZE)
title_image = ImageTk.PhotoImage(title_image)
# add image to label
title_image_label = ttk.Label(title_frame, anchor="w", image=title_image)

# title label
title_text_label = ttk.Label(
    title_frame,
    text="OmniVeyor GUI",
    font=TITLE_FONT,
    anchor="center",
)

# subtitle label
subtitle_label = ttk.Label(
    title_frame,
    text="By Atta, Inshal, Mustafa & Shaheer",
    font=SUBTITLE_FONT,
    anchor="center",
)

""" DISPLAY """
display_frame = ttk.Frame(main_frame, style="Normal.TFrame", relief="raised")

# hexagon drawing
hexagons_canvas = Canvas(
    display_frame, highlightthickness=1, highlightbackground="black"
)

grid = hexagon.generate(50, 3, 4, False, True, 10, 10)
for i in range(len(grid)):
    hexagons_canvas.create_polygon(
        grid[i], fill="#00a1af", outline="black", activefill="#59a310"
    )
    hexagons_canvas.create_text(
        hexagon.positions[i][0], hexagon.positions[i][1], text=str(i + 1)
    )
for widget in hexagons_canvas.winfo_children():
    widget.grid_configure(padx=10, pady=10)

# load and resize config image
config_image = Image.open("app/assets/hexagons1.png")
config_image = config_image.resize(HEADING_ICON_SIZE)
config_image = ImageTk.PhotoImage(config_image)

display_title_label = ttk.Label(
    display_frame,
    text="Configuration",
    font=HEADING_FONT,
    compound="left",
    image=config_image,
    relief="ridge",
    anchor="center",
)

display_label = ttk.Label(
    display_frame,
    text="Rows:\t\t3\n\nColumns:\t\t4\n\nOrientation:\tPointy Top\n\nOffset:\t\tOdd",
    font=BODY_FONT,
    anchor="center",
    relief="ridge",
    padding=10,
)

feed_label = ttk.Label(display_frame, relief="raised", anchor="center")
# LabelVideoFeed(feed_label, 480, 270, 30)

""" CONTROL """
control_frame = ttk.Frame(main_frame, style="Normal.TFrame")

spath_frame = ttk.Frame(control_frame, relief="sunken")

spath_title_image = Image.open("app/assets/path_icon1.png")
spath_title_image = spath_title_image.resize(HEADING_ICON_SIZE)
spath_title_image = ImageTk.PhotoImage(spath_title_image)

spath_title_label = ttk.Label(
    spath_frame,
    text="Shortest Path",
    image=spath_title_image,
    compound="left",
    font=HEADING_FONT,
    anchor="center",
)

spath_src_label = ttk.Label(spath_frame, font=BODY_FONT, text="Start", anchor="w")
spath_src = IntVar()
spath_src_spinbox = ttk.Spinbox(spath_frame, from_=1, to=10, textvariable=spath_src)

spath_dest_label = ttk.Label(spath_frame, font=BODY_FONT, text="End", anchor="w")
spath_dest = IntVar()
spath_dest_spinbox = ttk.Spinbox(spath_frame, from_=1, to=10, textvariable=spath_dest)

spath_button_image = Image.open("app/assets/draw_icon.png")
spath_button_image = spath_button_image.resize(BUTTON_ICON_SIZE)
spath_button_image = ImageTk.PhotoImage(spath_button_image)

spath_button = ttk.Button(
    spath_frame,
    text="Draw Shortest Path",
    image=spath_button_image,
    compound="top",
    padding=5,
)

""" GEOMETRY MANAGEMENT """
main_frame.grid(column=0, row=0, sticky=(N, S, E, W))

title_frame.grid(column=0, row=0, sticky=(N, S, E, W))
title_image_label.grid(column=0, row=0, rowspan=2, sticky=(N, S, E, W))
title_text_label.grid(column=1, row=0, sticky=(N, S, E, W))
subtitle_label.grid(column=1, row=1, sticky=(N, S, E, W))

display_frame.grid(column=0, row=1, sticky=(N, S, E, W))
hexagons_canvas.grid(column=0, row=0, rowspan=2, padx=20, pady=20, sticky=(N, S, E, W))
display_title_label.grid(column=1, row=0, sticky=(N, S, E, W))
display_label.grid(column=1, row=1, sticky=(N, S, E, W))
feed_label.grid(column=2, row=0, rowspan=2, sticky=(N, S, E, W))

control_frame.grid(column=0, row=2, sticky=(N, S, E, W))

spath_frame.grid(column=0, row=0, sticky=(N, S, E, W))
spath_title_label.grid(column=0, row=0, columnspan=2, sticky=(N, S, E, W))
spath_src_label.grid(column=0, row=1, sticky=(N, S, E, W))
spath_src_spinbox.grid(column=1, row=1, padx=5, pady=5, sticky=(N, S, E, W))
spath_dest_label.grid(column=0, row=2, sticky=(N, S, E, W))
spath_dest_spinbox.grid(column=1, row=2, padx=5, pady=5, sticky=(N, S, E, W))
spath_button.grid(column=0, row=3, columnspan=2, sticky=(N, S, E, W))

""" RESIZING PROPERTIES """
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)
title_frame.columnconfigure(1, weight=1)
display_frame.columnconfigure(0, weight=1)
display_frame.columnconfigure(1, weight=1)
display_frame.columnconfigure(2, weight=1)
control_frame.columnconfigure(0, weight=1)

root.mainloop()
