from enum import Enum

# CONSTANTS OF NAVGATION.PY
MINIMAL_SPEED=20
DISTANCE_CONSTANT=2.75
STOP_CONSTANT=0.4
BASIC_TURNSPEED=0.125
PICTURE_NAME="pic.jpg"

# user change able parameters
SPEED=30


# CONSTANTS OF IMAGE.PY

# constants found by fitting the data to the curve
A=31.567
B=0.066258


# Distance calculation in y direction
A1=-0.081288
B1=17.67
C1=136.28
D1=13.1

# Distance calculation in x direction
A2=1.2749
B2=18.127
C2=1130.5

# image received from the robot
IMAGE_HEIGHT = 480
IMAGE_WIDTH=640

# the horizon in the image, assuming the camera is in a 90 degree angle to the ground, 
# it is half of the image height
HORIZON= IMAGE_HEIGHT / 2

# the distance of the lowest pixel in the screen
BOTTOM_OF_SCREEN=17

# parameters of slic image segmentation
N_SEGMENTS=45
COMPACTNESS=14 
SIGMA=3


class MODE(Enum):
  TO_POINT = 1
  TO_OBJECT = 2