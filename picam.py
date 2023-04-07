from picamera import PiCamera
from time import sleep

camera = PiCamera()
# for upside down camera
# camera.rotation = 180

# alpha for opacity (0-255)
camera.start_preview(alpha=200)

for i in range(5):
    # sleep for at least 2 seconds (sensor adjusts to light)
    sleep(5)
    camera.capture("/home/pi/Desktop/image%s.jpg" % i)

camera.stop_preview()
