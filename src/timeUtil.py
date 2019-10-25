
from datetime import datetime

def getTimeNowAsNMEA():
    time = datetime.utcnow()
    nmeaTime = (time.hour * 10000) + (time.minute*100) + (time.second)
    return nmeaTime