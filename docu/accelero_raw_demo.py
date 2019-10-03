#apt install python3-smbus
#pip install mpu6050_raspberrypi

from mpu6050 import mpu6050

accelero = mpu6050(0x68)


while(1):
	accel_data = accelero.get_accel_data()
    temp = accelero.get_temp()
    gyro_data = accelero.get_gyro_data()
    #data = accelero.get_all_data()
	print("accel: "+accel_data)
    print(" temp: "+temp)
    print(" gyro: "+gyro_data)