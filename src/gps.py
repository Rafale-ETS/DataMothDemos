

import serial

serPort = '/dev/ttyUSB0'

serCon = serial.Serial(serPort, 4800, timeout=5)

while 1:
    line = serCon.readline()
    print(line)
    #splitline = line.split(',')

    if line[0] == '$GPGGA':
        print(line)