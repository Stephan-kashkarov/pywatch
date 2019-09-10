from lib.ST7735 import TFT
from lib.sysfont import sysfont
from machine import SPI, Pin, I2C
import network
import time
import ntptime
import math
from pins import tft


def convTime(t) -> (int, int, int):
    """ Conv time
        This function takes Time object and returns 3 normalised
        integers to alow for the clock hand function to be reused

        Args:
            t: The time object from the utime lib
        
        Returns:
            (H, M, S): set of three integers in range(60)
    """
    return (t[3] % 12) * 5, t[4], t[5]


def clock(t) -> None:
    """
    Clock

    This function takes a time object and
    draws an analogue clock onto the screen
    in UTC time.

    Arg:
        t: The time object from the utime lib

    Returns: 
        None
    """
    tft.fill(TFT.WHITE)
    # tft.circle(Center, 63, TFT.GRAY)
    h, m, s = convTime(t)
    print("a")
    hand(h, 40, (64, 64), TFT.BLACK)
    print("b")
    hand(m, 20, (64, 64), TFT.GRAY)
    hand(s, 50, (64, 64), TFT.GREEN)
    time.sleep(0.5)


def hand(sec: float, radius: float, center: (int, int), color: (int, int, int)) -> None:
    """
    hand function

    This function takes a number form 0 to 60
    and prints it as an analogue hand.

    Args:
        secs: number between 0 and 60 of the time
        radius: the length of the hand
        center: the center point in (x, y)
        color: rgb value of the line (R, G, B) in ints

    Returns:
        None
    """
    if sec == 0 or sec == 60:
        tft.vline(center, -(radius), color)
    else:
        if 0 < sec <= 15:  # First sector
            A = math.tan(
                math.radians(90 - (sec * 6))
            )
            y = center[0] - math.sqrt((math.pow(radius, 2) * A) / (A + 1))
            x = center[1] + (y / A)
        elif 15 < sec <= 30:  # Second sector
            A = math.tan(
                math.radians((sec - 15) * 6)
            )
            y = center[0] + math.sqrt((math.pow(radius, 2) * A) / (A + 1))
            x = center[1] + (y / A)
        elif 30 < sec <= 45:  # Thrid sector
            A = math.tan(
                math.radians(90 - ((sec - 30) * 6))
            )
            y = center[0] + math.sqrt((math.pow(radius, 2) * A) / (A + 1))
            x = center[1] - (y / A)
        elif 45 < sec < 60:  # Forth sector
            A = math.tan(
                math.radians((sec - 45) * 6)
            )
            y = center[0] - math.sqrt((math.pow(radius, 2) * A) / (A + 1))
            x = center[1] - (y / A)

        tft.line(center, (int(x), int(y)), color)      


def run():
    """
    run function

    This function runs the clock in a try catch block
    on whatever time, time.localtime is running on.
    """
    while True:
        try:
            clock(time.localtime())
            time.sleep(0.5)
        except ZeroDivisionError:
            pass
