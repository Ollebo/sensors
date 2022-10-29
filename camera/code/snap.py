from picamera import PiCamera
from time import sleep
import uuid
import os
import time
import json
from GPSPhoto import gpsphoto


camera = PiCamera()
from saveToDisk import writeDataToFile
from addContext import addContext

id=os.getenv('OLLEBO_ID', '12345')
imagePath=os.getenv('OLLEBO_IMAGE_PATH', '/ollebo/images')
path=os.getenv('OLLEBO_PATH', '/ollebo/data/')

filegeo= path+"/status/geo"
sleepFoor=int(os.getenv('SLEEP', 10))



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
      return False

actionfile=os.getenv('ACTIONFILE','/ollebo/status/go')
def saveData():
    '''
    Will return tru if the action file is present alse no data will be saved
    '''
    print(os.path.isfile(actionfile))
    return os.path.isfile(actionfile)

print("start camera")
camera.start_preview()
while True:
    print("Running")
    if saveData():

        dataToSend = addContext()
        dataToSend["data"] = {
                "type": "image",
                "timestamp" : int(time.time()),

        }

        imagename = imagePath+"/"+str(uuid.uuid1())+"-"+id+".jpeg"
        camera.capture(imagename)
        #Write the geo data
        #Get geo data if we have
        geoData = readStatusGEO()
        if geoData  != False:
            #we have geo data
            photo = gpsphoto.GPSPhoto()
            photo = gpsphoto.GPSPhoto(imagename)
            info = gpsphoto.GPSInfo((geoData['longitude'], geoData['latitude']),alt=geoData['height'], timeStamp='1970:01:01 09:05:05')
            photo.modGPSData(info, imagename)
            print("Adding geo data to file")

        print("camera image saved to "+imagename )
        writeDataToFile(dataToSend)
    sleep(sleepFoor)



camera.stop_preview()