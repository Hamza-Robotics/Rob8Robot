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

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial',
                anonymous=True)

tf_buffer = tf2_ros.Buffer()
tf_listener = tf2_ros.TransformListener(tf_buffer)

rospy.sleep(3)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
print(scene)
group_name = "manipulator"
group = moveit_commander.MoveGroupCommander(group_name)
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

while True:

    TWC=np.load("/home/hamza/ros_ws/src/intention_application/src/numpyfiles/grasppose.npy")
    TCT=np.load("/home/hamza/ros_ws/src/intention_application/src/numpyfiles/c2t.npy")
    TWT=np.matmul((TCT),TWC)
    TBT=np.load("/home/hamza/ros_ws/src/intention_application/src/numpyfiles/currentpose.npy")
    TWB=np.matmul((TBT),TWT)
    tool=homogen2tf(TWB,"base")
    tool.header.stamp = rospy.Time.now()
    print("tool")
    print(tool)
    print("tool")
    object=tool

    print(group.get_current_pose())

    #print(object)
    object.pose.position.z= 0.2567349934015076
    object.pose.position.x= 0.11+object.pose.position.x
    object.pose.position.y= object.pose.position.y-0.06

    group.set_pose_target(object)



    # `go()` returns a boolean indicating whether the planning and execution was successful.
    success = group.go(wait=True)
    print(success)
    # Calling `stop()` ensures that there is no residual movement
    group.stop()
    # It is always good to clear your targets after planning with poses.
    # Note: there is no equivalent function for clear_joint_value_targets().
    group.clear_pose_targets()   # print(object_world_pose)
    print(group.get_current_pose())