import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String 

import std_msgs.msg

from moveit_commander.conversions import pose_to_list

def posegiver():
    rospy.init_node("posegiver", anonymous=True)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "manipulator"
    group = moveit_commander.MoveGroupCommander(group_name)
    

    current_pose=group.get_current_pose()
    current_pose=group.get_current_pose()

    print(type(current_pose))
    rate = rospy.Rate(10) # 10
    while not rospy.is_shutdown():
        pub = rospy.Publisher('intentionapplication/handeyecalibration/posegiver', geometry_msgs.msg.PoseStamped, queue_size=2)
        moveit_commander.roscpp_initialize(sys.argv)


        robot = moveit_commander.RobotCommander()
        scene = moveit_commander.PlanningSceneInterface()
        group_name = "manipulator"
        #group.set_pose_reference_frame("base_link")
        group = moveit_commander.MoveGroupCommander(group_name)

        current_pose=group.get_current_pose()
        current_pose=group.get_current_pose()
        current_pose=group.get_current_pose()
        pub.publish(current_pose)
        rate.sleep()

if __name__ == '__main__':
    try:
        posegiver()
    except rospy.ROSInterruptException:
            pass


