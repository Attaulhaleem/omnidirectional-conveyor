from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from omniveyor import Omniveyor


def get_image(file, size):
    with Image.open(file) as img:
        return ImageTk.PhotoImage(img.resize(size))


class TitleFrame(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.TITLE_FONT = ("TkHeadingFont", 35)
        self.SUBTITLE_FONT = ("TkTextFont", 18)
        self.TITLE_ICON_SIZE = (200, 160)
        self.title_image = get_image("app/assets/conveyor.png", self.TITLE_ICON_SIZE)
        # title image
        ttk.Label(self, anchor="w", image=self.title_image).grid(
            column=0, row=0, rowspan=2, sticky=(N, S, E, W)
        )
        # title text
        ttk.Label(
            self,
            text="Omniveyor GUI",
            font=self.TITLE_FONT,
            anchor="center",
        ).grid(column=1, row=0, sticky=(N, S, E, W))
        # subtitle text
        ttk.Label(
            self,
            text="By Atta, Inshal, Mustafa & Shaheer",
            font=self.SUBTITLE_FONT,
            anchor="center",
        ).grid(column=1, row=1, sticky=(N, S, E, W))


class DisplayFrame(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.canvas = Canvas(self, highlightthickness=1, highlightbackground="black")
        self.canvas.old_coords = None
        self.canvas.tag_bind("hexagon", "<Button-1>", self.clear_manual_path)
        self.canvas.tag_bind("hexagon", "<B1-Motion>", self.draw_manual_path)
        self.omniveyor = Omniveyor()

        for hexagon in self.omniveyor.hex_grid.hexagons:
            self.canvas.create_polygon(
                hexagon.points,
                fill="lightgreen",
                outline="black",
                activefill="red",
                tags="hexagon",
            )
            self.canvas.create_text(
                hexagon.position[0],
                hexagon.position[1],
                text=str(hexagon.id),
                tags="id",
            )
        self.canvas.grid(
            column=0, row=0, rowspan=2, padx=10, pady=10, sticky=(N, S, E, W)
        )

    def clear_manual_path(self):
        pass

    def draw_manual_path(self):
        pass


class PathFrame(ttk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
