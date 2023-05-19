from gpiozero import LightSensor, Buzzer

ldr = LightSensor(11)  # alter if using a different pin
while True:
    print(ldr.value)
