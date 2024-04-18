from machine import SPI, Pin
import sdcard
import uos
from rfm69 import RFM69
import time
import sys

# Initialize switch pin
switch_pin = Pin(20, Pin.IN)

print("-------------------------------------------------------------------")
print("Alert RFM loading")     
print("-------------------------------------------------------------------")

led = Pin(25, Pin.OUT)
ledstatusgood = Pin(18, Pin.OUT)
ledstatusbad = Pin(19, Pin.OUT)

FREQ = 433.8
ENCRYPTION_KEY = b"\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08"
NODE_ID = 100  # ID of this node (BaseStation)

spi = SPI(0, miso=Pin(4), mosi=Pin(7), sck=Pin(6), polarity=0, phase=0, firstbit=SPI.MSB)  # baudrate=50000,
nss = Pin(5, Pin.OUT, value=True)
rst = Pin(3, Pin.OUT, value=False)

rfm = RFM69(spi=spi, nss=nss, reset=rst)
rfm.frequency_mhz = FREQ
rfm.encryption_key = (ENCRYPTION_KEY)
rfm.node = NODE_ID

print("-------------------------------------------------------------------")
print("Alert SD Card loading")
print("-------------------------------------------------------------------")

spi_sd = SPI(1, baudrate=50000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB,
           sck=Pin(14, Pin.OUT),
           mosi=Pin(11, Pin.OUT), # De SPI0 TX
           miso=Pin(12, Pin.OUT)) # De SPI0 RX

# Create an instance of the SD card
sd = sdcard.SDCard(spi_sd, Pin(15))

# Mount the SD card
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

print("-------------------------------------------------------------------")
print('Freq            :', rfm.frequency_mhz)
print('NODE            :', rfm.node)

print("Waiting for packets...")
print("DEBUGING")
print("-------------------------------------------------------------------")

# Function to generate timestamp in the format YYYY-MM-DD_HH-MM-SS
def generate_timestamp():
    t = time.localtime()
    return "{:04d}-{:02d}-{:02d}_{:02d}-{:02d}-{:02d}".format(t[0], t[1], t[2], t[3], t[4], t[5])

# Generate a filename with timestamp
filename = "/sd/data_" + generate_timestamp() + ".txt"

# Open a text file in write mode
try:
    with open(filename, 'a') as data_file:
        while True:
            # Check the position of the switch
            switch_position = switch_pin.value()
            print("Switch position:", switch_position)
            
            if switch_position == 0:
                print("Switch is in position 0. Stopping script.")
                break  # Exit the loop if switch is in position 0
            
            elif switch_position == 1:
                # Receive RF packets and process them
                packet = rfm.receive(timeout=0.5)  # Without ACK
                if packet is None:  # No packet received
                    ledstatusbad.on()
                    pass
                else:  # Received a packet!
                    led.on()
                    ledstatusgood.on()
                    ledstatusbad.off()  # Turn off the bad status LED
                    message = str(packet, "ascii")  # this is our message
                    rssi = str(rfm.last_rssi)  # signal strength
                    print(message + ", " + rssi)  # print message with signal strength
                    
                    with open(filename, 'a') as data_file:
                        data_file.write(message +", " + rssi + "\n")
                    time.sleep(0.1)  # Add a small delay to stabilize LED state
                    ledstatusgood.off()
                    led.off()
                    time.sleep(0.1)  # Add a small delay to stabilize LED state

except OSError as e:
    print("Error:", e)

