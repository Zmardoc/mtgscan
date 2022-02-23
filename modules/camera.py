# camera

from picamera import PiCamera
import RPi.GPIO as GPIO
import time

camera = PiCamera()

def setup(preview):
	camera.color_effects = (128,128)
	camera.resolution = (600,200)
	#camera.rotation = 90
	if preview:
		camera.start_preview()

def stop():
	camera.stop_preview()


def capture():
	timestamp=time.strftime("%Y%m%d%H%M%S")
	filePath = "img/"+timestamp+".jpg"
	camera.capture(filePath)
	return filePath