# main mtg

import modules.servo as servo
import modules.camera as camera
import modules.scannerapi as scanner

def clean():
	camera.stop()
	servo.stop()

def move_card():
	servo.run_forward(0.85, 0.7)
	servo.run_backward(1, 0.5)
	servo.pause(0.5)

def run():
	camera.setup(True)
	servo.setup()

	for _ in range(5):
		move_card()
		servo.pause(1.5)
		scanner.add_path(camera.capture())

	scanner.scan_and_save_images()

run()
clean()