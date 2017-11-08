import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

_lightsPin = 18;

GPIO.setup(_lightsPin, GPIO.OUT)
GPIO.output(_lightsPin, GPIO.HIGH) # relay trigers on low


def on():
    GPIO.output(_lightsPin, GPIO.LOW)


def off():
    GPIO.output(_lightsPin, GPIO.HIGH)

def is_on():
	return not GPIO.input(_lightsPin)