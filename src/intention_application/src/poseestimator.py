import numpy as np
import cv2 as cv
import os
from mediapipe import solutions
import cv2
import time
import pandas as pd
import numpy as np
import os
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import pickle


def puttext(image,RF_intention,SVM_intention, nn_intention):
    strings_rf="empty"
    color_rf=(0,0,0)
    if RF_intention==True:
        strings_rf="RFC: Intention Yes"
        color_rf = (0, 255, 0)
    if RF_intention==False:
        strings_rf="RFC: Intention No"
        color_rf = (0, 0, 255)

    strings_SVM="empty"
    color_svm=(0,0,0)
    if SVM_intention==True:
        strings_SVM="SVM: Intention Yes"
        color_svm = (0, 255, 0)
    if SVM_intention==False:
        strings_SVM="SVM: Intention No"
        color_svm = (0, 0, 255)
    
    strings_nn="empty"
    color_nn=(0,0,0)
    if nn_intention==True:
        strings_nn="NNC: Intention Yes"
        color_nn = (0, 255, 0)
    if nn_intention==False:
        strings_nn="NNC: Intention No"
        color_nn = (0, 0, 255)

        
    
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # org
    org = (50, 50)
    
    # fontScale
    fontScale = 1
    
    # Blue color in BGR
    
    # Line thickness of 2 px
    thickness = 2
    
    # Using cv2.putText() method
    image = cv2.putText(image, strings_rf, org, font, 
                    fontScale, color_rf, thickness, cv2.LINE_AA)
    image = cv2.putText(image, strings_SVM, (50, 100), font, 
                    fontScale, color_svm, thickness, cv2.LINE_AA)   
    image = cv2.putText(image, strings_nn, (50, 150), font, 
                    fontScale, color_nn, thickness, cv2.LINE_AA)   
    return image


file = open("/home/hamza/poseestimation/Models/RandomForrestPickle", 'rb')
clf_RF = pickle.load(file)
file = open("/home/hamza/poseestimation/Models/NN", 'rb')
clf_NN= pickle.load(file)
file = open("/home/hamza/poseestimation/Models/SVMPickle", 'rb')
clf_SVM= pickle.load(file)

file = open("/home/hamza/poseestimation/Models/Scaler", 'rb')
scaler=  pickle.load(file)

file="/home/hamza/yesintention1.avi"


cap = cv.VideoCapture(file)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
# if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv2.imshow('frame', frame)

    mpPose = solutions.pose
    points = mpPose.PoseLandmark # Landmarks
    pose = mpPose.Pose()
    mpDraw = solutions.drawing_utils # For drawing keypoints
    results = pose.process(frame)


    temp=[]

    if results.pose_landmarks:
        mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS) # draw landmarks on blackie
        for j in results.pose_landmarks.landmark:
            temp = temp + [j.x, j.y,j.z, j.visibility]    
        x=np.asanyarray(temp).reshape(1, -1)
        x_scaled=scaler.transform(x)
        y_nn=clf_NN.predict(x_scaled)
        y_rf=clf_RF.predict(x)
        y_SVM=clf_SVM.predict(x_scaled)

        frame=puttext(frame,y_rf,y_SVM,y_nn)
    cv2.imshow('frame', frame)
    
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 

