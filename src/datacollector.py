
from gps import Nmea_GPS
from gyro_accel import GyroAccel
from anemo import Anemo
from database import mothDBSingle as mothDB

gpsDevice = Nmea_GPS('/dev/ttyUSB0')
gyrAccDevice = GyroAccel()
windDevice = Anemo()

#TODO: spawn threads for async devices data collection

while(1):
    #TODO: think up workings
    print("TODO")
    break
