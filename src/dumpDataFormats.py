
import json

import timeUtil, time
from database import mothDBSingle as mothDB

import printHelper

#dump data formats:
from gps import DataGGA, DataRMC, DataGPS
from gyro_accel import DataAccel, DataGyro, DataTemperature
from anemo import DataWind

fillDB = True
dumpJson = False

class Data:
    def __init__(self, gps, acc, gyr, tem, win):
        self.gps = gps
        self.acc = acc
        self.gyr = gyr
        self.tem = tem
        self.win = win

rmc = DataRMC(246060, 789123, 'V', 4807.038, 'N', 1131.001, 'E', 22.4, 84.4, 3.1, 'W')
gga = DataGGA(000000, 4807.038, 'N', 1131.001, 'E', 8, 12, 0.5, 12.3, 45.6)
gps = DataGPS(timeUtil.getTimeNowAsNMEA(), timeUtil.getDateNowAsNMEA(), 4807.038, 'N', 1131.001, 'E', 22.4, 84.4, 0.5, 12.3, 45.6)

acc = DataAccel(timeUtil.getTimeNowAsNMEA(), timeUtil.getDateNowAsNMEA(), 1.256, 2.456, 3.456)
gyr = DataGyro(timeUtil.getTimeNowAsNMEA(), timeUtil.getDateNowAsNMEA(), 25, 45, 25)
tem = DataTemperature(timeUtil.getTimeNowAsNMEA(), timeUtil.getDateNowAsNMEA(), 30)

win = DataWind(timeUtil.getTimeNowAsNMEA(), timeUtil.getDateNowAsNMEA(), 6, 25)

data = Data(gps.__dict__, acc.__dict__, gyr.__dict__, tem.__dict__, win.__dict__)

if dumpJson:
    f = open('docu/dataFormat.json', 'w+')
    f.write(json.dumps(data.__dict__, indent=4))
    f.close

if fillDB:
    dataCount = 0

    printHelper.debug("started DataDump")
    
    while(dataCount < 120): 

        printHelper.debug(str(dataCount))

        timenow = timeUtil.getTimeNowAsNMEA()
        datenow = timeUtil.getDateNowAsNMEA()
        gps.time = timenow
        gps.date = datenow
        acc.time = timenow
        acc.date = datenow
        gyr.time = timenow
        gyr.date = datenow
        tem.time = timenow
        tem.date = datenow
        win.time = timenow
        win.date = datenow

        mothDB.addGPSData(gps)
        mothDB.addACCData(acc)
        mothDB.addGYRData(gyr)
        mothDB.addTEMData(tem)
        mothDB.addWINData(win)

        dataCount += 1
