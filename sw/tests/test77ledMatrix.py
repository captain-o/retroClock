import re
import time
import argparse
import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
#vcc ->2
#gnd ->6
#dIn ->19
#cs ->24
#clk ->23

serial = spi(port=0, device=0, gpio=noop())
#device = max7219(serial, cascaded=2, block_orientation=block_orientation, rotate=rotate, blocks_arranged_in_reverse_order=inreverse)
device = max7219(serial, cascaded=2)
print("Created device")
device.contrast(10)
#device.contrast(100)


print(datetime.datetime.now().strftime("%H%M"))

while True:
    currentTime = datetime.datetime.now().strftime("%H%M")
    print(currentTime)
    with canvas(device) as draw:
        text(draw, (1, 0), currentTime, fill="white", font=proportional(TINY_FONT))
        #text(draw, (0, 0), currentTime, fill="white", font=proportional(LCD_FONT))
        #show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)
        time.sleep(1)





def testDisplay():

    for i in range(7):
        with canvas(device) as draw:
            print(i)
            text(draw, (0, 0), "LENA", fill="white", font=proportional(TINY_FONT))
            time.sleep(1)
    for i in range(5):
        with canvas(device) as draw:
            print(i)
            text(draw, (0, 0), "<3<3", fill="white", font=proportional(TINY_FONT))
            time.sleep(1)

#msg = "Hello"
#print(msg)
#show_message(device, msg, fill="white", font=proportional(CP437_FONT))
#time.sleep(1)

#show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0)

#with canvas(device) as draw:
 #  draw.rectangle(device.bounding_box, outline="white", fill="black")
  # draw.text((3, 3), "Hello world", fill="white")
