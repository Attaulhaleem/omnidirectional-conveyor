from tkinter import *
from tkinter import ttk, messagebox
from frames import TitleFrame, DisplayFrame, PathFrame
from videofeed import LabelVideoFeed
from omniveyor import Omniveyor


class App:
    def __init__(self):
        self.root = Tk()
        self.root.attributes("-fullscreen", True)
        self.create_frames()
        self.draw_canvas()
        self.update_video_feed()

    def run(self):
        self.root.mainloop()

    def create_frames(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.grid(column=0, row=0, rowspan=3, sticky=(N, S, E, W))

        self.title_frame = TitleFrame(self.main_frame)
        self.title_frame.grid(column=0, row=0, sticky=(N, S, E, W))

        self.display_frame = DisplayFrame(self.main_frame, relief="sunken")
        self.display_frame.grid(column=0, row=1, sticky=(N, S, E, W))
        self.display_frame.canvas.tag_bind(
            "hexagon", "<Button-1>", self.clear_manual_path
        )
        self.display_frame.canvas.tag_bind(
            "hexagon", "<B1-Motion>", self.draw_manual_path
        )

        self.path_frame = PathFrame(self.main_frame, relief="raised")
        self.path_frame.grid(column=0, row=2, sticky=(N, S, E, W))

    def clear_manual_path(self):
        pass

    def draw_manual_path(self):
        pass

    def draw_canvas(self):
        self.omniveyor = Omniveyor()
        for hexagon in self.omniveyor.hex_grid.hexagons:
            self.display_frame.canvas.create_polygon(
                hexagon.points,
                fill="lightgreen",
                outline="black",
                activefill="red",
                tags="hexagon",
            )
            self.display_frame.canvas.create_text(
                hexagon.position[0],
                hexagon.position[1],
                text=str(hexagon.id),
                tags="id",
            )

    def update_video_feed(self):
        LabelVideoFeed(self.display_frame.video_label, 480, 270, 30)


app = App()
app.run()
