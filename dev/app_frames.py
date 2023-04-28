from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# text fonts
TITLE_FONT = ("TkHeadingFont", 35)
SUBTITLE_FONT = ("TkTextFont", 18)
HEADING_FONT = ("TkHeadingFont", 14)
BODY_FONT = ("TkTextFont", 10)
# image sizes
TITLE_ICON_SIZE = (200, 160)
HEADING_ICON_SIZE = (50, 50)
BUTTON_ICON_SIZE = (30, 30)


def get_tk_image(file, size, assets="app/assets/"):
    with Image.open(assets + file) as img:
        return ImageTk.PhotoImage(img.resize(size))


class TitleFrame(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        # load title icon
        self.title_icon = get_tk_image("conveyor.png", TITLE_ICON_SIZE)
        # title icon label
        ttk.Label(self, anchor="w", image=self.title_icon).grid(
            column=0, row=0, rowspan=2, sticky=(N, S, E, W)
        )
        # title text label
        ttk.Label(
            self,
            text="Omniveyor GUI",
            font=TITLE_FONT,
            anchor="center",
        ).grid(column=1, row=0, sticky=(N, S, E, W))
        # subtitle text label
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
        self.canvas.grid(column=0, row=0, rowspan=2, sticky=(N, S, E, W))
        # load config icon
        self.config_icon = get_tk_image("hexagons1.png", HEADING_ICON_SIZE)
        # title label
        ttk.Label(
            self,
            text="Configuration",
            font=HEADING_FONT,
            compound="left",
            image=self.config_icon,
            anchor="center",
            relief="ridge",
        ).grid(column=1, row=0, sticky=(N, S, E, W))
        # info label
        ttk.Label(
            self,
            text="Rows:\t\t3\n\nColumns:\t\t4\n\nOrientation:\tPointy Top\n\nOffset:\t\tOdd",
            font=BODY_FONT,
            anchor="center",
            relief="ridge",
        ).grid(column=1, row=1, sticky=(N, S, E, W))
        # video feed label
        self.video_label = ttk.Label(self, anchor="center", relief="ridge")
        self.video_label.grid(column=2, row=0, rowspan=2, sticky=(N, S, E, W))


class PathFrame(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        # load title icon
        self.title_icon = get_tk_image("path_icon.png", HEADING_ICON_SIZE)
        # title label
        ttk.Label(
            self,
            text="Path Finder",
            image=self.title_icon,
            compound="left",
            font=HEADING_FONT,
            anchor="center",
        ).grid(column=0, row=0, columnspan=4, sticky=(N, S, E, W))
        # start point label
        ttk.Label(self, font=BODY_FONT, text="Start Point", anchor="w").grid(
            column=0, row=1, sticky=(N, S, E, W)
        )
        # start point spinbox
        self.start_spinbox = ttk.Spinbox(self, from_=0, to=9)
        self.start_spinbox.state(["readonly"])
        self.start_spinbox.grid(column=1, row=1, padx=5, pady=5, sticky=(N, S, E, W))
        # end point label
        ttk.Label(self, font=BODY_FONT, text="End Point", anchor="w").grid(
            column=0, row=2, sticky=(N, S, E, W)
        )
        # end point spinbox
        self.end_spinbox = ttk.Spinbox(self, from_=0, to=9)
        self.end_spinbox.state(["readonly"])
        self.end_spinbox.grid(column=1, row=2, padx=5, pady=5, sticky=(N, S, E, W))
        # mode select button
        self.mode_button = ttk.Checkbutton(
            self,
            text="Use Manual Path",
            onvalue=True,
            offvalue=False,
        )
        self.mode_button.grid(
            column=2, row=1, columnspan=2, rowspan=2, sticky=(N, S, E, W)
        )
        # load draw icon
        self.draw_icon = get_tk_image("draw_icon.png", BUTTON_ICON_SIZE)
        # draw path button
        self.draw_button = ttk.Button(
            self,
            text="Draw Shortest Path",
            image=self.draw_icon,
            compound="top",
            padding=5,
        )
        self.draw_button.grid(column=0, row=3, columnspan=2, sticky=(N, S, E, W))
        # load move icon
        self.move_icon = get_tk_image("move_icon.png", BUTTON_ICON_SIZE)
        # move path button
        self.move_button = ttk.Button(
            self,
            text="Traverse Path",
            image=self.move_icon,
            compound="top",
            padding=5,
            state=["disabled"],
        )
        self.move_button.grid(column=2, row=3, columnspan=2, sticky=(N, S, E, W))
        # path text label
        ttk.Label(self, text="Path", font=BODY_FONT).grid(
            column=0, row=4, sticky=(N, S, E, W)
        )
        # path text entry
        self.path_entry = ttk.Entry(self, state=["readonly"], font=BODY_FONT)
        self.path_entry.grid(column=1, row=4, columnspan=3, sticky=(N, S, E, W))
