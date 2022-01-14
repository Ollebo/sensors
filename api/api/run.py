#
#
#
# File to start
#
# Lissen for events from the que
#!/usr/bin/env python

import time
import json
from flask import Flask, request, render_template, url_for, redirect

import redis

r = redis.Redis(
    host='redis')
app = Flask(__name__)


@app.route("/orien", methods = ['GET'])
def orien():
		value = r.get('Orien')
		print(value)
		return "Get along nothing to {0}".format(value)

@app.route("/accel", methods = ['GET'])
def accel():
		value = r.get('Acceleration')
		print(value)
		return "Get along nothing to {0}".format(value)

@app.route("/gyro", methods = ['GET'])
def gyro():
		value = r.get('Gyroscope')
		print(value)
		return "Get along nothing to {0}".format(value)

@app.route("/mag", methods = ['GET'])
def mag():
		value = r.get('Magnetic')
		print(value)
		return "Get along nothing to {0}".format(value)