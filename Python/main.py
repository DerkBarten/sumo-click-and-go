from sumopy.interface import SumoController
import numpy as np
import navigation as nav
from constants import *
import time
import unwarp as wrp
import cv2
import math
from PIL import Image
from StringIO import StringIO
from skimage import io
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

	
#nav.slow_turn(controller, math.pi/2.0, chain=True)
#nav.move_to_point(controller, 0, 150, 20, verbose=False)
#nav.slow_turn(controller, math.pi/2.0, chain=True)
#nav.move_to_point(controller, 0, 150, 20, verbose=False)
#



def nice_picture(controller):
	controller.store_pic()
	pic = controller.get_pic()

	#convert pic to Image
	img = Image.open(StringIO(pic))

	np_pic = np.array(img.getdata(), np.uint8).reshape(img.size[1], img.size[0], 3)
	
	# unwarp the image
	pic = wrp.unwarp_image(np_pic)
	return pic

	
# make a connection to the sumo
controller = SumoController()
# need for initializing
controller.move(0,0)

pic = nice_picture(controller)
#nav.move_to_point(controller, 0, 100, 20, verbose=False)

#nav.slow_turn(controller, math.pi/)
#nav.move_to_point(controller, 20, 100, 20, verbose=False)

def onclick(event, x, y, flags, param):
	global pic
	if event == cv2.EVENT_LBUTTONDOWN:
		print "Click detected"
		x,y=nav.screen_to_local(x, y)[:2]
		delta_y = nav.distance_y(y)
		delta_x = nav.distance_x(x,y)
		print delta_y
		print delta_x
		nav.move_to_point(controller, delta_x, delta_y, 20, verbose=False)
		time.sleep(2)
		pic = nice_picture(controller)
		print "Show picture"
		cv2.imshow("image",pic)

cv2.namedWindow("image")
cv2.setMouseCallback("image", onclick)
print "Showing Picture"

  
while True:
	cv2.imshow("image",pic)
	key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
		cv2.destroyAllWindows()
		exit(0)
