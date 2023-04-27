from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from videofeed import LabelVideoFeed
from omniveyor import Omniveyor

""" ASSETS """
assets_path = "app/assets/"

""" CALLBACK FUNCTIONS """


# def loadTkImage(file, dir="", size=(10, 10)):
#     img = Image.open(dir + file)
#     img = img.resize(TITLE_ICON_SIZE)
#     img = ImageTk.PhotoImage(img)


def movePath():
    return


def clearManualPath(e):
    hexagons_canvas.delete("spline")
    hexagons_canvas.old_coords = None
    path_list.clear()
    path_text.set("")


def drawManualPath(e):
    if not manual_path.get():
        return
    index = hex_grid.get_nearest_index((e.x, e.y))
    if len(path_list) == 0 or path_list[-1] != index:
        path_list.append(index)
        path_text.set(" -> ".join(map(str, path_list)))
    x, y = hex_grid.hexagons[index].position
    if hexagons_canvas.old_coords is not None:
        x1, y1 = hexagons_canvas.old_coords
        hexagons_canvas.create_line(
            x, y, x1, y1, width=3, smooth=1, tags="spline", arrow="first"
        )
    hexagons_canvas.old_coords = x, y


def drawShortestPath():
    global path_list
    hexagons_canvas.delete("lines")
    path_move_button.state(["disabled"])
    if path_src.get() == path_dest.get():
        path_text.set("")
        messagebox.showerror("Error", "Start and end points cannot be the same!")
        return
    path_list = hex_grid.get_path_indexes(path_src.get(), path_dest.get())
    path_text.set(" -> ".join(map(str, path_list)))
    path_positions = [val for i in path_list for val in hex_grid.hexagons[i].position]
    hexagons_canvas.create_line(
        path_positions, arrow="last", capstyle="round", tags="lines", width=3
    )
    path_move_button.state(["!disabled"])


def activateManual():
    if manual_path.get():
        new_state = ["disabled"]
        path_move_button.state(["!disabled"])
    else:
        new_state = ["!disabled"]
        path_move_button.state(["disabled"])
    path_src_spinbox.state(new_state)
    path_dest_spinbox.state(new_state)
    path_draw_button.state(new_state)
    path_list.clear()
    path_text.set("")
    hexagons_canvas.delete("lines")
    hexagons_canvas.delete("spline")
    hexagons_canvas.old_coords = None


""" FONTS """
TITLE_FONT = ("TkHeadingFont", 35)
SUBTITLE_FONT = ("TkTextFont", 18)
HEADING_FONT = ("TkHeadingFont", 14)
BODY_FONT = ("TkTextFont", 10)

""" IMAGE SIZES """
TITLE_ICON_SIZE = (200, 160)
HEADING_ICON_SIZE = (50, 50)
BUTTON_ICON_SIZE = (30, 30)

""" WINDOW """
root = Tk()
root.attributes("-fullscreen", True)
main_frame = ttk.Frame(root, padding=10)

""" TEMPLATE """
# normal_frame_style = ttk.Style()
# normal_frame_style.configure("Normal.TFrame", padding=5)
ttk.Style().configure("Normal.TFrame", padding=5)

""" TITLE """
title_frame = ttk.Frame(main_frame, style="Normal.TFrame")

# load and resize title image
title_image = Image.open(assets_path + "conveyor.png")
title_image = title_image.resize(TITLE_ICON_SIZE)
title_image = ImageTk.PhotoImage(title_image)
# add image to label
title_image_label = ttk.Label(title_frame, anchor="w", image=title_image)

