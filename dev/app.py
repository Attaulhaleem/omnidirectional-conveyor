from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from frames import TitleFrame, DisplayFrame, PathFrame

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


def get_image(file, size):
    with Image.open(ASSETS_PATH + file) as img:
        return ImageTk.PhotoImage(img.resize(size))


class App:
    def __init__(self):
        self.root = Tk()
        self.root.attributes("-fullscreen", True)
        # self.root.columnconfigure(0, weight=1)
        # self.root.rowconfigure(0, weight=1)
        self.create_frames()

    def run(self):
        self.root.mainloop()

    def create_frames(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.grid(column=0, row=0, rowspan=3, sticky=(N, S, E, W))

        self.title_frame = TitleFrame(self.main_frame)
        self.title_frame.grid(column=0, row=0, sticky=(N, S, E, W))

        self.display_frame = DisplayFrame(self.main_frame, relief="sunken")
        self.display_frame.grid(column=0, row=1, sticky=(N, S, E, W))

        self.path_frame = PathFrame(self.main_frame, relief="raised")
        self.path_frame.grid(column=0, row=2, sticky=(N, S, E, W))


app = App()
app.run()
