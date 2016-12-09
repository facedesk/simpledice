from sense_hat import SenseHat
from random import randint


sense = SenseHat()
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0,255)
min=1
max=6
num = randint(min,max)



if((max/num) >= 3.0):
  sense.show_message(str(num), text_colour = blue)
elif((max/num) >= 2.0):
  sense.show_message(str(num), text_colour = green)
else:
  sense.show_message(str(num), text_colour = red)