# title label
title_text_label = ttk.Label(
    title_frame,
    text="Omniveyor GUI",
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
hexagons_canvas.tag_bind("hexagon", "<Button-1>", clearManualPath)
hexagons_canvas.tag_bind("hexagon", "<B1-Motion>", drawManualPath)

hex_grid = Omniveyor().hex_grid
for hexagon in hex_grid.hexagons:
    hexagons_canvas.create_polygon(
        hexagon.points,
        fill="#00a1af",
        outline="black",
        activefill="#59a310",
        tags="hexagon",
    )
    hexagons_canvas.create_text(
        hexagon.position[0], hexagon.position[1], text=str(hexagon.id), tags="id"
    )
for widget in hexagons_canvas.winfo_children():
    widget.grid_configure(padx=10, pady=10)

# load and resize config image
config_image = Image.open(assets_path + "hexagons1.png")
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

""" PATH FINDER """
path_frame = ttk.Frame(main_frame, style="Normal.TFrame", relief="sunken")

path_title_image = Image.open(assets_path + "path_icon.png")
path_title_image = path_title_image.resize(HEADING_ICON_SIZE)
path_title_image = ImageTk.PhotoImage(path_title_image)

path_title_label = ttk.Label(
    path_frame,
    text="Path Finder",
    image=path_title_image,
    compound="left",
    font=HEADING_FONT,
    anchor="center",
)

path_src_label = ttk.Label(path_frame, font=BODY_FONT, text="Start Point", anchor="w")
path_src = IntVar()
path_src_spinbox = ttk.Spinbox(path_frame, from_=0, to=9, textvariable=path_src)
path_src_spinbox.state(["readonly"])

path_dest_label = ttk.Label(path_frame, font=BODY_FONT, text="End Point", anchor="w")
path_dest = IntVar()
path_dest_spinbox = ttk.Spinbox(path_frame, from_=0, to=9, textvariable=path_dest)
path_dest_spinbox.state(["readonly"])
path_dest.set(1)

manual_path = BooleanVar()
path_list = list()
path_checkbutton = ttk.Checkbutton(
    path_frame,
    text="Use Manual Path",
    variable=manual_path,
    onvalue=True,
    offvalue=False,
    command=activateManual,
)

path_draw_image = Image.open(assets_path + "draw_icon.png")
path_draw_image = path_draw_image.resize(BUTTON_ICON_SIZE)
path_draw_image = ImageTk.PhotoImage(path_draw_image)

path_draw_button = ttk.Button(
    path_frame,
    text="Draw Shortest Path",
    image=path_draw_image,
    command=drawShortestPath,
    compound="top",
    padding=5,
)

path_move_image = Image.open(assets_path + "move_icon.png")
path_move_image = path_move_image.resize(BUTTON_ICON_SIZE)
path_move_image = ImageTk.PhotoImage(path_move_image)

path_move_button = ttk.Button(
    path_frame,
    text="Traverse Path",
    image=path_move_image,
    command=movePath,
    compound="top",
    padding=5,
    state=["disabled"],
)

path_text_label = ttk.Label(path_frame, text="Path", font=BODY_FONT)

path_text = StringVar()
path_text_entry = ttk.Entry(
    path_frame, state=["readonly"], font=BODY_FONT, textvariable=path_text
)

""" GEOMETRY MANAGEMENT """
main_frame.grid(column=0, row=0, sticky=(N, S, E, W))

title_frame.grid(column=0, row=0, sticky=(N, S, E, W))
title_image_label.grid(column=0, row=0, rowspan=2, sticky=(N, S, E, W))
title_text_label.grid(column=1, row=0, sticky=(N, S, E, W))
subtitle_label.grid(column=1, row=1, sticky=(N, S, E, W))

display_frame.grid(column=0, row=1, sticky=(N, S, E, W))
hexagons_canvas.grid(column=0, row=0, rowspan=2, padx=20, pady=20, sticky=(N, S, E, W))
hexagons_canvas.old_coords = None
display_title_label.grid(column=1, row=0, sticky=(N, S, E, W))
display_label.grid(column=1, row=1, sticky=(N, S, E, W))
feed_label.grid(column=2, row=0, rowspan=2, sticky=(N, S, E, W))

path_frame.grid(column=0, row=2, sticky=(N, S, E, W))
path_title_label.grid(column=0, row=0, columnspan=4, sticky=(N, S, E, W))
path_src_label.grid(column=0, row=1, sticky=(N, S, E, W))
path_src_spinbox.grid(column=1, row=1, padx=5, pady=5, sticky=(N, S, E, W))
path_dest_label.grid(column=0, row=2, sticky=(N, S, E, W))
path_dest_spinbox.grid(column=1, row=2, padx=5, pady=5, sticky=(N, S, E, W))
path_checkbutton.grid(column=2, row=1, columnspan=2, rowspan=2, sticky=(N, S, E, W))
path_draw_button.grid(column=0, row=3, columnspan=2, sticky=(N, S, E, W))
path_move_button.grid(column=2, row=3, columnspan=2, sticky=(N, S, E, W))
path_text_label.grid(column=0, row=4, sticky=(N, S, E, W))
path_text_entry.grid(column=1, row=4, columnspan=3, sticky=(N, S, E, W))

""" RESIZING PROPERTIES """
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)

title_frame.columnconfigure(1, weight=1)
title_frame.rowconfigure(0, weight=1)
title_frame.rowconfigure(1, weight=1)

display_frame.columnconfigure(0, weight=3)
display_frame.columnconfigure(1, weight=1)
display_frame.columnconfigure(2, weight=3)
display_frame.rowconfigure(0, weight=5)
display_frame.rowconfigure(1, weight=5)

path_frame.columnconfigure(0, weight=1)
path_frame.columnconfigure(1, weight=1)
path_frame.columnconfigure(2, weight=1)
path_frame.columnconfigure(3, weight=1)
path_frame.rowconfigure(0, weight=3)
path_frame.rowconfigure(1, weight=3)


root.mainloop()
