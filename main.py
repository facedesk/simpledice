from __future__ import division
from sense_hat import SenseHat
from random import randint


sense = SenseHat()
red  = (255,0,0)
blue=(0,0,255)
green=(0,255,0)
min=1
max =6

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z= acceleration['z']

    x = round(x,0)
    y = round(y,0)
    z = round(z,0)

#    print("x={0}, y= {1}, z = {2}".format(x,y,z))
    if(x>1 or y>1 or z>1):
        num = randint(min,max)
        ratio = max/num

	print(str(max)+","+str(num) +" > "+str(ratio))
        if (ratio <=1):
            sense.show_message(str(num),text_colour=blue)
        elif (ratio <=2):
            sense.show_message(str(num),text_colour=green)
        elif (ratio <= 3 or num == 1):
            sense.show_message(str(num),text_colour=red)
	else:
	    sense.show_message("invalid "+str(num),text_colour=red)
