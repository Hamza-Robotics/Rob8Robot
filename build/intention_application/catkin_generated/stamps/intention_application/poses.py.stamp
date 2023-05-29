import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

geometry_msgs.msg
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial',
                anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "manipulator"
group = moveit_commander.MoveGroupCommander(group_name)


pose_goal = geometry_msgs.msg.Pose()
pose_goal.position.x = 0.7303241647724765
pose_goal.position.y = 0.7309555761323018
pose_goal.position.z = 0.3533808086501359
pose_goal.orientation.x = -0.6965137531107767
pose_goal.orientation.y = -0.23789428109642932
pose_goal.orientation.z = 0.33790720101734645
pose_goal.orientation.w = 0.5865949422299651


group.set_pose_target(pose_goal)
success = group.go(wait=True)
# Calling `stop()` ensures that there is no residual movement
group.stop()
# It is always good to clear your targets after planning with poses.
# Note: there is no equivalent function for clear_joint_value_targets().
group.clear_pose_targets()





current_pose=group.get_current_pose()
current_pose=group.get_current_pose()
rospy.sleep(2)
current_pose=group.get_current_pose()

print(current_pose)