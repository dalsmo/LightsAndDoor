from flask import Flask
from flask import jsonify
import threading
import door
import lights


app = Flask(__name__)


def door_timer_callback():
    door.close()
    print("Door CLOSED")

door_timer = threading.Timer(15, door_timer_callback)


@app.route('/')
def index():
    doorState = 'open' if door.is_open() else 'closed'
    lightState = 'on' if lights.is_on() else 'off'
    
    return 'This is the door and lights index page, lights are {lights}, door is {door}.'.format(door=doorState, lights=lightState)


@app.route('/door/open')
def open():
    door.open()
    print("Door OPEN")

    door_timer.cancel()
    door_timer.start()

    return '200 status ok'


@app.route('/light/on')
def on():
    lights.on()
    print("Lights ON")
    return '200 ok'


@app.route('/light/off')
def off():
    lights.off()
    print("Lights OFF")
    return '200 ok'


@app.route('/statusOfStuff')
def statusOfStuff():
    print("Checking status of door and lights")
    return jsonify(lights=lights.is_on(),
                   door=door.is_open())


if __name__ == '__main__':
    app.run()