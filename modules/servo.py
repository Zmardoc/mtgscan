# servo module
import time
import RPi.GPIO as GPIO

servoPin = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin,GPIO.OUT)
servo = GPIO.PWM(servoPin,50)

# measured limit of duty cycles

# 6.6 - 7.6
STOP = 7
# 1.6 > x > 6.6
FORWARD_UPPER_LIMIT = 6.6
FORWARD_BOTTOM_LIMIT = 1.6
# 7.6 < x < 13.1
BACKWARD_UPPER_LIMIT = 13.1
BACKWARD_BOTTOM_LIMIT = 7.6

def setup():
	servo.start(STOP)

def stop():
	setup()
	servo.stop()
	GPIO.cleanup()

def run(dutycycle, seconds):
	servo.ChangeDutyCycle(dutycycle)
	if seconds != 0:
		time.sleep(seconds)

# speed 0-1 (percent)
def run_forward(speed, seconds):
	dutyCycle = FORWARD_UPPER_LIMIT - (FORWARD_UPPER_LIMIT - FORWARD_BOTTOM_LIMIT) * speed
	run(dutyCycle, seconds)

def run_backward(speed, seconds):
	dutyCycle = BACKWARD_BOTTOM_LIMIT + (BACKWARD_UPPER_LIMIT - BACKWARD_BOTTOM_LIMIT) * speed
	run(dutyCycle, seconds)

def pause(seconds):
	run(STOP, seconds)