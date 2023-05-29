import os
import cv2
import numpy as np
import cv2 as cv
import glob
# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

shape = (7,9)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((shape[0]*shape[1],3), np.float32)
objp[:,:2] = np.mgrid[0:shape[0],0:shape[1]].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

arr = os.listdir('intention_application/src/CameraCalibration/image')
i=0


 
    # Find the chess board corners
for image in arr:
    i=i+1

    gray = cv2.imread("intention_application/src/CameraCalibration/image/"+image,0) 
    img=cv2.imread("intention_application/src/CameraCalibration/image/"+image,0) 
    print(np.shape(gray))
    # Find the chess board corners	cv2.imshow("I",img)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, shape)


    # If found, add object points, image points (after refining them)
    if ret == True:
        if i==10:
            break
        objpoints.append(objp)

        imgpoints.append(corners)
        #corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        #imgpoints.append(corners2)



#cv2.destroyAllWindows()



ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

#Reprojection error
tot_error = 0.0
tot_error_sq = 0.0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
    tot_error += error
    tot_error_sq += error * error
np.save("/home/hamza/ros_ws/src/intention_application/src/numpyfiles/mtx.npy",mtx)
np.save("/home/hamza/ros_ws/src/intention_application/src/numpyfiles/dist.npy",dist)
print(mtx)
print(dist)

import math
print ("mean absolute error: ", tot_error/len(objpoints))
print ("rms error: ", math.sqrt(tot_error_sq/len(objpoints)))

