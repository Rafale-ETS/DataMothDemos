from lora_lib import LoRaE5, Modes, Regions

def printHexAsString(response):
    try:
        hex = response.split(b' ')[2].split(b'\r')[0].split(b'"')[1]
        print(bytes.fromhex(hex.decode('utf-8')).decode('utf-8'))
        
    except IndexError:
        pass

le5 = LoRaE5('com7', Regions.america, Modes.recieve, printHexAsString)
le5.serCon.close()
