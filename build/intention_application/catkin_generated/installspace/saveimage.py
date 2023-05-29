#!/usr/bin/env python3
# license removed for brevity
from tf.transformations import quaternion_matrix, quaternion_from_matrix
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import open3d as o3d
import numpy as np
import os
import tf2_ros
import pickle
import message_filters
import tf
import geometry_msgs.msg
import rospy
import tf2_ros
import tf2_geometry_msgs
import geometry_msgs
import sys
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
import actionlib
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list


import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
import actionlib
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

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


def pose2homogen(pose):

    matrix=np.zeros((3,4))
    cur_matrix_homo = np.vstack(( matrix, np.array([0, 0, 0, 1]))) # to homogenous coordinates   
    q=np.array([pose.pose.orientation.x,pose.pose.orientation.y,pose.pose.orientation.z,pose.pose.orientation.w])

    cur_matrix_homo[0][3]= pose.pose.position.x
    cur_matrix_homo[1][3]=pose.pose.position.y
    cur_matrix_homo[2][3]=pose.pose.position.z

    rotm=quaternion_matrix(q)
    cur_matrix_homo[:3, :3]=rotm[:3, :3]
    
    return(cur_matrix_homo)

def callback(rgb : Image, depth : Image):
    rospy.sleep(1)
    current_pose=tf_buffer.lookup_transform("base","tool0_controller",rospy.Duration(0))
    print(current_pose)
    current_pose=tf2homogen(current_pose)
    dir_pose="/home/hamza/ros_ws/src/intention_application/src/numpyfiles/currentpose.npy"
    np.save(dir_pose,current_pose)
    cv_bridge = CvBridge()
    rgb_img = cv_bridge.imgmsg_to_cv2(rgb, "rgb8")
    depth_img = cv_bridge.imgmsg_to_cv2(depth, "16UC1")
    dir_rgb=(os.path.dirname(os.path.abspath(__file__))+"/numpyfiles/"+"imagergb.npy")
    np.save(dir_rgb,rgb_img)
    dir_depth=(os.path.dirname(os.path.abspath(__file__))+"/numpyfiles/"+"imagedepth.npy")
    np.save(dir_depth,depth_img)
    dir_matrix=(os.path.dirname(os.path.abspath(__file__))+"/numpyfiles/"+"mtx.npy")
    print("we out here")
    rospy.wait_for_message("chatterss",String)
    
    
    
  

def ImageFeed():
    rgb_sub=message_filters.Subscriber("camera/color/image_raw",Image)
    depth_sub = message_filters.Subscriber('/camera/depth/image_raw', Image)
    ts = message_filters.ApproximateTimeSynchronizer([rgb_sub,depth_sub],10,1)
    ts.registerCallback(callback)
    rospy.spin()
    print("SS")
    


import geometry_msgs.msg
if __name__ == '__main__':
    rospy.init_node("Camera_Feed", anonymous=True)
    tf_buffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tf_buffer)
    print("HE")
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    # Create a pose stamped message type from the camera image topic.
    ImageFeed()
