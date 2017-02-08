import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage import io

# Parameters of slic image segmentation
N_SEGMENTS=45
COMPACTNESS=14
SIGMA=3

# A possible image segmentation technique
def slic_segmentation(image_path):
  image = io.imread(image_path)
  segments = slic(image, n_segments=N_SEGMENTS, compactness=COMPACTNESS, sigma=SIGMA)
  return segments # Returns a plottable image
