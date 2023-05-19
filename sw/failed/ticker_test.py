from RPi import GPIO
import time
GPIO.setmode(GPIO.BCM)

# GPIO ports for the 7seg pins
segments =  (11,4,23,8,7,10,18,25)
# 7seg_segment_pins (11,7,4,2,1,10,5,3) +  100R inline
GPIO.setup(segments, GPIO.OUT, initial=0)

# GPIO ports for the digit 0-3 pins
digits = (22,27,17,24)
# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively
GPIO.setup(digits, GPIO.OUT, initial=1)

#          (a,b,c,d,e,f,g,dp)
num = {' ':(0,0,0,0,0,0,0,0),
    '0':(0,0,0,0,0,0,1,1),
    '1':(1,0,0,1,1,1,1,1),
    '2':(0,0,1,0,0,1,0,1),
    '3':(0,0,0,0,1,1,0,1),
    '4':(1,0,0,1,1,0,0,1),
    '5':(0,1,0,0,1,0,0,1),
    '6':(0,1,0,0,0,0,1,1),
    '7':(0,0,0,1,1,1,1,1),
    '8':(0,0,0,0,0,0,0,1),
    '9':(0,0,0,0,1,0,0,1),
    'b':(0,0,1,1,1,1,1,0),
    'y':(0,1,1,1,0,1,1,0),
    'E':(1,0,0,1,1,1,1,0),
    'A':(1,1,1,0,1,1,1,0),
    'L':(0,0,0,1,1,1,0,0),
    'X':(0,1,1,0,1,1,1,0)}

def seg():
    for digit in range(4):
        GPIO.output(segments, (num[display_string[digit]]))
        GPIO.output(digits[digit], 0)
        time.sleep(0.001)
        GPIO.output(digits[digit], 1)
try:

    while True:
        n = "3333"
        display_string = str(n).rjust(4)
        print(display_string)
        seg()

finally:
    GPIO.cleanup()
