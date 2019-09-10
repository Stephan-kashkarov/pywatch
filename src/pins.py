from lib.ST7735 import TFT
from lib.sysfont import sysfont
from machine import SPI, Pin, I2C

spi = SPI(2, baudrate=20000000, polarity=0, phase=0,
          sck=Pin(14), mosi=Pin(13), miso=Pin(12))
tft = TFT(spi, 16, 17, 18)
tft.initr()
tft.rgb(True)
buttons = [Pin(27, Pin.IN), Pin(25, Pin.IN)]
