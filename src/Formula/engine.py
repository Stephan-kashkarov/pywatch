"""
TODO: Make UI elements render
TODO: Make engine decorator
"""
from pyb import SPI
from machine import Pin, ADC
from lib import (
    #* Screens
    st7735,
    #* Touch Displays
)

## Engines

class Breadboard:
    def __init__(self, **kwargs):
        self.pot = ADC(Pin(0))
        self.x_move = True
        self.cursor = [0, 0]
        self.spi = SPI(SPI.MASTER, )

    def check_input(self):
        self.cursor[int(self.x_move)] = self.pot.read()

    def show_bitmap(self, bitmap):
        bitmap.add()

## Core classes
