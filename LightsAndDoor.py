from flask import Flask
from flask import jsonify
import time
import door
import lights


app = Flask(__name__)


@app.route('/')
def index():
    doorState = 'open' if door.is_open() else 'closed'
    lightState = 'on' if lights.is_on() else 'off'
    
    return 'this is the door and lights index page, lights are {lights}, door is {door}'.format(door=doorState, lights=lightState)

###########################
@app.route('/door/open')
def open():
    door.open()
    print("door open")
    time.sleep(15)

    door.close()

    return '200 status ok'

###########################
@app.route('/light/on')
def on():
    lights.on()
    print("lights ON")
    return '200 ok'

@app.route('/light/off')
def off():
    lights.off()
    print("lights off")
    return '200 ok'

###########################
@app.route('/statusOfStuff')
def statusOfStuff():
    print("cheking staus of door and lights")
    return jsonify(lights=lights.is_on(),
                   door=door.is_open())

if __name__ == '__main__':
    app.run()