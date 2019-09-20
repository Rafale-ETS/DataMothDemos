
import json

#dump gps data formats:
import gps
from gps import DataGGA, DataRMC, DataGPS

class Data:
    def __init__(self, gps):
        self.gps = gps

rmc = DataRMC(123456, 789123, 'V', 4807.038, 'N', 1131.001, 'E', 22.4, 84.4, 3.1, 'W')
gga = DataGGA(123456, 4807.038, 'N', 1131.001, 'E', 8, 12, 0.5, 12.3, 45.6)
gps = DataGPS(gga.__dict__, rmc.__dict__)



data = Data(gps.__dict__)

f = open('docu/dataFormat.json', 'w+')
f.write(json.dumps(data.__dict__))
f.close