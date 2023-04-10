import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class VideoFeed:
    def __init__(self):
        self.vs = cv2.VideoCapture(0)
        self.current_image = None
        self.root = Tk()
        self.frame = ttk.Frame(self.root)
        self.label = ttk.Label(self.frame)
        self.frame.grid(column=0, row=0)
        self.label.grid(column=0, row=0)
        self.video_loop()
        self.root.mainloop()

    def video_loop(self):
        ok, frame = self.vs.read()
        if ok:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            self.current_image = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=self.current_image)
            self.label.configure(image=imgtk)
            self.label.image = imgtk
        self.root.after(30, self.video_loop)


VideoFeed()
