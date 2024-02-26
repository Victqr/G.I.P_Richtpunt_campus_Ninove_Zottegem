import machine
import time

# Define the pin to which the sensor is connected
co2_sensor_pin = machine.ADC(26)  # Change 26 to the pin you are using

def read_co2_level():
    sensor_value = co2_sensor_pin.read_u16()  
    co2_ppm = sensor_value / 65535 * 5000     
    return co2_ppm

def main():
    while True:
        # Read the CO2 level
        co2_ppm = read_co2_level()
        
        # Print the CO2 level
        print("CO2 Concentration (ppm): {:.2f}".format(co2_ppm))
        
        # Wait for a few seconds before reading the sensor again
        time.sleep(2)

if __name__ == "__main__":
    main()
