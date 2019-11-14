
isDebug = True

def infoMPU6050(text):
    print("[mpu6050] " + text)

def infoGPS(text):
    print("[GPS] "+ text)

def error(text):
    print("[ERROR] "+ text)

def warning(text):
    print("[Warning] "+ text)

def debug(text):
    if isDebug:
        print("[Debug] "+ text)

