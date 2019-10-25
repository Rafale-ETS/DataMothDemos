#apt install python3-smbus
#pip install mpu6050_raspberrypi

from mpu6050 import mpu6050
import timeUtil

class DataAccel:
    def __init__(self, time, x, y, z):
        self.time = time #UTC en secondes
        self.x = x
        self.y = y
        self.z = z

class DataGyro:
    def __init__(self, time, pitch, yaw, roll):
        self.time = time #UTC en secondes
        self.pitch = pitch
        self.yaw = yaw
        self.roll = roll

class DataTemperature:
    def __init__(self, time, temp):
        self.time = time
        self.temp = temp

class GyroAccel:
    def __init__(self):
        self.accelero = mpu6050(0x68)

    def getAccelData(self):
        accel_data = self.accelero.get_accel_data()
        x = accel_data.x #needs math formula
        y = accel_data.y #idem
        z = accel_data.z #idem 2
        return DataAccel(timeUtil.getTimeNowAsNMEA(), x, y, z)
    
    def getGyroData(self):
        gyro_data = self.accelero.get_gyro_data()
        pitch = gyro_data.x #needs math formula
        yaw = gyro_data.y   #idem
        roll = gyro_data.z  #idem 2
        return DataGyro(timeUtil.getTimeNowAsNMEA(), pitch, yaw, roll)

    def getTemperatureData(self):
        temp = self.accelero.get_temp()
        return DataTemperature(timeUtil.getTimeNowAsNMEA(), temp)

