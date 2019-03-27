from finch import Finch
from keyboard import *
import keyboard
from time import sleep

finch = Finch()
while True:
        if keyboard.is_pressed('w'):
                finch.wheels(1,1)
        if keyboard.is_pressed('a'):
                finch.wheels(-0.7,0.7)
        if keyboard.is_pressed('d'):
                finch.wheels(0.7,-0.7)
        if keyboard.is_pressed('s'):
                finch.wheels(-1,-1)
        if keyboard.is_pressed('q'):
                sleep(3)
        if keyboard.is_pressed('e'):
                break
                
finch.close()

