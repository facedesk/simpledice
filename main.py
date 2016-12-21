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
	print(str(num) +" > "+str(max/num))
        if (max/num)<=(1):
            sense.show_message(str(num),text_colour=blue)
        elif (max/num)<=(2):
            sense.show_message(str(num),text_colour=green)
        elif ((max/num)<= 3):
            sense.show_message(str(num),text_colour=red)
	else:
	    sense.show_message("invalid "+str(num),text_colour=red)
