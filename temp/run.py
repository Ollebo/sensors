import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4






while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        f = open("/midevices/devices-temp.json", "w")
        data = '"temp":"{0:0.1f}", "humidity":"{1:0.1f}"'.format(temperature, humidity)
        f.write("{"+data+"}")
        f.close()
        time.sleep(4)
    else:
        print("Failed to retrieve data from humidity sensor")
