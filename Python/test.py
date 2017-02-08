import numpy as np
import cv2



fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
frame = cv2.imread("images/map.jpg",cv2.IMREAD_COLOR)

fgmask = fgbg.apply(frame, learningRate=0.001)
print fgmask
cv2.imshow('frame',fgmask)
    

cv2.waitKey(0)
cv2.destroyAllWindows()