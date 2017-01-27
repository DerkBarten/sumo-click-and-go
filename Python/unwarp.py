import numpy as np
import cv2
from matplotlib import pyplot as plt

# Define camera matrix K
K = np.array( [[ 167.69730563, 0, 316.21916917],
		[0, 165.29531017, 228.87860432],
		[0, 0, 1]])

# Define distortion coefficients d
d = np.array([-0.04919493,  0.04762404,  0.00313313, -0.00210365, -0.02119823])


def unwarp_image(input_matrix):
	# Read an example image and acquire its size
	img = input_matrix
	h, w = img.shape[:2]

	# Generate new camera matrix from parameters
	newcameramatrix, roi = cv2.getOptimalNewCameraMatrix(K, d, (w,h), 0)

	# Generate look-up tables for remapping the camera image
	mapx, mapy = cv2.initUndistortRectifyMap(K, d, None, newcameramatrix, (w, h), 5)

	# Remap the original image to a new image
	newimg = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)


	h, w = newimg.shape[:2]
	center = (w / 2, h / 2)
	M = cv2.getRotationMatrix2D(center, 180, 1.0)
	newimg = cv2.warpAffine(newimg, M, (w, h))
	return newimg

