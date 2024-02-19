import winsound
import time

def beep():
    winsound.Beep(2500,1000)

while True:
    time.sleep(5)
    beep()
    print("Drink Water")