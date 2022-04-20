import gps
import time
import os

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
sleepFoor=int(os.getenv('SLEEP', 10))




from saveToDisk import writeDataToFile, writeStatus
from addContext import addContext


actionfile=os.getenv('ACTIONFILE','/vstech/status/go')
def saveData():
    '''
    Will return tru if the action file is present alse no data will be saved
    '''
    return os.path.isfile(actionfile)




while True:
    try:
        report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
        print(report)
        if report['class'] == 'TPV':
            if hasattr(report, 'time'):
                dataToSend = addContext()
                
                if hasattr(report, 'lon'):

                    dataToSend["data"] = {
                      "type": "gps",
                      "timestamp" : int(time.time()),
                      "mesuretamp": str(report.time),
                      "geopoint": {"lat": report.lat ,"lon": report.lon }                      
                      #"ep" :{"epx": report.epx, "epy": report.epy, "epv": report.epv, "ept": report.ept, "eps": report.eps },
                      }
                if hasattr(report, 'alt'):
                    dataToSend["data"]["altitude"]= report.alt
                if hasattr(report, 'speed'):
                    dataToSend["data"]["speed"]= report.speed
                if hasattr(report, 'track'):
                    dataToSend["data"]["track"]= report.track


                
                if saveData():
                    print(dataToSend)
                    writeDataToFile(dataToSend)
                    writeStatus(dataToSend["data"])
                time.sleep(sleepFoor)


    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")
