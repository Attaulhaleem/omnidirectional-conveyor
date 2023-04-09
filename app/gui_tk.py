from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# top level window
root = Tk()
# root.state("zoomed")

# main window
main_frame = ttk.Frame(root, padding=10)

# define style for Frame template
normal_frame_style = ttk.Style()
normal_frame_style.configure(
    "Normal.TFrame", background="blue", relief="ridge", borderwidth=10, padding=5
)

# frame for title and subtitle
title_frame = ttk.Frame(main_frame, style="Normal.TFrame")

# load and resize title image
title_image = Image.open("app/assets/hexagons1.png")
title_image = title_image.resize((120, 120))
title_image = ImageTk.PhotoImage(title_image)
# add image to label
title_image_label = ttk.Label(
    title_frame, anchor="w", image=title_image, background="pink"
)

# title label
title_text_label = ttk.Label(
    title_frame,
    text="OmniVeyor GUI",
    font=("TkHeadingFont", 30),
    anchor="center",
    background="orange",
)

# subtitle label
subtitle_label = ttk.Label(
    title_frame,
    text="Atta ul Haleem\tInshal Khan\tMustafa Ansari\tShaheer Ahmed",
    font=("TkMenuFont", 10),
    anchor="center",
    background="yellow",
)

# frame for hexagons canvas and statistics
hexagons_frame = ttk.Frame(main_frame, style="Normal.TFrame")


# hexagon drawing
hexagons_canvas = Canvas(hexagons_frame)

# align objects to grid
main_frame.grid(column=0, row=0, sticky=(N, S, E, W))
# title
title_frame.grid(column=0, row=0, sticky=(N, S, E, W))
title_image_label.grid(column=0, row=0, rowspan=2, sticky=(N, S, E, W))
title_text_label.grid(column=1, row=0, sticky=(N, S, E, W))
subtitle_label.grid(column=1, row=1, sticky=(N, S, E, W))
# hexagons
hexagons_frame.grid(column=0, row=1, sticky=(N, S, E, W))

# set resizing properties
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)
title_frame.columnconfigure(1, weight=1)

root.mainloop()
