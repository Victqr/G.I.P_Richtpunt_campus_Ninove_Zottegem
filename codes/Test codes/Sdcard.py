import sdcard
import uos
from machine import Pin, SPI

# Maak een chip select (CS) pin (en start het HIGH)
cs = machine.Pin(17, machine.Pin.OUT)

# Intialiseer SPI peripheral 0 (start met 1 MHz)
spi = SPI(0, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=machine.SPI.MSB,
           sck=machine.Pin(18, machine.Pin.OUT),
           mosi=machine.Pin(19, machine.Pin.OUT), # De SPI0 TX
           miso=machine.Pin(16, machine.Pin.OUT)) # De SPI0 RX

# Creeer een SDCard object sd met de spi en cs:
sd = sdcard.SDCard(spi, cs)

# We openen de SD kaart en koppelen aan directory /sd
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

# we schrijven de directory van de SD kaart uit in REPL
files = uos.listdir('/sd')
print("SD-kaart bestanden:", files)

# we wijzigen uos naar directory /sd
uos.chdir('/sd')

# Controleer of counter.txt aanwezig is
counter = 1
if "counter.txt" in files:
    # open het en lees de teller uit (read = 'r')
    print("counter found")
    with open('/sd/counter.txt', "r") as countfile:
        try:
            counter = int(countfile.readline().strip())
            print(counter)
        except ValueError:
            print("Invalid content in counter.txt, resetting counter to 1")
            counter = 1

    # we tellen 1 bij de teller en slaan op voor volgende keer (write = 'w')
    with open('/sd/counter.txt', "w") as countfile:
        countfile.write(str(counter + 1)) #schrijf teller
        countfile.write('\n') # Een nieuwe lijn op einde
else:
    # counter.txt bestaat niet, dus maak het met inhoud 1
    with open('/sd/counter.txt', "w") as countfile:
        print("Maken counter.txt aan!")
        countfile.write(str(counter)) # de teller als string
        countfile.write('\n') # een nieuwe lijn
