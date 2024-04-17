from machine import SPI, I2C, Pin, ADC, PWM
from rfm69 import RFM69
from bme280 import BME280, BMP280_I2CADDR
import time
import machine
import sdcard
import uos
import os
from utime import sleep

co2_sensor_pin = machine.ADC(27)
O3_sensor_pin = machine.ADC(26)
buzzer = Pin(28, Pin.OUT)
buzzer.value(0)


NAME = "SpaceSense"
FREQ = 433.8

ENCRYPTION_KEY = b"\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08"
NODE_ID = 120  # ID of this node
BASESTATION_ID = 100  # ID of the node (base station) to be contacted

# Buses & Pins
spi = SPI(0, baudrate=50000, polarity=0, phase=0, firstbit=SPI.MSB)
nss = Pin(5, Pin.OUT, value=True)
rst = Pin(3, Pin.OUT, value=False)
i2c = I2C(0)

# RFM Module
rfm = RFM69(spi=spi, nss=nss, reset=rst)
rfm.frequency_mhz = FREQ
rfm.encryption_key = (ENCRYPTION_KEY)
rfm.node = NODE_ID  # This instance is the node 120
rfm.destination = BASESTATION_ID  # Send to specific node 100

bmp = BME280(i2c=i2c, address=BMP280_I2CADDR)  # create a bmp object
adc = ADC(Pin(26))  # TMP36 analog pin
led = Pin(25, Pin.OUT)  # Onboard LED

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

# Main Loop
print('Frequency     :', rfm.frequency_mhz)
print('encryption    :', rfm.encryption_key)
print('NODE_ID       :', NODE_ID)
print('BASESTATION_ID:', BASESTATION_ID)

counter = 1  # set counter

def read_co2_level():
    sensor_value = co2_sensor_pin.read_u16()
    co2_ppm = sensor_value / 65535 * 3300
    print(sensor_value)
    return sensor_value

def read_sensor():
    sensor_value2 = O3_sensor_pin.read_u16()
    ppm = sensor_value2 / 65535 * 3300
    print(sensor_value2)
    return sensor_value2

def calculate_altitude(sea_level_pressure, measured_pressure):
    # Bereken het hoogteverschil op basis van de barometrische formule
    altitude = 44330 * (1 - (measured_pressure / sea_level_pressure) ** (1 / 5.255))
    return altitude

# Bekende atmosferische druk op zeeniveau (in hPa)
sea_level_pressure = 1009.1

while True:
    co2_ppm = read_co2_level()
    O3_ppm = read_sensor()
    temp, pressure, humidity = bmp.raw_values  # lees BMP280: Temp, druk (hPa), luchtvochtigheid

    # Bereken de hoogte met behulp van de bekende atmosferische druk op zeeniveau
    altitude = calculate_altitude(sea_level_pressure, pressure)

    # Toevoegen van sensorwaarden aan de berichtstring
    msg = f"{altitude:.2f}, {pressure:.2f}, {temp:.2f}, {co2_ppm:.2f}, {O3_ppm:.2f}, 123"
    print(msg)

    # Schrijf de gegevens naar het nieuwe bestand
    with open(filename, 'a') as data_file:
        data_file.write(msg + "\n")

    led.on()  # Led AAN tijdens het verzenden van gegevens
    rfm.send(bytes(msg, "utf-8"))
    led.off()
    counter += 1  # Tel de iteraties op
    time.sleep(0.5)  # Wacht voor de volgende meting




