import datetime
import os
import json
#
# Enhance the data for the sensor with new data
#
#
id = os.environ.get("ID", 'id1222')
hostname = os.environ.get("HOSTNAME", 'localhost')
client = os.environ.get("CLIENT", 'localhost')
device_id = os.environ.get("DEVICE_ID", 'localhost')


path=os.getenv('OLLEBO_PATH', '/ollebo/data/')
filegeo= path+"/status/geo"
filedata= path+"/status/go"


def readStatusGEO():
    '''
    Lets write the data down to file so we have it
    '''
    #Lets make a uuid
    try: 
      s = open(filegeo, "r")
      geoData = s.read()
      s.close()
      #print(geoData)
      return json.loads(geoData)
    except FileNotFoundError:
      print("no geo file")
      return {'msg':'No file'}
    

def readMission():
  '''
  Get the mission data from the data file
  '''
  try: 
    s = open(filedata, "r")
    misData = s.read()
    s.close()
    print(misData)
    return json.loads(misData)
  except FileNotFoundError:
    print("no data file")
    return {'mission':'none','project':'none'}
    

def addContext():
    '''
    This will add json context to the mesuerment 
    like time and other data
    '''

    #Get geo data
    geoData = readStatusGEO()
    geoDataIn={'msg':'No geo'}
    if 'vAcc' in geoData.keys():
       geoDataIn=geoData 
    missionData = readMission()
    data = {
          "client": client,
          "from": hostname,
          "geo": geoDataIn,
          "mission": missionData['mission'],
          "project": missionData["project"],
          "device": {
            "id": device_id,
            "uptime": 0,
            "network": {},
            "ssid": "none",
            "rssi": 0,
            "ip": "10.0.0.0"
            
          }
    }

    return data