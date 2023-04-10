from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import hexagon
from videofeed import LabelVideoFeed

# FONTS
TITLE_FONT = ("TkHeadingFont", 30)
SUBTITLE_FONT = ("TkMenuFont", 15)
HEADING_FONT = ("TkHeadingFont", 14)
BODY_FONT = ("TkTextFont", 10)

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
title_image = Image.open("app/assets/hex-box-blue.png")
title_image = title_image.resize((120, 120))
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
    text="Atta ul Haleem\tInshal Khan\tMustafa Ansari\tShaheer Ahmed",
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
config_image = config_image.resize((50, 50))
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
LabelVideoFeed(feed_label, 480, 270, 30)

""" CONTROL """


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


""" RESIZING PROPERTIES """
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)
title_frame.columnconfigure(1, weight=1)
display_frame.columnconfigure(0, weight=1)
display_frame.columnconfigure(1, weight=1)
display_frame.columnconfigure(2, weight=1)

root.mainloop()
