from machine import Pin, ADC
from micropython import const
import utime
from math import exp, log

class BaseMQ:
    MQ_SAMPLE_TIMES = const(5)
    MQ_SAMPLE_INTERVAL = const(10) #delay time sensor uit lezen aangpast van 500
    MQ_HEATING_PERIOD = const(60000)
    MQ_COOLING_PERIOD = const(90000)
    STRATEGY_FAST = const(1)
    STRATEGY_ACCURATE = const(2)

    def __init__(self, pinData, pinHeater=-1, boardResistance=10, baseVoltage=3.3, measuringStrategy=STRATEGY_ACCURATE):
        self._heater = False
        self._cooler = False
        self._ro = -1
        self._useSeparateHeater = False
        self._baseVoltage = baseVoltage
        self._lastMeasurement = utime.ticks_ms()
        self._rsCache = None
        self.dataIsReliable = False
        self.pinData = ADC(pinData)
        self.measuringStrategy = measuringStrategy
        self._boardResistance = boardResistance

        if pinHeater != -1:
            self._useSeparateHeater = True
            self.pinHeater = Pin(pinHeater, Pin.OUT)

    def getRoInCleanAir(self):
        raise NotImplementedError("Please Implement this method")

    def calibrate(self, ro=-1):
        if ro == -1:
            ro = 0
            print("Calibrating:")
            for i in range(0, self.MQ_SAMPLE_TIMES + 1):
                print("Step {0}".format(i))
                ro += self.__calculateResistance__(self.pinData.read_u16())
                utime.sleep_ms(self.MQ_SAMPLE_INTERVAL)
            ro = ro / (self.getRoInCleanAir() * self.MQ_SAMPLE_TIMES)
        self._ro = ro
        self._stateCalibrate = True

    def heaterPwrHigh(self):
        if self._useSeparateHeater:
            self.pinHeater.on()
        self._heater = True
        self._prMillis = utime.ticks_ms()

    def heaterPwrLow(self):
        self._heater = True
        self._cooler = True
        self._prMillis = utime.ticks_ms()

    def heaterPwrOff(self):
        if self._useSeparateHeater:
            self.pinHeater.off()
        self._heater = False

    def __calculateResistance__(self, rawAdc):
        vrl = rawAdc * (self._baseVoltage / 65535)
        rsAir = (self._baseVoltage - vrl) / vrl * self._boardResistance
        return rsAir

    def __readRs__(self):
        if self.measuringStrategy == self.STRATEGY_ACCURATE:
            rs = 0
            for i in range(0, self.MQ_SAMPLE_TIMES + 1):
                rs += self.__calculateResistance__(self.pinData.read_u16())
                utime.sleep_ms(self.MQ_SAMPLE_INTERVAL)
            rs = rs / self.MQ_SAMPLE_TIMES
            self._rsCache = rs
            self.dataIsReliable = True
            self._lastMeasurement = utime.ticks_ms()
        else:
            rs = self.__calculateResistance__(self.pinData.read_u16())
            self.dataIsReliable = False
        return rs

    def readScaled(self, a, b):
        return exp((log(self.readRatio()) - b) / a)

    def readRatio(self):
        return self.__readRs__() / self._ro

    def heatingCompleted(self):
        if self._heater and (not self._cooler) and (utime.ticks_diff(utime.ticks_ms(), self._prMillis) > self.MQ_HEATING_PERIOD):
            return True
        else:
            return False

    def coolanceCompleted(self):
        if self._heater and self._cooler and (utime.ticks_diff(utime.ticks_ms(), self._prMillis) > self.MQ_COOLING_PERIOD):
            return True
        else:
            return False

    def cycleHeat(self):
        self._heater = False
        self._cooler = False
        self.heaterPwrHigh()
        print("Heated sensor")

    def atHeatCycleEnd(self):
        if self.heatingCompleted():
            self.heaterPwrLow()
            print("Cool sensor")
            return False
        elif self.coolanceCompleted():
            self.heaterPwrOff()
            return True
        else:
            return False
        
    def readScaled(self, a, b):        
        ratio = self.readRatio()
        if ratio <= 0:
            return 0  # Voorkom logaritme van negatieve of nulwaarden
        return exp((log(ratio)-b)/a)
    
    