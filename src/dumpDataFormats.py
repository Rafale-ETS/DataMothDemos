
import json

import timeUtil

#dump data formats:
from gps import DataGGA, DataRMC, DataGPS
from gyro_accel import DataAccel, DataGyro, DataTemperature
from anemo import DataWind

class Data:
    def __init__(self, gps, acc, gyr, tem, win):
        self.gps = gps
        self.acc = acc
        self.gyr = gyr
        self.tem = tem
        self.win = win

rmc = DataRMC(246060, 789123, 'V', 4807.038, 'N', 1131.001, 'E', 22.4, 84.4, 3.1, 'W')
gga = DataGGA(000000, 4807.038, 'N', 1131.001, 'E', 8, 12, 0.5, 12.3, 45.6)
gps = DataGPS(gga.__dict__, rmc.__dict__)

acc = DataAccel(timeUtil.getTimeNowAsNMEA(), 1.256, 2.456, 3.456)
gyr = DataGyro(timeUtil.getTimeNowAsNMEA(), 25, 45, 25)
tem = DataTemperature(timeUtil.getTimeNowAsNMEA(), 30)

win = DataWind(timeUtil.getTimeNowAsNMEA(), 6, 25)

data = Data(gps.__dict__, acc.__dict__, gyr.__dict__, tem.__dict__, win.__dict__)

f = open('docu/dataFormat.json', 'w+')
f.write(json.dumps(data.__dict__, indent=4))
f.close