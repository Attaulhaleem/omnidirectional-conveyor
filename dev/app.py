from tkinter import *
from tkinter import ttk, messagebox
from app_frames import TitleFrame, DisplayFrame, PathFrame
from videofeed import LabelVideoFeed
from omniveyor import Omniveyor


class App:
    def __init__(self):
        self.omniveyor = Omniveyor()
        self.create_frames()
        self.draw_canvas()

    def run(self):
        LabelVideoFeed(self.display_frame.video_label, 480, 270, 30)
        self.root.mainloop()

    def create_frames(self):
        self.root = Tk()
        self.root.attributes("-zoomed", True)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        self.title_frame = TitleFrame(self.root)
        self.title_frame.grid(column=0, row=0, sticky="ew")
        self.title_frame.columnconfigure(1, weight=1)

        self.display_frame = DisplayFrame(self.root)
        self.display_frame.grid(column=0, row=1, sticky="ew")
        # bind events to canvas
        self.display_frame.canvas.tag_bind(
            "hexagon", "<Button-1>", self.clear_manual_path
        )
        self.display_frame.canvas.tag_bind(
            "hexagon", "<B1-Motion>", self.draw_manual_path
        )
        self.display_frame.columnconfigure(0, weight=1)
        self.display_frame.columnconfigure(2, weight=1)

        self.path_frame = PathFrame(self.root, relief="raised")
        self.path_frame.grid(column=0, row=2, sticky="ew")
        # stores the current path indexes
        self.path_indexes = []
        # define variables for widget states
        self.start_pt = IntVar()
        self.end_pt = IntVar()
        self.is_manual = BooleanVar()
        self.path_text = StringVar()
        # configure button callbacks and variables
        self.path_frame.start_spinbox.config(textvariable=self.start_pt)
        self.path_frame.end_spinbox.config(textvariable=self.end_pt)
        self.path_frame.path_entry.config(textvariable=self.path_text)
        self.path_frame.mode_button.config(
            variable=self.is_manual, command=self.activate_manual
        )
        self.path_frame.draw_button.config(command=self.draw_shortest_path)
        self.path_frame.move_button.config(command=self.move_path)

    def draw_canvas(self):
        for hexagon in self.omniveyor.hexagons:
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

    def clear_manual_path(self, event):
        # delete the path
        self.display_frame.canvas.delete("spline")
        # reset old coordinates
        self.display_frame.canvas.old_coords = None
        # clear path indexes and text
        self.path_indexes.clear()
        self.path_text.set("")

    def draw_manual_path(self, event):
        # for readability
        canvas = self.display_frame.canvas
        # if manual mode not selected, do not draw path
        if not self.is_manual.get():
            return
        # find nearest hexagon's index
        index = self.omniveyor.get_nearest_index((event.x, event.y))
        # if new hexagon
        if len(self.path_indexes) == 0 or self.path_indexes[-1] != index:
            # add to path
            self.path_indexes.append(index)
            # convert to string for displaying
            self.path_text.set(" -> ".join(map(str, self.path_indexes)))
        # store the new point
        (x, y) = self.omniveyor.hexagons[index].position
        # if more than one points have been traced
        if canvas.old_coords is not None:
            # retrieve last point
            (x1, y1) = canvas.old_coords
            # create line between old and new point
            canvas.create_line(
                x, y, x1, y1, width=3, smooth=1, tags="spline", arrow="first"
            )
        # new point becomes old point
        canvas.old_coords = (x, y)

    def activate_manual(self):
        # for readability
        canvas = self.display_frame.canvas
        move_button = self.path_frame.move_button
        draw_button = self.path_frame.draw_button
        start_spinbox = self.path_frame.start_spinbox
        end_spinbox = self.path_frame.end_spinbox
        # if manual mode
        if self.is_manual.get():
            new_state = ["disabled"]
            # enable move button
            move_button.state(["!disabled"])
        # otherwise
        else:
            new_state = ["!disabled"]
            # disable move button
            move_button.state(["disabled"])
        # enable spinboxes and buttons if not manual, else disable
        start_spinbox.state(new_state)
        end_spinbox.state(new_state)
        draw_button.state(new_state)
        # clear path
        self.path_indexes.clear()
        self.path_text.set("")
        # delete any old path
        canvas.delete("lines")
        canvas.delete("spline")
        # reset old coordinates
        canvas.old_coords = None

    def draw_shortest_path(self):
        # for readability
        canvas = self.display_frame.canvas
        move_button = self.path_frame.move_button
        # delete previously drawn path
        canvas.delete("lines")
        # path not drawn yet, disable move button
        move_button.state(["disabled"])
        # show error message if start and end pts are same
        if self.start_pt.get() == self.end_pt.get():
            self.path_text.set("")
            messagebox.showerror("Error", "Start and end points cannot be the same!")
            return
        # find path from start to end pt
        path_list = self.omniveyor.get_path_indexes(
            self.start_pt.get(), self.end_pt.get()
        )
        # convert to string for displaying
        self.path_text.set(" -> ".join(map(str, path_list)))
        # get hexagon center positions
        path_positions = [
            val for i in path_list for val in self.omniveyor.hexagons[i].position
        ]
        # draw lines through hexagon centers
        canvas.create_line(
            path_positions, arrow="last", capstyle="round", tags="lines", width=3
        )
        # path is now drawn, enable move button
        move_button.state(["!disabled"])

    def move_path(self):
        self.omniveyor.actuate()


if __name__ == "__main__":
    App().run()
