

import serial

class DataRMC:
    def __init__(self, time, date, status, latt, lattD, longit, longD, speedOG, trackAgl, magVar, magVarD):
        self.time = time
        self.date = date
        self.status = status
        self.latt = latt
        self.lattD = lattD
        self.longit = longit
        self.longD = longD
        self.speedOG = speedOG
        self.trackAgl = trackAgl
        self.magVar = magVar
        self.magVarD = magVarD

class DataGGA:
    def __init__(self, time, latt, lattD, longit, longD, fix, satNum, hDilution, altMSL, hautMSL):
        self.time = time
        self.latt = latt
        self.lattD = lattD
        self.longit = longit
        self.longD = longD
        self.fix = fix
        self.satNum = satNum
        self.hDilution = hDilution
        self.altMSL = altMSL
        self.hautMSL = hautMSL

class DataGPS:
    def __init__(self, DataGGA, DataRMC):
        self.gga = DataGGA
        self.rmc = DataRMC

class Nmea_GPS:

    def __init__(self):
        self.serPort = '/dev/ttyUSB0'
        self.pooling = True
        self.debug = True
        self.serCon = serial.Serial(self.serPort, 4800, timeout=5)    

    #This function will lock your software until self.pooling = False
    def poolData(self):
        while self.pooling:
            line = self.serCon.readline()
            splitline = line.decode().split(',')

            if self.debug:
                self.debugPrint(line)

            if splitline[0] == "GPGGA":
                self.extractGGA(line)
            elif splitline[0] == "GPRMC":
                self.extractRMC(line)

    def extractRMC(self, line):
        return DataRMC(line[1], line[9], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[10], line[11])

    def extractGGA(self, line):
        return DataGGA(line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[11])
        
    def debugPrint(self, line):
        print(line)

        f = open("../debugGPSData.txt", "a+")
        f.write(line)
        f.close()
