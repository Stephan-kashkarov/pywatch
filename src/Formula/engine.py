"""
TODO: Make UI elements render
TODO: Make engine decorator
"""
from pyb import SPI
from machine import Pin, ADC
from lib import (
    # Screens
    st7735,
    # Touch Displays
)

# Engines


class Breadboard:
    def __init__(self, **kwargs):
        self.pot = ADC(Pin(0))
        self.x_move = True
        self.cursor = [0, 0]
        self.spi = SPI(SPI.MASTER, baudrate=20000000, polarity=0, phase=0)
        self.tft = st7735.tft(self.spi, Pin(0), Pin(12))
        # Interrupt handler
        Pin(16).irq(handler=self.flags(), trigger=Pin.IRQ_RISING)

    def check_input(self):
        self.cursor[int(self.x_move)] = self.pot.read()

    def show_bitmap(self, bitmap):
        cursor = Bitmap(
            map=[
                ["00 00 00",  "00 00 00",  "00 00 00", ],
                ["00 00 00",  "FF 00 00",  "00 00 00", ],
                ["00 00 00",  "00 00 00",  "00 00 00", ],
            ],
        )
        bitmap.add(cursor, pos=self.cursor)
        for y, row in bitmap.raw():
            for x, pixel in enumerate(row):
                self.tft.pixel((y, x), TFTColor(*pixel.split()))
        
    def flags(self):
        self.x_move = not self.x_move

# Core classes


class Bitmap:
    def __init__(self, **kwargs):
        self.map = kwargs.get('map', False)
        if self.map:
            self.size = (len(_map), len(_map[0]))
        else:
            # Dont question this please i like it >:(
            self.size = kwargs.get("size", lambda: raise Exception("Args missing"))
            self.map = []
            for y in range(self.size[0]):
                self.map.append([])
                for _ in range(self.size[1]):
                    self.map[y].append("00 00 00")

    def add(self, bitmap, pos):
        if not bitmap:
            return
        for y in range(pos[0], pos[0] + len(bitmap)):
            for x in range(pos[1], pos[1] + len(bitmap[0])):
                self.bitmap[y][x] = bitmap[pos[0] - y][pos[1] - x]


class Interaction:
    def __init__(self, **kwargs):
        self.type = kwargs.get('type')
        self.pos = kwargs.get('pos')