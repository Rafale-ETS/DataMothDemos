# dummy for errorchecking reason outside of py
# DON'T COPY TO PY
class dummyData:
    def __init__(self):
        self.x = 1.256
        self.y = 2.789
        self.z = 3.556

class mpu6050:
    def __init__(self, id):
        self.id = id

    def get_accel_data(self):
        return dummyData()

    def get_gyro_data(self):
        return dummyData()

    def get_temp(self):
        return 26