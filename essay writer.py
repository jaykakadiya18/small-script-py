import rotatescreen
import time

screen = rotatescreen.get_primary_display()

for i in range(1):
    time.sleep(0.3)
    screen.rotate_to(i*90 % 360)

