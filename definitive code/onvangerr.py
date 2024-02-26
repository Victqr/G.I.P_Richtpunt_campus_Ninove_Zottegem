from machine import SPI, Pin
from rfm69 import RFM69
import time
import csv

FREQ           = 433.1
ENCRYPTION_KEY = b"\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08"
NODE_ID        = 100 # ID of this node (BaseStation)

spi = SPI(0, polarity=0, phase=0, firstbit=SPI.MSB) # baudrate=50000,
nss = Pin( 5, Pin.OUT, value=True )
rst = Pin( 3, Pin.OUT, value=False )

led = Pin( 25, Pin.OUT )

rfm = RFM69( spi=spi, nss=nss, reset=rst )
rfm.frequency_mhz = FREQ
rfm.encryption_key = ( ENCRYPTION_KEY )
rfm.node = NODE_ID

print( 'Freq            :', rfm.frequency_mhz )
print( 'NODE            :', rfm.node )
print("Waiting for packets...")

# Open een CSV-bestand in schrijfmodus
with open('/sd/rfm_data.csv', 'w', newline='') as csvfile:
    # Definieer de velden in de CSV
    fieldnames = ['Message', 'RSSI']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # Schrijf de kopregel
    writer.writeheader()
    
    while True:
        packet = rfm.receive(timeout=0.5) # Zonder ACK
        if packet is None: # Geen pakket ontvangen
            print(".")
            pass
        else: # Een pakket ontvangen!
            led.on()
            # Decodeer van ASCII-tekst (naar lokale utf-8)
            message = str(packet, "ascii") # Dit is ons bericht
            rssi = str(rfm.last_rssi) # Signaalsterkte
            # Schrijf de gegevens naar het CSV-bestand
            writer.writerow({'Message': message, 'RSSI': rssi})
            print(message + ", " + rssi) # Bericht met signaalsterkte afdrukken
            led.off()
