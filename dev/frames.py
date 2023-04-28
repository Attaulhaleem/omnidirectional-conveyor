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
