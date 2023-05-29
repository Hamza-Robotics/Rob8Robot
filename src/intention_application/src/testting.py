import cv2
import numpy as np
import os



rgb_img=np.load((os.path.dirname(os.path.abspath(__file__))+"/numpyfiles/"+"imagergb.npy"))
cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
cv2.imshow("g",rgb_img)
cv2.waitKey(0)