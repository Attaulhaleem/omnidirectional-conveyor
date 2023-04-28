from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# assets path
ASSETS_PATH = "app/assets/"
# text fonts
TITLE_FONT = ("TkHeadingFont", 35)
SUBTITLE_FONT = ("TkTextFont", 18)
HEADING_FONT = ("TkHeadingFont", 14)
BODY_FONT = ("TkTextFont", 10)
# image sizes
TITLE_ICON_SIZE = (200, 160)
HEADING_ICON_SIZE = (50, 50)
BUTTON_ICON_SIZE = (30, 30)


def get_tk_image(file, size):
    with Image.open(ASSETS_PATH + file) as img:
        return ImageTk.PhotoImage(img.resize(size))


class TitleFrame(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        # load the title image
        self.title_image = get_tk_image("conveyor.png", TITLE_ICON_SIZE)
        # title image
        ttk.Label(self, anchor="w", image=self.title_image).grid(
            column=0, row=0, rowspan=2, sticky=(N, S, E, W)
        )
        # title text
        ttk.Label(
            self,
            text="Omniveyor GUI",
            font=TITLE_FONT,
            anchor="center",
        ).grid(column=1, row=0, sticky=(N, S, E, W))
        # subtitle text
        ttk.Label(
            self,
            text="By Atta, Inshal, Mustafa & Shaheer",
            font=SUBTITLE_FONT,
            anchor="center",
        ).grid(column=1, row=1, sticky=(N, S, E, W))


class DisplayFrame(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        # canvas for hexagons
        self.canvas = Canvas(self, highlightthickness=1, highlightbackground="black")
        self.canvas.old_coords = None
        self.canvas.grid(
            column=0, row=0, rowspan=2, padx=10, pady=10, sticky=(N, S, E, W)
        )

        # load config image
        self.config_image = get_tk_image("hexagons1.png", HEADING_ICON_SIZE)
        # display title
        ttk.Label(
            self,
            text="Configuration",
            font=HEADING_FONT,
            compound="left",
            image=self.config_image,
            relief="ridge",
            anchor="center",
        ).grid(column=1, row=0, sticky=(N, S, E, W))
        # display info
        ttk.Label(
            self,
            text="Rows:\t\t3\n\nColumns:\t\t4\n\nOrientation:\tPointy Top\n\nOffset:\t\tOdd",
            font=BODY_FONT,
            anchor="center",
            relief="ridge",
            padding=10,
        ).grid(column=1, row=1, sticky=(N, S, E, W))
        # video feed
        self.video_label = ttk.Label(self, relief="raised", anchor="center")
        self.video_label.grid(column=2, row=0, rowspan=2, sticky=(N, S, E, W))


class PathFrame(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        # load path title image
        self.path_title_image = get_tk_image("path_icon.png", HEADING_ICON_SIZE)
        # path title label
        ttk.Label(
            self,
            text="Path Finder",
            image=self.path_title_image,
            compound="left",
            font=HEADING_FONT,
            anchor="center",
        ).grid(column=0, row=0, columnspan=4, sticky=(N, S, E, W))
        # path source label
        ttk.Label(self, font=BODY_FONT, text="Start Point", anchor="w").grid(
            column=0, row=1, sticky=(N, S, E, W)
        )
        # path source
        path_src = IntVar()
        path_src_spinbox = ttk.Spinbox(self, from_=0, to=9, textvariable=path_src)
        path_src_spinbox.state(["readonly"])
        path_src_spinbox.grid(column=1, row=1, padx=5, pady=5, sticky=(N, S, E, W))
        # path destination label
        ttk.Label(self, font=BODY_FONT, text="End Point", anchor="w").grid(
            column=0, row=2, sticky=(N, S, E, W)
        )
        # path destination
        path_dest = IntVar()
        path_dest.set(1)
        path_dest_spinbox = ttk.Spinbox(self, from_=0, to=9, textvariable=path_dest)
        path_dest_spinbox.state(["readonly"])
        path_dest_spinbox.grid(column=1, row=2, padx=5, pady=5, sticky=(N, S, E, W))
        # manual path
        manual_path = BooleanVar()
        path_list = list()
        # mode select button
        self.path_checkbutton = ttk.Checkbutton(
            self,
            text="Use Manual Path",
            variable=manual_path,
            onvalue=True,
            offvalue=False,
        )
        self.path_checkbutton.grid(
            column=2, row=1, columnspan=2, rowspan=2, sticky=(N, S, E, W)
        )
        # load draw path image
        self.path_draw_image = get_tk_image("draw_icon.png", BUTTON_ICON_SIZE)
        # draw path button
        self.path_draw_button = ttk.Button(
            self,
            text="Draw Shortest Path",
            image=self.path_draw_image,
            compound="top",
            padding=5,
        )
        self.path_draw_button.grid(column=0, row=3, columnspan=2, sticky=(N, S, E, W))
        # load move path image
        self.path_move_image = get_tk_image("move_icon.png", BUTTON_ICON_SIZE)
        # move path button
        self.path_move_button = ttk.Button(
            self,
            text="Traverse Path",
            image=self.path_move_image,
            compound="top",
            padding=5,
            state=["disabled"],
        )
        self.path_move_button.grid(column=2, row=3, columnspan=2, sticky=(N, S, E, W))
        # path text label
        ttk.Label(self, text="Path", font=BODY_FONT).grid(
            column=0, row=4, sticky=(N, S, E, W)
        )
        # path text variable
        path_text = StringVar()
        # path text entry
        ttk.Entry(
            self, state=["readonly"], font=BODY_FONT, textvariable=path_text
        ).grid(column=1, row=4, columnspan=3, sticky=(N, S, E, W))
