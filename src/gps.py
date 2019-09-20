

import serial

serPort = '/dev/ttyUSB0'

serCon = serial.Serial(serPort, 4800, timeout=5)

while 1:
    line = serCon.readline()
    splitline = line.decode().split(',')

    if splitline[0] == '$GPGGA':
        latt = line[2]
        latDirec = line[3]
        longit = line[4]
        longDirec = line[5]
        print("lattitude: "+str(latt)+" lattDirect: "+str(latDirec)+" longitude: "+str(longit)+" longDirect: "+str(longDirec))