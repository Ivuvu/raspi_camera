import time
import picamera

with picamera.PiCamera() as camera:
	camera.resolution = (1024,768)
	camera.start_preview()
	# camera warm-up time
	time.sleep(2)
	camera.capture('sample.jpg')


