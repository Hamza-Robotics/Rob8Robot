import rospy 
import open3d as o3d
import numpy as np
import os
import cv2
import random
import rospy
import tf2_ros
import tf2_geometry_msgs
import tf
import geometry_msgs
import sys
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
import actionlib
from std_msgs.msg import String
from sensor_msgs.msg import Image

from moveit_commander.conversions import pose_to_list
from tf.transformations import quaternion_matrix, quaternion_from_matrix



import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
import actionlib
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

import rospy
import tf2_ros
import tf2_geometry_msgs
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
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
import actionlib
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from intention_application.msg import Array
def coordinatesystem(length):
    l=length
    x=np.zeros((l,3))
    x[:,0]=np.linspace(0,1, num=l)
    X = o3d.geometry.PointCloud()
    X.points = o3d.utility.Vector3dVector(x)
    X.paint_uniform_color([1, 0, 0])

    y=np.zeros((l,3))
    y[:,1]=np.linspace(0,1, num=l)
    Y = o3d.geometry.PointCloud()
    Y.points = o3d.utility.Vector3dVector(y)
    Y.paint_uniform_color([0, 1, 0])


    z=np.zeros((l,3))
    z[:,2]=np.linspace(0,1, num=l)
    Z = o3d.geometry.PointCloud()
    Z.points = o3d.utility.Vector3dVector(z)
    Z.paint_uniform_color([0, 0, 1])



    # Pass xyz to Open3D.o3d.geometry.PointCloud and visualize
    return ([X,Y,Z])
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

def xytopointcloud(x,y,Z,w,h,mtx):
    fx=mtx[0,0]
    fy=mtx[1,1]
    cx=mtx[0,2]
    cy=mtx[1,2]
   # x=x-w/2
   # y=y-h/2
    xyz=np.zeros((1,3))
    
    xyz[0,0]=((x-cx)*Z)/fx
    xyz[0,1]=((y-cy))*Z/fy
    xyz[0,2]=Z
    
   #print("PPPPOIIIINT",xyz)

    pcd=o3d.geometry.PointCloud()
    pcd.points=o3d.utility.Vector3dVector(xyz)

    pcd.paint_uniform_color([1,0,0])
    return pcd

def Clustering(pcd,eps,min_points):
    labels = np.array(
        pcd.cluster_dbscan(eps, min_points, print_progress=True))
    max_label = labels.max()
    Clus=[]
    for i in range(max_label):
        id=np.where(labels==i)[0]
        pcl_i=pcd.select_by_index(id)
        Clus.append(pcl_i)

    return Clus

def pointcloud(arr):
    
    #x=arr.x
    #y=arr.y

    #print(x,y)
    #print(type(x),type(y))


    depth_img=np.load((os.path.dirname(os.path.abspath(__file__))+"/numpyfiles/"+"imagedepth.npy"),allow_pickle=True)
    rgb_img=np.load((os.path.dirname(os.path.abspath(__file__))+"/numpyfiles/"+"imagergb.npy"),allow_pickle=True)
    mtx=np.load(os.path.dirname(os.path.abspath(__file__))+"/numpyfiles/"+"mtx.npy")
    print(np.shape(rgb_img))
    #mtx= np.array([[570.3405082258201, 0.0, 319.5], [0.0, 570.3405082258201, 239.5], [0.0, 0.0, 1.0]])
    #sendposetorobot(x,y,mtx,depth_img)

    #cv2.imshow("rgb",rgb_img)
    #cv2.waitKey(0)
    ############ MAKE RGB ###########################
    im_rgbd=o3d.geometry.RGBDImage.create_from_color_and_depth(o3d.geometry.Image(rgb_img), o3d.geometry.Image(depth_img),convert_rgb_to_intensity=False)
    intrinsic=o3d.camera.PinholeCameraIntrinsic(640,480 ,mtx[0][0],mtx[1][1],mtx[0][2],mtx[1][2])
    intrinsic=o3d.camera.PinholeCameraIntrinsic(640,480 ,mtx[0][0],mtx[1][1],mtx[0][2],mtx[1][2])
    pcd=o3d.geometry.PointCloud.create_from_rgbd_image(im_rgbd,intrinsic)
    xyz=coordinatesystem(50)
    #o3d.visualization.draw_geometries([pcd,xyz[0],xyz[1],xyz[2]])   

    ######### SEGMENT CLOUD######################
    plane_model, inliers = pcd.segment_plane(distance_threshold=0.0081,
                                            ransac_n=90,
                                            num_iterations=100)

    pcd = pcd.select_by_index(inliers, invert=True)
    #o3d.visualization.draw_geometries([pcd])   
    Clus=Clustering(pcd,eps=0.008, min_points=40)
    #point_ROI=xytopointcloud(x,y,depth_img[y,x]/1000,depth_img.shape[1],depth_img.shape[0],mtx)
    #print(depth_img[y,x]/1000)
    #print(depth_img[y,x]/1000)

    #o3d.visualization.draw_geometries(Clus)   

    


    for i in range(len(Clus)):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)

        sum=r+g+b
        
        Clus[i].paint_uniform_color([random.randint(0,100)/100,random.randint(0,100)/100,random.randint(0,100)/100])

        #Clus[i]=Clus[i].voxel_down_sample(voxel_size=0.007)

    o3d.visualization.draw_geometries(Clus)   
    #o3d.visualization.draw_geometries(Clus)

    #object_to_be_picked=roicluster(Clus,point_ROI.points)
    print("Hej")
    #pose=grasppose(object_to_be_picked)

    
    
    #rospy.wait_for_message("chatter",Array)


