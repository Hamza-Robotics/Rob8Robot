import socket
import pickle
import cv2
import os
from intention_application.msg import Array
from intention_application.msg import Array 

class Client:
    def __init__(self):
        # Connect to server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(("192.168.0.102", 12347))

    def send_robot_image_path(self, path):
        # Load and send image
        img = cv2.imread(path)
        data = pickle.dumps(img)
        # Send the size of the data first
        self.s.sendall(len(data).to_bytes(4, byteorder='big'))
        self.s.sendall(data)

    def send_robot_image(self, img):
        data = pickle.dumps(img)
        # Send the size of the data first
        self.s.sendall(len(data).to_bytes(4, byteorder='big'))
        self.s.sendall(data)

    def recv_data(self):
        data = self.s.recv(1024)
        if data:
            x, y, boolean = pickle.loads(data)
            print(x, y, boolean)
            return x, y, boolean
        return None, None, None

import random
#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import numpy as np
from intention_application.msg import Array

def talker(client):
    rgb_img=np.load((os.path.dirname(os.path.abspath(__file__))+"/numpyfiles/"+"imagergb.npy"))
    cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
    print(rgb_img)
    #client.send_robot_image(rgb_img)

    pub = rospy.Publisher('chatter', Array, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    print("here")
    while True:
        #x,y,intention=client.recv_data()
        data=Array()
  
        intention=0
        data.x=random.randint(0,400)
        data.y=random.randint(0,400)
        data.intention=bool(intention)
        pub.publish(data)
        rospy.sleep(1)
        rate.sleep()

if __name__ == '__main__':
    client=2
    #client = Client()
    try:
        talker(client)
    except rospy.ROSInterruptException:
        pass
