#! only python 3.5+
#
# Made to run om the unit and start and controll the sensors and 
#
import time
import subprocess
import sys
import string
import random
import os


def generateMissionName():
    return ''.join(random.choice(string.ascii_letters) for x in range(10))

def getProject():
    return os.environ.get('PROJECT', generateMissionName() )


def startStreamer(): 
    result = subprocess.run(
        ["docker-compose", "-f","/home/pi/stream/docker-compose.yaml","start" ], capture_output=True, text=True
    )
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)

def stopStreamer(): 
    result = subprocess.run(
        ["docker-compose", "-f","/home/pi/stream/docker-compose.yaml","stop" ], capture_output=True, text=True
    )
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)



def startOlleboSensors(): 
    result = subprocess.run(
        ["docker-compose", "-f","/home/pi/ollebo/docker-compose-navio.yaml","start" ], capture_output=True, text=True
    )
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)

def stopOlleboSensors(): 
    result = subprocess.run(
        ["docker-compose", "-f","/home/pi/ollebo/docker-compose-navio.yaml","start" ], capture_output=True, text=True
    )
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)



def deleteGoFile():
    result = subprocess.run(
        ["rm", "/opt/data/status/go" ], capture_output=True, text=True
    )
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)

def makeGoFile():
    gofile = {
        "mission": generateMissionName(),
        "project": getProject()
    }
    #f = open("/opt/data/status/go", "w")
    #f.write("Now the file has more content!")
    #f.close()
    print(gofile)


#Lets start by deleting the go file
deleteGoFile()

#Lets startup the sensor 
#startOlleboSensors()

#Lets start the streamer
#startStreamer()

makeGoFile()
while True:
    print("Check if we are armed")
    time.sleep(10)