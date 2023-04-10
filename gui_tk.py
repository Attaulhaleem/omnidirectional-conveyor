from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import hexagon

# top level window
root = Tk()
root.state("zoomed")

# main window
main_frame = ttk.Frame(root, padding=10)

# define style for Frame template
normal_frame_style = ttk.Style()
normal_frame_style.configure("Normal.TFrame", relief="ridge", borderwidth=10, padding=5)

# frame for title and subtitle
title_frame = ttk.Frame(main_frame, style="Normal.TFrame")

# load and resize title image
title_image = Image.open("app/assets/hexagons1.png")
title_image = title_image.resize((120, 120))
title_image = ImageTk.PhotoImage(title_image)
# add image to label
title_image_label = ttk.Label(title_frame, anchor="w", image=title_image)

# title label
title_text_label = ttk.Label(
    title_frame,
    text="OmniVeyor GUI",
    font=("TkHeadingFont", 30),
    anchor="center",
)

# subtitle label
subtitle_label = ttk.Label(
    title_frame,
    text="Atta ul Haleem\tInshal Khan\tMustafa Ansari\tShaheer Ahmed",
    font=("TkMenuFont", 10),
    anchor="center",
)

# frame for hexagons canvas and statistics
display_frame = ttk.Frame(main_frame, style="Normal.TFrame")

# hexagon drawing
hexagons_canvas = Canvas(display_frame)

grid = hexagon.generate(50, 3, 4, False, True, 10, 10)
for coords in grid:
    hexagons_canvas.create_polygon(
        coords, fill="#00a1af", outline="#000000", activefill="#59a310"
    )
for widget in hexagons_canvas.winfo_children():
    widget.grid_configure(padx=10, pady=10)

display_label = ttk.Label(
    display_frame,
    text="Rows:\t\t3\n\nColumns:\t\t4\n\nOrientation:\tPointy Top\n\nOffset:\t\tOdd",
    font=("TkHeadingFont", 12),
    anchor="center",
)

feed_frame = ttk.Frame()
# align objects to grid
main_frame.grid(
    column=0, row=0, sticky=(N, S, E, W)
)  # column=0, row=0, sticky=(N, S, E, W))
# title
title_frame.grid(column=0, row=0, rowspan=2, columnspan=2, sticky=(N, S, E, W))
title_image_label.grid(column=0, row=0, rowspan=2, sticky=(N, S, E, W))
title_text_label.grid(column=1, row=0, sticky=(N, S, E, W))
subtitle_label.grid(column=1, row=1, sticky=(N, S, E, W))
# display
display_frame.grid(column=0, row=2, sticky=(N, S, E, W))
hexagons_canvas.grid(column=0, row=0, padx=20, pady=20, sticky=(N, S, E, W))
display_label.grid(column=1, row=0, sticky=(N, S, E, W))

# set resizing properties
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)
title_frame.columnconfigure(1, weight=1)
display_frame.columnconfigure(0, weight=1)
hexagons_canvas.columnconfigure(0, weight=1)
hexagons_canvas.rowconfigure(0, weight=1)

root.mainloop()
