#!/usr/bin/env python3

from flask import Flask
from flask import request
import flask
import paho.mqtt.publish
import sys

app = Flask(__name__)

BROKER="openhab.sf"
PORT=1883

# The string length of each of these keys appears to be important
API_KEY = 'TheAPIKeyIsHere000000000000000000000000000000000'
FEED_ID = '1234567890'

def forceint(val):
    try:
        return int(val)
    except:
        return 0

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/<csv>", methods=['PUT'])
def api(csv):
    vals = [forceint(x) for x in request.data.decode('UTF-8').split(',')]
    sys.stderr.write("Logging usage: {}\n".format(vals))
    senddata(vals[0])
    reqid = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    response = flask.make_response()
    if reqid:
        response.headers['X-Request-Id'] = reqid
    return response

@app.route("/activate/<deviceid>", methods=['GET'])
def activate(deviceid):
    response = flask.Response('{},{}\r\n'.format(API_KEY, FEED_ID))
    return response

def senddata(val):
    paho.mqtt.publish.single("currentcost/power/usage", val, hostname=BROKER)

if __name__ == "__main__":
    app.run(port=80, host='0.0.0.0')
