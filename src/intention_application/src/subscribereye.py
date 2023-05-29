#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import geometry_msgs.msg


import rospy
from std_msgs.msg import String
import tf2_ros
import geometry_msgs.msg
from tf.transformations import quaternion_matrix, quaternion_from_matrix
import tf2_geometry_msgs
import numpy as np
np.set_printoptions(suppress=True)
import tf.transformations
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
def homogen2tf(pose,frame):
    # Create a pose stamped message type from the camera image topic.
    object_pose = geometry_msgs.msg.PoseStamped()
    # Only works with a timestamp, timing information is very important in tf
    object_pose.header.stamp = rospy.Time.now()
    # The logical camera always outputs the pose of an object it its own
    # reference frame and here it is called logical_camera1_frame
    # If we have more than one logical camera, this name will change
    object_pose.header.frame_id = frame
    object_pose.pose.position.x = pose[0][3]
    object_pose.pose.position.y =pose[1][3]
    object_pose.pose.position.z = pose[2][3]
    quat=tf.transformations.quaternion_from_matrix(pose)
    object_pose.pose.orientation.x = quat[0]
    object_pose.pose.orientation.y = quat[1]
    object_pose.pose.orientation.z = quat[2]
    object_pose.pose.orientation.w = quat[3]

    return object_pose
def pose2homogen(pose):
    matrix=np.zeros((3,4))
    matrix = np.vstack(( matrix, np.array([0, 0, 0, 1]))) # to homogenous coordinates   
    q=np.array([pose.pose.orientation.x,
                pose.pose.orientation.y,
                pose.pose.orientation.z,
                pose.pose.orientation.w])

    matrix[0][3]= pose.pose.position.x
    matrix[1][3]=pose.pose.position.y
    matrix[2][3]=pose.pose.position.z

    rotm=quaternion_matrix(q)
    matrix[:3, :3]=rotm[:3, :3]

    return matrix

def callback(data):
    
    TWC=data
    TWC=pose2homogen(data)
    TCT=homogeneous_transform
    TWT=np.matmul((TCT),TWC)
    TBT=np.load("/home/hamza/ros_ws/src/intention_application/src/numpyfiles/currentpose.npy")
    TWB=np.matmul((TBT),TWT)
    tool=homogen2tf(TWB,"base")
    tool.header.stamp = rospy.Time.now()
    rospy.sleep(1)
    #object_world_pose = tf_buffer.transform(tool, "moveit")


    object=tool

    #print(object)
    object.pose.position.z= 0.3067349934015076
    object.pose.position.x= 0.11+object.pose.position.x
    #object.pose.position.y= object.pose.position.y-0.06

    group.set_pose_target(object)
    print("tool")
    print(object)
    print("tool")


    # `go()` returns a boolean indicating whether the planning and execution was successful.
    success = group.go(wait=True)
    print(success)
    # Calling `stop()` ensures that there is no residual movement
    group.stop()
    rospy.sleep(0.3)

    # It is always good to clear your targets after planning with poses.
    # Note: there is no equivalent function for clear_joint_value_targets().
    group.clear_pose_targets()   # print(object_world_pose)
    print(group.get_current_pose())
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    rospy.Subscriber('intentionapplication/pose', geometry_msgs.msg.PoseStamped, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('listenesjsjs', anonymous=True)

    moveit_commander.roscpp_initialize(sys.argv)

    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)

    rospy.sleep(4)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    print(scene)
    group_name = "manipulator"
    group = moveit_commander.MoveGroupCommander(group_name)

    #robot.setMaxVelocityScalingFactor(1)


    rotation = np.array([
        [0.22108477, -0.97150638, 0.08542181],
        [0.97500083, 0.22217576, 0.00336374],
        [-0.02224655, 0.08254266, 0.9963392]
    ])

    translation = np.array([
        [0.1095592],
        [-0.00816192],
        [-0.17505415]
    ])


    homogeneous_transform = np.concatenate((np.load("/home/hamza/ros_ws/src/intention_application/src/handeyecalibration/rotation.npy"), np.load("/home/hamza/ros_ws/src/intention_application/src/handeyecalibration/translation.npy")), axis=1)
    homogeneous_transform = np.vstack((homogeneous_transform, [0, 0, 0, 1]))

    listener()
