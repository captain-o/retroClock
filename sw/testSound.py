
import pygame

def playAlarm():
    pygame.mixer.init()
    pygame.mixer.music.load("klingel-ding-dong.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


playAlarm()
