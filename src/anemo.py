
import timeUtil

class DataWind:
    def __init__(self, time, speed, direc):
        self.time = time
        self.speed = speed
        self.direc = direc

class Anemo:
    def __init__(self):
        self.serial = None

    def getWindData(self):
        #TODO: get data from sensors
        return DataWind(timeUtil.getTimeNowAsNMEA(), 0, 0) #TODO: change for actual data