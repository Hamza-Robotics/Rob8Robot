
#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import random
def callback(rgb : Image):

    cv_bridge = CvBridge()
    rgb_img = cv_bridge.imgmsg_to_cv2(rgb, "rgb8")
    cv2.imshow("rgb",rgb_img)
    cv2.waitKey(5)
    cv2.imwrite("intention_application/src/CameraCalibration/image/"+str(random.randint(0,100000))+".png",rgb_img)
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/camera/color/image_raw", Image, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
