from tkinter import *
from tkinter import ttk, messagebox
from frames import TitleFrame, DisplayFrame, PathFrame
from videofeed import LabelVideoFeed
from omniveyor import Omniveyor


class App:
    def __init__(self):
        self.create_frames()
        self.draw_canvas()

    def update_video_feed(self):
        LabelVideoFeed(self.display_frame.video_label, 480, 270, 30)

    def run(self):
        self.update_video_feed()
        self.root.mainloop()

    def create_frames(self):
        self.root = Tk()
        self.root.attributes("-fullscreen", True)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.main_frame = ttk.Frame(self.root)
        self.main_frame.grid(column=0, row=0, sticky=(N, S, E, W))
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.title_frame = TitleFrame(self.main_frame)
        self.title_frame.grid(column=0, row=0, sticky=(N, S, E, W))
        self.title_frame.columnconfigure(1, weight=1)
        self.title_frame.rowconfigure(0, weight=1)
        self.title_frame.rowconfigure(1, weight=1)

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
        self.path_frame.path_checkbutton.config(command=self.activate_manual)
        self.path_frame.path_draw_button.config(command=self.draw_shortest_path)
        self.path_frame.path_move_button.config(command=self.move_path)

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

    def clear_manual_path(self):
        pass

    def draw_manual_path(self):
        pass

    def activate_manual(self):
        pass

    def draw_shortest_path(self):
        pass

    def move_path(self):
        pass


app = App()
app.run()
