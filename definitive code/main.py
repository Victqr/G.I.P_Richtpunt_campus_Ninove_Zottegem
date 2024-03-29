
from machine import SPI, I2C, Pin, ADC
from rfm69 import RFM69
from bme280 import BME280, BMP280_I2CADDR
import time
import machine

co2_sensor_pin = machine.ADC(26)
O3_sensor_pin = machine.ADC(27)

NAME           = "SpaceSense"
FREQ           = 433.8

ENCRYPTION_KEY = b"\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08"
NODE_ID        = 120 # ID of this node
BASESTATION_ID = 100 # ID of the node (base station) to be contacted

# Buses & Pins
spi = SPI(0, baudrate=50000, polarity=0, phase=0, firstbit=SPI.MSB)
nss = Pin( 5, Pin.OUT, value=True )
rst = Pin( 3, Pin.OUT, value=False )
i2c = I2C(0)

# RFM Module
rfm = RFM69( spi=spi, nss=nss, reset=rst )
rfm.frequency_mhz  = FREQ
rfm.encryption_key = ( ENCRYPTION_KEY )
rfm.node           = NODE_ID # This instance is the node 120
rfm.destination    = BASESTATION_ID # Send to specific node 100

bmp = BME280(i2c=i2c, address=BMP280_I2CADDR) # create a bmp object
adc = ADC(Pin(26)) # TMP36 analog pin
led = Pin(25, Pin.OUT) # Onboard LED

# Main Loop
print( 'Frequency     :', rfm.frequency_mhz )
print( 'encryption    :', rfm.encryption_key )
print( 'NODE_ID       :', NODE_ID )
print( 'BASESTATION_ID:', BASESTATION_ID )

print("iteration_count, time_sec, pressure_hpa, bmp280_temp") # print header
counter = 1 # set counter
ctime = time.time() # time now

def read_co2_level():
    sensor_value = co2_sensor_pin.read_u16()  
    co2_ppm = sensor_value / 65535 * 5000     
    return co2_ppm

def read_sensor():
    sensor_value = O3_sensor_pin.read_u16()
    ppm = sensor_value / 65535 * 3.3
    return ppm

while True:
    co2_ppm = read_co2_level()
    O3_ppm = read_sensor()
    temp, pressure, humidity =  bmp.raw_values # read BMP280: Temp, pressure (hPa), humidity
    msg = f"{counter}, {time.time()-ctime}, {pressure:.2f}, {temp:.2f}, {co2_ppm:.2f}, {O3_ppm:.2f}, {NAME}"
    print(msg)
    led.on() # Led ON while sending data
    rfm.send(bytes(msg , "utf-8"))
    led.off()
    counter += 1 # increment counter
    time.sleep(0.5) # wait before next reading
    