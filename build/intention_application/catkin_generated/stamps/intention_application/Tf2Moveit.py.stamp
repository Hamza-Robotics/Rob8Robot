#!/usr/bin/env python
import rospy

# to get commandline arguments
import sys
from tf.transformations import quaternion_matrix, quaternion_from_matrix

# because of transformations
import tf
import numpy as np
import tf2_ros
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

matrix=np.load("/home/hamza/ros_ws/src/intention_application/src/handeyecalibration/tf2moveit.npy")

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


matrix=np.linalg.inv(matrix)
#!/usr/bin/env python
import roslib

import rospy
import tf

if __name__ == '__main__':

    rospy.init_node('fixed_tf_broadcaster')
    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.sleep(3)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "manipulator"
    group = moveit_commander.MoveGroupCommander(group_name)
    (group.get_current_pose())
    (group.get_current_pose())
    R1=tf2homogen(tf_buffer.lookup_transform("base","tool0_controller",rospy.Duration(0)))
    R2=pose2homogen(group.get_current_pose())
    matrix =(np.matmul(R2, np.linalg.inv(R1)))
    
    
    print(R2)
    print(np.matmul((matrix),R1))
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():

        
        matrix=np.load("/home/hamza/ros_ws/src/intention_application/src/handeyecalibration/tf2moveit.npy")

        br = tf.TransformBroadcaster()


        quat=tf.transformations.quaternion_from_matrix(matrix)

        br.sendTransform((  matrix[0][3], matrix[1][3], matrix[2][3]),
                         (quat[0],quat[1],quat[2],quat[3]),
                         rospy.Time.now(),
                         "moveit",
                         "tool0_controller")
        rate.sleep()
