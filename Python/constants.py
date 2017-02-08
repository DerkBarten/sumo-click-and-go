from enum import Enum

# CONSTANTS OF NAVGATION.PY
MINIMAL_SPEED=20
DISTANCE_CONSTANT=2.75
STOP_CONSTANT=0.4

# Constants received by using linear regression
TURN_CONSTANT_A=2.6336
TURN_CONSTANT_B=-0.49059
# The turnspeed of the sumo
SLOW_TURN=4

# Standard speed (scale 0-100)
SPEED=30

# Distance constants used by calculation in y direction received by using
# linear regression
A1=0.001226
B1=-6.0579
C1=9.2569
D1=1.5988

# Distance constants used by calculation in x direction received by using
# linear regression
A2=-0.0095437
B2=2.8863
C2=0.46188

# The image dimensions received from the robot
IMAGE_HEIGHT=480
IMAGE_WIDTH=640
