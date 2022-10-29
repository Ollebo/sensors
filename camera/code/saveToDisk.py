import uuid
import os
import json

path=os.getenv('OLLEBO_URL', '/ollebo/data')
filestaus= path+"/status/gpsstatus"
s = open(filestaus, "w")

def writeDataToFile(data):
    '''
    Lets write the data down to file so we have it
    '''
    #Lets make a uuid
    fileUuid=str(uuid.uuid1())
    filePath= path+""+fileUuid+".ollebo.json"
    dataToSend = json.dumps(data)
    f = open(filePath, "w")
    f.write(dataToSend)
    print(dataToSend)
    print("File Written")
    f.close()
    return True


def writeStatus(data):
    '''
    Lets write the data down to file so we have it
    '''
    #Lets make a uuid
    s.write(json.dumps(data))
    print("status Written")
    return True