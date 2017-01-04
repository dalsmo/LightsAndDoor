from flask import Flask
from flask import jsonify
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
app = Flask(__name__)

lightsPin = 18;
doorOpenPin = 17;

# single sorce of troth, read dor pins to figure out if shit is trigered or not.

#http://flask.pocoo.org/docs/0.12/quickstart/

@app.before_first_request
def _run_on_start():
    GPIO.setup(lightsPin, GPIO.OUT)
    GPIO.setup(doorOpenPin, GPIO.OUT) 
    GPIO.output(lightsPin, GPIO.HIGH) # relay trigers on low
    GPIO.output(doorOpenPin, GPIO.HIGH) # relay triggers on low
    print "GPIOs sett upp"

@app.route('/')
def index():
    doorState = 'closed' if GPIO.input(lightsPin) else 'open'
    lightState = 'off' if GPIO.input(doorOpenPin) else 'on'
    
    return 'this is the door and lights index page, lights are {lights}, door is {door}'.format(door=doorState, lights=lightState)

###########################
@app.route('/door/open')
def open():
    GPIO.output(doorOpenPin, GPIO.LOW)
    print("door open")
    time.sleep(15)

    GPIO.output(doorOpenPin, GPIO.HIGH)
    print("door closed")

    return '200 status ok'

###########################
@app.route('/light/on')
def on():
    GPIO.output(lightsPin, GPIO.LOW)
    print("lights ON")
    return '200 ok'

@app.route('/light/off')
def off():
    GPIO.output(lightsPin, GPIO.HIGH)
    print("lights off")
    return '200 ok'

###########################
@app.route('/statusOfStuff')
def statusOfStuff():
    print("cheking staus of door and lights")
    return jsonify(lights=not GPIO.input(lightsPin),
                   door=not GPIO.input(doorOpenPin))

if __name__ == '__main__':
    app.run()