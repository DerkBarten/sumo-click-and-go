from sumopy.interface import SumoController
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import io
import numpy as np
import navigation as nav
import constants as con
import image as im # TODO maybe change this name
import time

import unwarp as wrp


controller = SumoController()
nav.picture(controller, con.PICTURE_NAME)
# we will just override the image
wrp.unwarp_image(con.PICTURE_NAME, con.PICTURE_NAME)
pic = io.imread(con.PICTURE_NAME)
mode = con.MODE.TO_POINT

def onclick(event):
  global mode
  global image
  if event.xdata != None and event.ydata != None:
    x,y=nav.screen_to_local(event.xdata, event.ydata)[:2]
    print "x = " + str(x)
    print "y = " + str(y)
    print nav.distance_y(y)
    print nav.distance_x(x,y)
	
plt.gcf().canvas.mpl_connect('button_press_event', onclick)
canvas = plt.gca()
canvas.imshow(pic)
canvas.axis('off')
plt.show()
	    

#print "connected?"