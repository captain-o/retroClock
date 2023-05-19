# code modified, tweaked and tailored from code by bertwert
# on RPi forum thread topic 91796
import RPi.GPIO as GPIO
import time
import datetime
GPIO.setmode(GPIO.BCM)

# GPIO ports for the 7seg pins
segments =  (11,4,23,8,7,10,18,25)
# 7seg_segment_pins (11,7,4,2,1,10,5,3) +  100R inline

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

# GPIO ports for the digit 0-3 pins
digits = (22,27,17,24)
# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)

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
    '9':(0,0,0,0,1,0,0,1)}
#GPIO.cleanup()

def seg(displyStr):
    for digit in range(4):
        GPIO.output(segments, (num[displyStr[digit]]))
        GPIO.output(digits[digit], 0)
        time.sleep(0.001)
        GPIO.output(digits[digit], 1)

try:

    x= 400
    while x > 0:
        number = datetime.datetime.now().strftime("%H%M")
        print(number)
        #n = number + number + number + number
        #n = datetime.datetime.now().strftime("%H%M")
        displyStr = str(number).rjust(4)
        #seg(display_string)
        seg(displyStr)

finally:
    GPIO.cleanup()
