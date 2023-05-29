
import rospy
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
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
import actionlib
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list




def pickupper(data):
    if True:

    # Check if the logical camera has seen our box which has the name 'object'.          
        # Create a pose stamped message type from the camera image topic.
        object_pose = geometry_msgs.msg.PoseStamped()
        # Only works with a timestamp, timing information is very important in tf
        object_pose.header.stamp = rospy.Time.now()
        # The logical camera always outputs the pose of an object it its own
        # reference frame and here it is called logical_camera1_frame
        # If we have more than one logical camera, this name will change
        object_pose.pose.position.x = -582
        object_pose.pose.position.y = -682
        object_pose.pose.position.z = 26
        object_pose.pose.orientation.x = 0.8188359
        object_pose.pose.orientation.y = 0.2580991
        object_pose.pose.orientation.z = 0.4577985
        object_pose.pose.orientation.w = 0.2308965
        
        moveit_commander.roscpp_initialize(sys.argv)
        robot_arm_group = moveit_commander.MoveGroupCommander("manipulator")
        robot_arm_client=actionlib.SimpleActionClient(
                    "execute_trajectory",moveit_msgs.msg.ExecuteTrajectoryAction)
        waypoints=[]
        current_pose=robot_arm_group.get_current_pose()
        rospy.sleep(0.5)
        current_pose=robot_arm_group.get_current_pose()

        waypoints.append(current_pose.pose)
        waypoints.append(object_pose.pose) 
        fraction =0
        for count_cartesian_plan in range(0,3):
                if fraction < 1.0:
                    (plan_cartesian,fraction)=robot_arm_group.compute_cartesian_path(
                        waypoints,
                        0.1,
                        0 
                    )
                else:
                    break
                
        robot_arm_goal=moveit_msgs.msg.ExecuteTrajectoryGoal()
        robot_arm_goal.trajectory=plan_cartesian
        robot_arm_client.send_goal(robot_arm_goal)
        robot_arm_client.wait_for_result()

        print("Here")


            






if __name__ == '__main__':
    print('========================================')
    # Initialize ROS node to transform object pose.
    print("Initializing node ...")
    rospy.init_node('pickup', anonymous=True)


    # Subscribe to the logical camera topic.
    print("Subscribing to logical camera ...")
    rospy.Subscriber('chatter' ,String,callback=pickupper)
    
    rospy.spin()
