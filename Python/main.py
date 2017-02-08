from sumopy.interface import SumoController
import numpy as np
from navigation import *
from constants import *
import time

import cv2
import math
from skimage import io
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Make a connection to the sumo
controller = SumoController()
# Needed for initializing, probably for initializing the command stack. If this
# command is not issued before taking a photo, the Sumo usually gives an error.
controller.move(0,0)
# Get a picture from the sumo
pic = get_picture(controller)

lookForInput=True

def onclick(event, x, y, flags, param):
	global pic
	global lookForInput
	if event == cv2.EVENT_LBUTTONDOWN:
		print "Click detected"
		x,y=screen_to_local(x, y)[:2]
		delta_y = distance_y(y)
		delta_x = distance_x(x,y)
		print delta_y
		print delta_x
		lookForInput=False
		dur = move_to_point(controller, delta_x, delta_y, 20, verbose=False)
		time.sleep(dur + 1)
		print "Drive Completed"
		pic = old_picture(controller)
		print "Show next picture"
		cv2.imshow("image",pic)
		lookForInput=True

cv2.namedWindow("image")
cv2.setMouseCallback("image", onclick)
print "Showing Picture"


while True:
	cv2.imshow("image",pic)
	key = cv2.waitKey(1) & 0xFF
	if not lookForInput:
		continue
        if key == 27:
		cv2.destroyAllWindows()
		exit(0)

	if key == 83:
		duration = slow_turn(controller, math.pi/2.0)
		time.sleep(duration + 0.5)
		pic = old_picture(controller)
		print "Show next picture"
		cv2.imshow("image",pic)

	if key == 81:
		duration = slow_turn(controller, -1*math.pi/2.0)
		time.sleep(duration + 0.5)
		pic = old_picture(controller)
		print "Show next picture"
		cv2.imshow("image",pic)
