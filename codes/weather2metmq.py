from machine import SPI, I2C, Pin, ADC
from rfm69 import RFM69
from bme280 import BME280, BMP280_I2CADDR
from math import exp, log
from BaseMQ import BaseMQ
import utime
import time

class MQ5(BaseMQ):  # MQ5 erft van de BaseMQ-klasse
    MQ5_RO_BASE = const(6.0)  # Aangepaste waarde voor MQ5

    def __init__(self, pinData, pinHeater=-1, boardResistance=10, baseVoltage=3.3, measuringStrategy=BaseMQ.STRATEGY_ACCURATE):
        super().__init__(pinData, pinHeater, boardResistance, baseVoltage, measuringStrategy)

    def getRoInCleanAir(self):
        return self.MQ5_RO_BASE

    def readLPG(self):
        lpg = self.readScaled(-0.45, 2.95)
        return lpg

    def readMethane(self):
        methane = self.readScaled(-0.38, 3.21)
        return methane

# Voorbeeldgebruik
pin = 26
mq5_sensor = MQ5(pinData=pin, baseVoltage=3.3)

print("Calibrating MQ5...")
mq5_sensor.calibrate()
print("Calibration completed. Base resistance: {0}".format(mq5_sensor._ro))

# Buses & Pins
spi = SPI(0, baudrate=50000, polarity=0, phase=0, firstbit=SPI.MSB)
nss = Pin(5, Pin.OUT, value=True)
rst = Pin(3, Pin.OUT, value=False)
i2c = I2C(0)

# RFM Module
rfm = RFM69(spi=spi, nss=nss, reset=rst)
rfm.frequency_mhz = 433.8
rfm.encryption_key = b"\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08"
rfm.node = 120
rfm.destination = 100

bmp = BME280(i2c=i2c, address=BMP280_I2CADDR)  # create a bmp object
led = Pin(25, Pin.OUT)  # Onboard LED
adcpin = 27
tmp36 = ADC(adcpin)

# Main Loop
print('Frequency     :', rfm.frequency_mhz)
print('encryption    :', rfm.encryption_key)
print('NODE_ID       :', rfm.node)
print('BASESTATION_ID:', rfm.destination)

print("iteration_count, time_sec, pressure_hpa, bmp280_temp, mq5_lpg, mq5_methane")  # print header
counter = 1  # set counter
ctime = time.time()  # time now

while True:
    adc_value = tmp36.read_u16()
    volt = (3.3/65535)*adc_value
    degC = (100*volt)-50
    print(round(degC, 1))
    temp, pressure, humidity = bmp.raw_values  # read BMP280: Temp, pressure (hPa), humidity
    mq5_lpg = mq5_sensor.readLPG()
    mq5_methane = mq5_sensor.readMethane()
    msg = f"c: {counter}, p: {pressure:.2f}, t: {temp:.2f}, t: {degC} l: {mq5_lpg:.2f}, m: {mq5_methane:.2f}, Spacesence"
    print(msg)
    led.on()  # Led ON while sending data
    rfm.send(bytes(msg, "utf-8"))
    led.off()
    counter += 1  # increment counter



