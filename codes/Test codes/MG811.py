import machine
import time

# Define the pin to which the sensor is connected
sensor_pin = machine.ADC(27)

def read_sensor():
    # Read the analog value from the sensor
    sensor_value = sensor_pin.read_u16()

    # Convert the raw sensor value to ppm
    ppm = sensor_value / 65535 * 3.3

    return ppm

def main():
    while True:
        # Read the sensor value
        ppm = read_sensor()
        
        # Print the ppm value
        print("Concentration O3 (ppm): {:.2f}".format(ppm))
        
        # Wait for a few seconds before reading the sensor again
        time.sleep(2)

if __name__ == "__main__":
    main()
