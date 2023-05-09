import threading
import time
import cv2
from PIL import Image, ImageTk
from picamera import PiCamera
from picamera.array import PiRGBArray
import detector


class CameraStream:
    def __init__(self, label, resolution=(544, 400), framerate=30):
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
        self.update_label()

    def _update(self):
        for frame in self.camera.capture_continuous(
            self.rawCapture, format="bgr", use_video_port=True
        ):
            self.frame = frame.array
            self.rawCapture.truncate(0)

    def read(self):
        return self.frame

    def update_label(self):
        frame = self.read()
        if frame is not None:
            # Convert the frame from OpenCV to a PIL ImageTk object
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            image_tk = ImageTk.PhotoImage(image)
            processed = detector.get_contours_image(image_tk)

            # Update the label with the new image
            self.label.configure(image=processed)
            self.label.image = processed

        self.label.after(10, self.update_label)  # Schedule the next update
