from machine import SPI, Pin
import sdcard
import uos
from rfm69 import RFM69



FREQ           = 433.8
ENCRYPTION_KEY = b"\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08"
NODE_ID        = 100 # ID of this node (BaseStation)

spi = SPI(0, polarity=0, phase=0, firstbit=SPI.MSB) # baudrate=50000,
nss = Pin( 5, Pin.OUT, value=True )
rst = Pin( 3, Pin.OUT, value=False )
led = Pin(25, Pin.OUT)

rfm = RFM69( spi=spi, nss=nss, reset=rst )
rfm.frequency_mhz = FREQ
rfm.encryption_key = ( ENCRYPTION_KEY )
rfm.node = NODE_ID

###############################################################################################################################
##############                  FOUT IN DE SPI HIJ STAAT OP SPI0 MAAR DAT IS VOOR DE RFM MODULE                  ##############
###############################################################################################################################
# Configure SPI for SD card
# spi_sd = SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB,
#            sck=Pin(18, Pin.OUT),
#            mosi=Pin(19, Pin.OUT), # De SPI0 TX
#            miso=Pin(16, Pin.OUT)) # De SPI0 RX

# Create an instance of the SD card
# sd = sdcard.SDCard(spi_sd, Pin(17))

# # Mount the SD card
# vfs = uos.VfsFat(sd)
# uos.mount(vfs, "/sd")
###############################################################################################################################
##############                  FOUT IN DE SPI HIJ STAAT OP SPI0 MAAR DAT IS VOOR DE RFM MODULE                  ##############
###############################################################################################################################



###############################################################################################################################
##############                                    JUISTE DEEL SPI STAAT OP SPI1                                  ##############
###############################################################################################################################
spi_sd = SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB,
           sck=Pin(14, Pin.OUT),
           mosi=Pin(11, Pin.OUT), # De SPI0 TX
           miso=Pin(12, Pin.OUT)) # De SPI0 RX

# Create an instance of the SD card
sd = sdcard.SDCard(spi_sd, Pin(15))

# Mount the SD card
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")
###############################################################################################################################
##############                                    JUISTE DEEL SPI STAAT OP SPI1                                  ##############
###############################################################################################################################
print( 'Freq            :', rfm.frequency_mhz )
print( 'NODE            :', rfm.node )

print("Waiting for packets...")


# Open a text file in write mode


try:
    with open('/sd/data.txt', 'w') as data_file:
        while True:
            packet = rfm.receive( timeout=0.5 ) # Without ACK
            if packet is None: # No packet received
                print( "." )
                pass
            else: # Received a packet!
                led.on()
                message = str(packet, "ascii") # this is our message
                rssi = str(rfm.last_rssi) # signal strength
                print(message + ", " + rssi) # print message with signal strength
                data_file.write(message + ", " + rssi + "\n")  # Add a newline
                led.off()
except OSError as e:
    print("Error:", e)


