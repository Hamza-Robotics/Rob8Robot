import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import open3d as o3d
import numpy as np

import message_filters





class HelperFunction():
    def callback(rgb : Image, depth : Image):
        cv_bridge = CvBridge()
        rgb_img = cv_bridge.imgmsg_to_cv2(rgb, "rgb8")
        depth_img = cv_bridge.imgmsg_to_cv2(depth, "16UC1")
        mtx= np.array([[570.3405082258201, 0.0, 319.5], [0.0, 570.3405082258201, 239.5], [0.0, 0.0, 1.0]])
        Im_Rgbd=o3d.geometry.RGBDImage.create_from_color_and_depth(o3d.geometry.Image(rgb_img), o3d.geometry.Image(depth_img),convert_rgb_to_intensity=False)
        intrinsic=o3d.camera.PinholeCameraIntrinsic(640,480 ,mtx[0][0],mtx[1][1],mtx[0][2],mtx[1][2])
        np.save("numpyfolder/intrincis.npy",intrinsic)

    def ImageFeed():
        rospy.init_node("Camera_Feed",anonymous=True)
        rgb_sub=message_filters.Subscriber("camera/color/image_raw",Image)
        depth_sub = message_filters.Subscriber('/camera/depth/image_raw', Image)
        ts = message_filters.ApproximateTimeSynchronizer([rgb_sub,depth_sub],10,1)
        ts.registerCallback(callback)