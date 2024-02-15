import machine
import time

# Definieer de pin waarop de sensor is aangesloten
sensor_pin = machine.ADC(27)

def read_sensor():
    # Lees de analoge waarde van de sensor
    sensor_value = sensor_pin.read_u16()

    # Converteer de ruwe sensorwaarde naar ppm
    ppm = sensor_value / 65535 * 3.3

    return ppm

def main():
    while True:
        # Lees de sensorwaarde
        ppm = read_sensor()
        
        # Druk de ppm-waarde af
        print("Concentration O3 (ppm): {:.2f}".format(ppm))
        
        # Wacht een paar seconden voordat de sensor opnieuw wordt gelezen
        time.sleep(2)

if __name__ == "__main__":
    main()

