# About
This repository contains the code for an interface in which the user is able to click on an arbitrary point in space, and the Sumo Jumper will drive to the specified location.
# Setup
The code requires sumopy to be installed on a place python can find. This could be in dist-packages, but also any other location when specified in the PYTHONPATH evironment variable.

# Run
To run the code, make sure the Sumo is turned on and you are connected to it. Run main.py, a screen should pop up with camera feed from the Sumo. Click on a point on the ground to let the Sumo drive to it.

# Known Issues
* Double clicking results in repeating the same action
* Sumo is irresponsive, in the terminal, the statistics are printed and the drive complete message is shown, but the sumo did not move. Try to reconnect. If it still does not move, try to restart or swapout it's battery.
* After an arbitrary time, the Sumo shuts down /enters sleepmode by itself.
* Some commands nearby the sumo might results in large deviations in the x-direction, this might be of a flawed regression function in the x-direction.
* Clicking above the horizon will result in a negative distance.