def roicluster(clusters,point):
    
    cost=np.zeros((1,len(clusters)))
    i=0
    for cluster in clusters:
        #print("shape",np.asarray(cluster.points))

        if np.shape(np.asarray(cluster.points))[0]>10:
            mean,_=cluster.compute_mean_and_covariance()
            cost[0,i]=(np.linalg.norm(mean-point))
            i=i+1
            


    
    #print(cost)
    #o3d.visualization.draw_geometries([clusters[np.argmin(cost)]])

    return clusters[np.argmin(cost)]

def grasppose(object):
    xyz = np.asarray(object.points)
    #print("xyzpose",xyz)
    xyz=(np.mean(xyz,axis=0))
    #print(xyz)
    matrix = np.array([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]],
                        dtype=float)
    matrix[0][3]=xyz[0]
    matrix[1][3]=xyz[1]
    matrix[2][3]=xyz[2]

    return matrix

def sendposetorobot(x,y,mtx,rgbd):
        pub = rospy.Publisher('intentionapplication/pose', geometry_msgs.msg.PoseStamped, queue_size=1)
        # Create a pose stamped message type from the camera image topic.
        object_pose = geometry_msgs.msg.PoseStamped()
        # Only works with a timestamp, timing information is very important in tf
        object_pose.header.stamp = rospy.Time.now()
        # The logical camera always outputs the pose of an object it its own
        # reference frame and here it is called logical_camera1_frame
        # If we have more than one logical camera, this name will change
        fx=mtx[0,0]
        fy=mtx[1,1]
        cx=mtx[0,2]
        cy=mtx[1,2]
        Z=(rgbd[x,y])/1000
        if Z > 0.1:
            print(Z,"HHHSH")
            xyz=np.zeros((1,3))
    
            object_pose.header.frame_id = "camera_link"
            object_pose.pose.position.x =((x-cx)*Z)/fx
            object_pose.pose.position.y =((y-cy))*Z/fy
            object_pose.pose.position.z = Z
            quat=tf.transformations.quaternion_from_matrix(np.eye(4))
            object_pose.pose.orientation.x = quat[0]
            object_pose.pose.orientation.y = quat[1]
            object_pose.pose.orientation.z = quat[2]
            object_pose.pose.orientation.w = quat[3]
            #print(object_pose)
            pub.publish(object_pose)
            rospy.sleep(2)
            print(object_pose)
            #object_world_pose = tf_buffer.transform(object_pose, "tool0_controller")
            pozs=pose2homogen(object_pose)
            np.save("/home/hamza/ros_ws/src/intention_application/src/numpyfiles/grasppose.npy",pozs)
            rospy.sleep(2)

def imageprocessing():
    rospy.Subscriber('/camera/depth/image_raw', Image, pointcloud)
    rospy.spin()


if __name__=="__main__":
    rospy.sleep(3)
    rospy.init_node('send_pose', anonymous=True)
    imageprocessing()
    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    
    
    imageprocessing()

    pass