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
def homogen2tf(pose,frame):
    # Create a pose stamped message type from the camera image topic.
    object_pose = geometry_msgs.msg.PoseStamped()
    # Only works with a timestamp, timing information is very important in tf
    object_pose.header.stamp = rospy.Time.now()
    # The logical camera always outputs the pose of an object it its own
    # reference frame and here it is called logical_camera1_frame
    # If we have more than one logical camera, this name will change

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
    
    
    matrix[0][3]= -0.558827336721005
    matrix[1][3]= 0.2751496506182364
    matrix[2][3]=0.2528180601089223

    rotm=quaternion_matrix(q)
    matrix[:3, :3]=rotm[:3, :3]

    return matrix


def callback(pose: geometry_msgs.msg.PoseStamped):

    
    rospy.sleep(1)

    TCT=np.load("/home/hamza/ros_ws/src/intention_application/src/numpyfiles/c2t.npy")
    TWC=pose2homogen(pose)

    TWT=np.matmul((TCT),TWC)
    #current_pose=tf_buffer.lookup_transform_full("base",rospy.Duration(0),"tool0_controller",rospy.Duration(0),"base")
    #TBT=tf2homogen(current_pose)

    TBT=np.load("/home/hamza/ros_ws/src/intention_application/src/numpyfiles/currentpose.npy")
    TWB=np.matmul((TBT),TWT)
    tool=homogen2tf(TWB,"tool0_controller")
    tool.pose.position.z=0.30

    R1=tf2homogen(tf_buffer.lookup_transform("base","tool0_controller",rospy.Duration(0)))
    R2=pose2homogen(group.get_current_pose())
    matrix =(np.matmul(R2, np.linalg.inv(R1)))

    GOAL=(np.matmul((matrix),pose2homogen(tool)))
    goal=homogen2tf(GOAL,"camera_link")


    moveit=geometry_msgs.msg.Pose()
    moveit.position.x=goal.pose.position.x 
    moveit.position.y=goal.pose.position.y
    moveit.position.z=goal.pose.position.z 
    moveit.orientation.x=goal.pose.orientation.x
    moveit.orientation.y=goal.pose.orientation.y
    moveit.orientation.z=goal.pose.orientation.z
    moveit.orientation.w=goal.pose.orientation.w
    print(moveit)
    group.set_pose_target(moveit)
    # `go()` returns a boolean indicating whether the planning and execution was successful.
    success = group.go(wait=True)
    print(success)
    # Calling `stop()` ensures that there is no residual movement
    group.stop()
    # It is always good to clear your targets after planning with poses.
    # Note: there is no equivalent function for clear_joint_value_targets().
    group.clear_pose_targets()   # print(object_world_pose)


def listener():
    rospy.Subscriber("intentionapplication/pose", geometry_msgs.msg.PoseStamped, callback)
    rospy.spin()

if __name__ == '__main__':
    moveit_commander.roscpp_initialize(sys.argv)
 

    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "manipulator"
    group = moveit_commander.MoveGroupCommander(group_name)
    # Initialize ROS node to transform object pose.
    print("Initializing node ...")
    rospy.init_node('transform_object_poses', anonymous=True)

    # Create a TF buffer in the global scope
    print("Creating tf buffer ...")
    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    
    listener()
