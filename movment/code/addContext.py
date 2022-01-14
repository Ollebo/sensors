import datetime
import os
#
# Enhance the data for the sensor with new data
#
#
id = os.environ.get("ID", 'id1222')
hostname = os.environ.get("HOSTNAME", 'localhost')
client = os.environ.get("CLIENT", 'localhost')
device_id = os.environ.get("DEVICE_ID", 'localhost')




def addContext():
    '''
    This will add json context to the mesuerment 
    like time and other data
    '''
    data = {
          "client": client,
          "from": hostname,
          "device": {
            "id": device_id,
            "uptime": 80,
            "network": {},
            "ssid": "Skynet",
            "rssi": -62,
            "ip": "10.0.1.71"
            
          }
    }





    return data