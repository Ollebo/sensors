import Adafruit_DHT
import time
import json
from flask import Flask, request, render_template, url_for, redirect

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def root():
    return "Home for temp"



@app.route("/metrics", methods = ['GET'])
def metrics():
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            tempdata = "{0:0.1f}".format(temperature)
            humidata = "{0:0.1f}".format(humidity)
            premethues_data = "sensor_data_temp "+str(tempdata)+" \nsensor_data_humidity "+str(humidata)
            f = open("/midevices/devices-temp.json", "w")
            data = '"temp":"{0:0.1f}", "humidity":"{1:0.1f}"'.format(temperature, humidity)
            f.write("{"+data+"}")
            f.close()
            return premethues_data
        else:
            return "Error getting data "


@app.route("/json", methods = ['GET'])
def json():
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:

            f = open("/midevices/devices-temp.json", "w")
            data = '"temp":"{0:0.1f}", "humidity":"{1:0.1f}"'.format(temperature, humidity)
            f.write("{"+data+"}")
            f.close()
            json_data = "{"+data+"}"
            return json_data
        else:
            return "Error getting data "

@app.route("/live", methods = ['GET'])
def live():
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            return "Working"
        else:
            return "Error getting data "