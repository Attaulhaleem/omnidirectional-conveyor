from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from frames import TitleFrame, DisplayFrame, PathFrame


def get_image(file, size):
    with Image.open(file) as img:
        return ImageTk.PhotoImage(img.resize(size))


class App:
    def __init__(self):
        self.root = Tk()
        self.root.attributes("-fullscreen", True)
        # self.root.columnconfigure(0, weight=1)
        # self.root.rowconfigure(0, weight=1)
        self.configure_frames()

    def run(self):
        self.root.mainloop()

    def configure_frames(self):
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
