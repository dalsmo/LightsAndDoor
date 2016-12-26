from flask import Flask
from flask import jsonify
import time
#import RPi.GPIO as GPIO
app = Flask(__name__)

lightsPin = 18;
doorOpenPin = 19;

# single sorce of troth, read dor pins to figure out if shit is trigered or not.

#http://flask.pocoo.org/docs/0.12/quickstart/

@app.before_first_request
def _run_on_start():
    #GPIO.setup(lightsPin, GPIO.OUT)
    #GPIO.setup(doorOpenPin, GPIO.OUT) 
    #GPIO.output(lightsPin, GPIO.HIGH) # relay trigers on low
    #GPIO.output(doorOpenPin, GPIO.HIGH) # relay triggers on low
    print "GPIOs sett upp"

@app.route('/')
def index():
    s = 'this is the door and lights index page,'
    #if GPIO.input(lightsPin): # 1 means lights are off
    #    s = s + 'loghts are OFF, '
    #else:
    #    s = s + 'loghts are ON, '

    #if GPIO.input(doorOpenPin):
    #    s = s + 'door is CLOSED, '
    #else:
    #    s = s + 'door is OPEN. '

    return 'this is the door and lights index page'

###########################
@app.route('/door/open')
def open():
    # GPIO.output(doorOpenPin, GPIO.LOW)
    print("door open")
    time.sleep(15)

    # GPIO.output(doorOpenPin, GPIO.HIGH)
    print("door closed")

    return '200 status ok'

###########################
@app.route('/light/on')
def on():
    # GPIO.output(lightsPin, GPIO.LOW)
    print("lights ON")
    return '200 ok'

@app.route('/light/off')
def off():
    # GPIO.output(lightsPin, GPIO.HIGH)
    print("lights off")
    return '200 ok'

###########################
@app.route('/statusOfStuff')
def statusOfStuff():
    print("cheking staus of door and lights")
    var1 = True;
    var2 = True;
    resp = jsonify(username=var1,
                   email=var2,
                   id='just text')
    return resp



