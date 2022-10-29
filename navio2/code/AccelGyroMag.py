"""

"""

import spidev
import time
import argparse 
import sys
import navio.mpu9250
import navio.util
import os
import datetime




from addContext import addContext
from saveToDisk import writeDataToFile


imu = navio.lsm9ds1.LSM9DS1()
imu.initialize()

sleepFoor=int(os.getenv('SLEEP', 10))
actionfile=os.getenv('ACTIONFILE','/ollebo/data/status/go')
def saveData():
    '''
    Will return tru if the action file is present alse no data will be saved
    '''
    return os.path.isfile(actionfile)



time.sleep(1)

while True:

	imu.read_temp()
	m9a, m9g, m9m = imu.getMotion9()
	dataToSend = addContext()
	dataToSend["data"] = {
          "timestamp": int(time.time()),
          "mesuretime": str(datetime.datetime.now()),
          "type": "movement",
          "acc_x":"{:+7.3f}".format(m9a[0]),
          "acc_y":"{:+7.3f}".format(m9a[1]),
          "acc_z":"{:+7.3f}".format(m9a[2]),
          "gyro_x": "{:+8.3f}".format(m9g[0]),
          "gyro_y": "{:+8.3f}".format(m9g[1]),
          "gyro_z": "{:+8.3f}".format(m9g[2]),
          "mag_x": "{:+7.3f}".format(m9m[0]),
          "mag_y": "{:+7.3f}".format(m9m[1]),
          "mag_z": "{:+7.3f}".format(m9m[2]),
		  "temp": imu.temperature

          } 

	print(dataToSend)
	if saveData():
		writeDataToFile(dataToSend)
	time.sleep(sleepFoor)
