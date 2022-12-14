'''
 # @ Author: Nabin Paudel|Scelester
 # @ Create Time: 2022-12-13 23:11:20
 # @ Modified time: 2022-12-27 10:36:20 
 # @ Description: retrive PH sensor data using ADC 
 '''


import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
# ------------------------------  
import math


def get_ph_value():
    # create the spi bus
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

    # create the cs (chip select)
    cs = digitalio.DigitalInOut(board.D5)

    # create the mcp object
    mcp = MCP.MCP3008(spi, cs)

    # create an analog input channel on pin 0 
    chan = AnalogIn(mcp, MCP.P0)


    # print('Raw ADC Value: ', chan.value)
    # print('ADC Voltage: ' + str(chan.voltage) + 'V')
    
    phval = (chan.voltage + 20.046) * (10.24/6)/5

    # return ((chan.voltage*10)/59.16)*1000

    # print(float(phval))
    
    return float(phval),float(chan.voltage)