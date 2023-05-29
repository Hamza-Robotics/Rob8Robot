#!/usr/bin/env python
# license removed for brevity

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import open3d as o3d
import numpy as np
import os
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
import message_filters
import tf
import pickle
from tf.transformations import quaternion_matrix, quaternion_from_matrix

moveit_commander.roscpp_initialize(sys.argv)
import tf2_ros

from scipy.spatial.transform import Rotation


def tf2homogen(pose):
    matrix=np.zeros((3,4))
    matrix = np.vstack(( matrix, np.array([0, 0, 0, 1]))) # to homogenous coordinates   
    q=np.array([pose.transform.rotation.x,
                pose.transform.rotation.y,
                pose.transform.rotation.z,
                pose.transform.rotation.w])
    

    matrix[0][3]= pose.transform.translation.x
    matrix[1][3]=pose.transform.translation.y
    matrix[2][3]=pose.transform.translation.z

    rotm=quaternion_matrix(q)
    matrix[:3, :3]=rotm[:3, :3]

    return matrix



def matrix_to_pose_quaternion(matrix):
    # Extract translation from the matrix
    translation = matrix[:3, 3]

    # Extract rotation matrix from the matrix
    rotation_matrix = matrix[:3, :3]

    # Convert rotation matrix to quaternion
    rotation = Rotation.from_matrix(rotation_matrix)
    quaternion = rotation.as_quat()

    return translation, quaternion


def quat2rotm(Q):

    q0 = Q[3]
    q1 = Q[2]
    q2 = Q[1]
    q3 = Q[0]
     
    # First row of the rotation matrix
    r00 = 2 * (q0 * q0 + q1 * q1) - 1
    r01 = 2 * (q1 * q2 - q0 * q3)
    r02 = 2 * (q1 * q3 + q0 * q2)
     
    # Second row of the rotation matrix
    r10 = 2 * (q1 * q2 + q0 * q3)
    r11 = 2 * (q0 * q0 + q2 * q2) - 1
    r12 = 2 * (q2 * q3 - q0 * q1)
     
    # Third row of the rotation matrix
    r20 = 2 * (q1 * q3 - q0 * q2)
    r21 = 2 * (q2 * q3 + q0 * q1)
    r22 = 2 * (q0 * q0 + q3 * q3) - 1
     
    # 3x3 rotation matrix
    rot_matrix = np.array([[r00, r01, r02],
                           [r10, r11, r12],
                           [r20, r21, r22]])
                            
    return rot_matrix


def pose2homogen(pose):
    matrix=np.zeros((3,4))

    cur_matrix_homo = np.vstack(( matrix, np.array([0, 0, 0, 1]))) # to homogenous coordinates   
    q=np.array([pose.pose.orientation.x,pose.pose.orientation.y,pose.pose.orientation.z,pose.pose.orientation.w])

    cur_matrix_homo[0][3]= pose.pose.position.x
    cur_matrix_homo[1][3]=pose.pose.position.y
    cur_matrix_homo[2][3]=pose.pose.position.z

    rotm=quat2rotm(q)
    cur_matrix_homo[:3, :3]=rotm


    return cur_matrix_homo
def cv2homogen(tvec,rvec):
    matrix = np.array([[0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 1]],
                            dtype=float)
    

    matrix[:3, :3], _ = cv2.Rodrigues(rvec)
    matrix[0][3]=tvec[0,0,0]
    matrix[1][3]=tvec[0,0,1]
    matrix[2][3]=tvec[0,0,2]



    return matrix

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "manipulator"
group = moveit_commander.MoveGroupCommander(group_name)
mtx=np.load("intention_application/src/numpyfiles/mtx.npy")
#mtx= np.array([[570.3405082258201, 0.0, 319.5], [0.0, 570.3405082258201, 239.5], [0.0, 0.0, 1.0]])

dist=np.load("intention_application/src/numpyfiles/dist.npy")



dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
parameters =  cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(dictionary, parameters)
poses=[]
aruco=[]
moveit2tf=np.load("intention_application/src/handeyecalibration/moveit2tf.npy")

def callback(rgb : Image, pose : geometry_msgs.msg.PoseStamped):

    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)
    parameters =  cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(dictionary, parameters)


    cv_bridge = CvBridge()
    rgb_img = cv_bridge.imgmsg_to_cv2(rgb, "rgb8")
    markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(rgb_img)
    TCB=(tf_buffer.lookup_transform("base","tool0_controller",rospy.Time()))
    if len(markerCorners) > 0:

        rvec, tvec, markerPoints = cv2.aruco.estimatePoseSingleMarkers(markerCorners,0.154,mtx,dist)
        if np.shape(rvec)[0]==1:
            cv2.drawFrameAxes(rgb_img,mtx,0,rvec, tvec, 0.1)
            #print(np.linalg.norm(tvec))
            print(tf2homogen(TCB))
            cv2.imshow("rgb",rgb_img)
            cv2.waitKey(1)
            print(len(poses))
            
            poses.append(tf2homogen(TCB))
            aruco.append(cv2homogen(tvec,rvec))


    if len(poses)==40:
        print("save")
        with open("/home/hamza/ros_ws/src/intention_application/src/handeyecalibration/aruco", "wb") as fp:   #Pickling
            pickle.dump(aruco, fp)

        with open("/home/hamza/ros_ws/src/intention_application/src/handeyecalibration/poses", "wb") as fp:   #Pickling
            pickle.dump(poses, fp)
def ImageFeed():
    rgb_sub=message_filters.Subscriber("camera/color/image_raw",Image)
    pose = message_filters.Subscriber('/intentionapplication/handeyecalibration/posegiver', geometry_msgs.msg.PoseStamped)
    ts = message_filters.ApproximateTimeSynchronizer([rgb_sub,pose],100,0.5)
    ts.registerCallback(callback)
    rospy.spin()



if __name__ == '__main__':

    rospy.init_node('transform_object_poses', anonymous=True)


    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    
    global count
    count=0

    ImageFeed()
