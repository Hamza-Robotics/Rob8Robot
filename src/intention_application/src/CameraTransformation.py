#!/usr/bin/env python
import rospy

# to get commandline arguments
import sys

# because of transformations
import tf
import numpy as np
import tf2_ros
import geometry_msgs.msg

rotation_matrix=np.load("/home/hamza/ros_ws/src/intention_application/src/handeyecalibration/rotation.npy")
translation=np.load("/home/hamza/ros_ws/src/intention_application/src/handeyecalibration/translation.npy")


#!/usr/bin/env python
import roslib

import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('fixed_tf_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        matrix = np.array([[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 1]],
                        dtype=float)
        matrix[:3, :3] = rotation_matrix




        quat=tf.transformations.quaternion_from_matrix(matrix)

        br.sendTransform((translation[0,0], translation[1,0], translation[2,0]),
                         (quat[0],quat[1],quat[2],quat[3]),
                         rospy.Time.now(),
                         "camera_link",
                         "tool0_controller")
        rate.sleep()
