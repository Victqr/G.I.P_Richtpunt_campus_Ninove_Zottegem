import machine
import time
import pycompss.mq131 as mq131

def setup():
    print("Calibration in progress...")
    r0, time_to_heat = mq131.calibrate()
    print("Calibration done!")
    print(f"R0 = {r0} Ohms")
    print(f"Time to heat = {time_to_heat} s")

def loop():
    while True:
        print("Sampling...")
        o3_ppm, o3_ppb, o3_mg_m3, o3_ug_m3 = mq131.sample()
        print(f"Concentration O3 (ppm): {o3_ppm}")
        print(f"Concentration O3 (ppb): {o3_ppb}")
        print(f"Concentration O3 (mg/m3): {o3_mg_m3}")
        print(f"Concentration O3 (ug/m3): {o3_ug_m3}")
        print("")
        time.sleep(30)

if __name__ == "__main__":
    setup()
    loop()