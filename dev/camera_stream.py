import threading
import time
import cv2
from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
from picamera import PiCamera
from picamera.array import PiRGBArray


class CameraStream:
    def __init__(self, label, resolution=(640, 480), framerate=30):
        self.label = label
        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        self.rawCapture = PiRGBArray(self.camera, size=resolution)
        time.sleep(0.1)  # Allow the camera to warm up

        self.frame = None
        self.thread = threading.Thread(target=self._update, args=())
        self.thread.daemon = True
        self.thread.start()

    def _update(self):
        for frame in self.camera.capture_continuous(
            self.rawCapture, format="bgr", use_video_port=True
        ):
            self.frame = frame.array
            self.rawCapture.truncate(0)

    def read(self):
        return self.frame

    def update_label(self):
        frame = self.camera_stream.read()
        if frame is not None:
            # Convert the frame from OpenCV to a PIL ImageTk object
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            image_tk = ImageTk.PhotoImage(image)

            # Update the label with the new image
            self.label.configure(image=image_tk)
            self.label.image = image_tk

        self.label.after(10, self.update_video)  # Schedule the next update


# class App:
#     def __init__(self, master):
#         self.master = master
#         self.camera_stream = CameraStream()

#         self.label = tk.Label(master)
#         self.label.pack()

#         self.update_label()

#     def update_label(self):
#         frame = self.camera_stream.read()
#         if frame is not None:
#             # Convert the frame from OpenCV to a PIL ImageTk object
#             image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#             image_tk = ImageTk.PhotoImage(image)

#             # Update the label with the new image
#             self.label.configure(image=image_tk)
#             self.label.image = image_tk

#         self.master.after(10, self.update_label)  # Schedule the next update


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()
