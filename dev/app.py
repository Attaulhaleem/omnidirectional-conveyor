from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from omniveyor import Omniveyor


class App:
    def __init__(self, master: Tk):
        self.master = master
        self.master.attributes("-fullscreen", True)
        # self.master.columnconfigure(0, weight=1)
        # self.master.rowconfigure(0, weight=1)
        self.omniveyor = Omniveyor()

        self.set_constants()
        self.load_images()
        self.config_sub_frames()
        self.config_title_frame()
        self.config_display_frame()
        self.config_path_frame()

    def set_constants(self):
        self.ASSETS = "app/assets/"
        self.TITLE_FONT = ("TkHeadingFont", 35)
        self.SUBTITLE_FONT = ("TkTextFont", 18)
        self.HEADING_FONT = ("TkHeadingFont", 14)
        self.BODY_FONT = ("TkTextFont", 10)
        self.TITLE_ICON_SIZE = (200, 160)
        self.HEADING_ICON_SIZE = (50, 50)
        self.BUTTON_ICON_SIZE = (30, 30)
        self.FRAME_STYLE = "Normal.TFrame"
        ttk.Style().configure("Normal.TFrame", padding=5)

    def get_image(self, file, size):
        img = Image.open(self.ASSETS + file)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)

    def load_images(self):
        self.title_image = self.get_image("conveyor.png", self.TITLE_ICON_SIZE)

    def config_sub_frames(self):
        self.main_frame = ttk.Frame(self.master, style=self.FRAME_STYLE, padding=10)
        self.main_frame.grid(column=0, row=0, rowspan=3, sticky=(N, S, E, W))
        # self.main_frame.columnconfigure(0, weight=1)
        # self.main_frame.rowconfigure(0, weight=1)

        self.title_frame = ttk.Frame(self.main_frame, style=self.FRAME_STYLE)
        self.title_frame.grid(column=0, row=0, sticky=(N, S, E, W))
        # self.title_frame.columnconfigure(1, weight=1)
        # self.title_frame.rowconfigure(0, weight=1)
        # self.title_frame.rowconfigure(1, weight=1)

        self.display_frame = ttk.Frame(
            self.main_frame, style=self.FRAME_STYLE, relief="raised"
        )
        self.display_frame.grid(column=0, row=1, sticky=(N, S, E, W))

        self.path_frame = ttk.Frame(
            self.main_frame, style=self.FRAME_STYLE, relief="sunken"
        )
        self.path_frame.grid(column=0, row=2, sticky=(N, S, E, W))

    def config_title_frame(self):
        # title image
        ttk.Label(self.title_frame, anchor="w", image=self.title_image).grid(
            column=0, row=0, rowspan=2, sticky=(N, S, E, W)
        )
        # title text
        ttk.Label(
            self.title_frame,
            text="Omniveyor GUI",
            font=self.TITLE_FONT,
            anchor="center",
        ).grid(column=1, row=0, sticky=(N, S, E, W))
        # subtitle text
        ttk.Label(
            self.title_frame,
            text="By Atta, Inshal, Mustafa & Shaheer",
            font=self.SUBTITLE_FONT,
            anchor="center",
        ).grid(column=1, row=1, sticky=(N, S, E, W))

    def config_display_frame(self):
        self.canvas = Canvas(
            self.display_frame, highlightthickness=1, highlightbackground="black"
        )
        self.canvas.old_coords = None
        self.canvas.tag_bind("hexagon", "<Button-1>", self.clear_manual_path)
        self.canvas.tag_bind("hexagon", "<B1-Motion>", self.draw_manual_path)

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

    def config_path_frame(self):
        pass

    def clear_manual_path(self):
        pass

    def draw_manual_path(self):
        pass


root = Tk()
app = App(root)
root.mainloop()
