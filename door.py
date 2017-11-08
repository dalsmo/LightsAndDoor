import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

_doorOpenPin = 17;

GPIO.setup(_doorOpenPin, GPIO.OUT) 
GPIO.output(_doorOpenPin, GPIO.HIGH) # relay triggers on low


def open():
	GPIO.output(_doorOpenPin, GPIO.LOW)


def close():
	GPIO.output(_doorOpenPin, GPIO.HIGH)


def is_open():
	return not GPIO.input(doorOpenPin)