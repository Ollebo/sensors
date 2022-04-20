from picamera import PiCamera
from time import sleep
import uuid
import os
import time


camera = PiCamera()
from saveToDisk import writeDataToFile
from addContext import addContext

id=os.getenv('VSTECH_ID', '12345')
imagePath=os.getenv('VSTECH_IMAGE_PATH', '/vstech/images')
sleepFoor=int(os.getenv('SLEEP', 10))


actionfile=os.getenv('ACTIONFILE','/vstech/status/go')
def saveData():
    '''
    Will return tru if the action file is present alse no data will be saved
    '''
    return os.path.isfile(actionfile)

camera.start_preview()
while True:
    if saveData():

        dataToSend = addContext()
        dataToSend["data"] = {
                "type": "image",
                "timestamp" : int(time.time()),

        }
        imagename = imagePath+"/"+str(uuid.uuid1())+"-"+id+".jpeg"
        camera.capture(imagename)
        print("camera image saved to "+imagename )
        writeDataToFile(dataToSend)
    sleep(sleepFoor)



camera.stop_preview()