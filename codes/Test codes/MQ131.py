import machine
import time

# Definieer de pin waarop de sensor is aangesloten
co2_sensor_pin = machine.ADC(26)  # Verander 26 naar de pin die je gebruikt

def read_co2_level():
    # Lees de analoge waarde van de sensor
    sensor_value = co2_sensor_pin.read_u16()

    # Converteer de ruwe sensorwaarde naar ppm (parts per million) voor CO2
    # De exacte conversie hangt af van de specificaties van de sensor
    # Dit is een algemene benadering en kan worden aangepast aan de specificaties van je sensor
    co2_ppm = sensor_value / 65535 * 5000  # 0-5000 ppm
    
    return co2_ppm

def main():
    while True:
        # Lees de CO2-waarde
        co2_ppm = read_co2_level()
        
        # Druk de CO2-waarde af
        print("CO2 Concentration (ppm): {:.2f}".format(co2_ppm))
        
        # Wacht een paar seconden voordat de sensor opnieuw wordt gelezen
        time.sleep(2)

if __name__ == "__main__":
    main()

