from enum import Enum

# CONSTANTS OF NAVGATION.PY
MINIMAL_SPEED=20
DISTANCE_CONSTANT=2.75
STOP_CONSTANT=0.4

# empirically gathered constants which help to convert angles to motor input
TURN_CONSTANT_A=2.6336
TURN_CONSTANT_B=-0.49059

SLOW_TURN=4

PICTURE_NAME="pic.jpg"
PICTURE_NAME_UNWARPED="pic_unwarped.jpg"

# user change able parameters
SPEED=30

# Distance calculation in y direction
A1=0.001226
B1=-6.0579
C1=9.2569
D1=1.5988

# Distance calculation in x direction
A2=-0.0095437
B2=2.8863
C2=0.46188

# image received from the robot
IMAGE_HEIGHT=480
IMAGE_WIDTH=640

# the smallest allowed angle
DURATION_THRESHHOLD=1.0/40
