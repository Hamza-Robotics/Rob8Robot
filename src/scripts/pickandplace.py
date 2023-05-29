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

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "manipulator"
group = moveit_commander.MoveGroupCommander(group_name)

# Create a pose stamped message type from the camera image topic.
object_pose = geometry_msgs.msg.Pose()
# Only works with a timestamp, timing information is very important in tf

object_pose.position.x = 0.23537374431096877
object_pose.position.y = 1.2309258699273016
object_pose.position.z = 0.5485446726166426
object_pose.orientation.x = -0.6975862465709212
object_pose.orientation.y =  0.046367294905580086
object_pose.orientation.z =  0.6781228205274983
object_pose.orientation.w = 0.22665600110754452

group.set_pose_target(object_pose)
for i in range(10):
    plan = group.go(wait=True)
    rospy.sleep(1)
# Calling `stop()` ensures that there is no residual movement
group.stop()
# It is always good to clear your targets after planning with poses.
# Note: there is no equivalent function for clear_joint_value_targets()
group.clear_pose_targets()


# The logical camera always outputs the pose of an object it its own
# reference frame and here it is called logical_camera1_frame
# If we have more than one logical camera, this name will change
current_pose=group.get_current_pose()
current_pose=group.get_current_pose()
rospy.sleep(2)
current_pose=group.get_current_pose()

print(current_pose)