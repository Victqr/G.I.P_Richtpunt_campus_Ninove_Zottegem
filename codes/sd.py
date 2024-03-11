import sdcard
import uos
import os
from machine import SPI, Pin

# Configure SPI for SD card
spi_sd = SPI(1, baudrate=1000000, polarity=0, phase=0, bits=8, firstbit=SPI.MSB,
             sck=Pin(14, Pin.OUT),
             mosi=Pin(11, Pin.OUT),  # De SPI0 TX
             miso=Pin(12, Pin.OUT))  # De SPI0 RX

# Create an instance of the SD card
sd = sdcard.SDCard(spi_sd, Pin(15))

# Mount the SD card
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

# Function to generate timestamp in the format YYYY-MM-DD_HH-MM-SS
def generate_timestamp():
    t = time.localtime()
    return "{:04d}-{:02d}-{:02d}_{:02d}-{:02d}-{:02d}".format(t[0], t[1], t[2], t[3], t[4], t[5])

# Generate a filename with timestamp
filename = "/sd/data_" + generate_timestamp() + ".txt"

# Writing header to the new file
with open(filename, 'a') as data_file:
    data_file.write("iteration_count, pressure_hpa, bmp280_temp, CO2, O3, Node\n")
