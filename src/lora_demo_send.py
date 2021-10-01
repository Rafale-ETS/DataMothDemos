from lora_lib import LoRaE5, Modes, Regions

le5 = LoRaE5('com6', Regions.america, Modes.transmit, None)

le5.sendString("Hello World!")
le5.sendString("This is Rafale3!")
le5.sendString("...")
le5.sendString("...")
le5.sendString("We are ready to do NOTHING AT ALL!!")

le5.serCon.close()