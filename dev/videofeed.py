import cv2
from tkinter import *
from PIL import Image, ImageTk


class LabelVideoFeed:
    def __init__(self, label, width, height, fps):
        self.vs = cv2.VideoCapture(0)
        self.current_image = None
        self.label = label
        self.width = width
        self.height = height
        self.fps = fps
        self.video_loop()

    def video_loop(self):
        ok, frame = self.vs.read()
        if ok:
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            self.current_image = Image.fromarray(cv2image)
            self.current_image = self.current_image.resize((self.width, self.height))
            imgtk = ImageTk.PhotoImage(image=self.current_image)
            self.label.configure(image=imgtk)
            self.label.image = imgtk
        self.label.after(int(1000 / self.fps), self.video_loop)
