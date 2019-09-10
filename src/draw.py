from machine import ADC, Pin
from pins import tft, buttons
from lib.ST7735 import TFT

# Pin Defs
pot = ADC(Pin(34))
pot.width(ADC.WIDTH_10BIT)
pot.atten(ADC.ATTN_11DB)



def run():
    """
    Run function

    takes a pot input and outputs a pixel on the tft
    """
    axis = True
    coord = [50, 0]
    tft.fill(TFT.BLACK)
    while True:
        
        coord[int(axis)] = int(pot.read()/8)
        print(coord, [x.value() for x in buttons])
        if buttons[0].value() == 0:
            print('button0')
            axis = not axis
        
        if buttons[1].value() == 0:
            print('button1')
            # break

        tft.pixel(coord, TFT.RED)

        

