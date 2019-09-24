
import gps
from gps import Nmea_GPS

gps = Nmea_GPS('/dev/ttyUSB0')

gps.poolData()

