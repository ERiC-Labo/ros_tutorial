#!/usr/bin/env python3
import rospy
import sensor_msgs
import numpy as np 
import random as rand
import ros_numpy

class Make_image_and_publish:
    def __init__(self, image_topic_name, loop_rate):
        self.pub = rospy.Publisher(image_topic_name, sensor_msgs.msg.Image, queue_size=100)
        loop = rospy.Rate(loop_rate)
        while not rospy.is_shutdown():
            self.make_image()
            self.image_publish()
            loop.sleep()
    
    def make_image(self):
        blank = np.zeros((240, 360, 3))
        blank += [rand.randint(0, 256), rand.randint(0, 256), rand.randint(0, 256)]
        blank = blank.astype(np.uint8)
        self.img = ros_numpy.msgify(sensor_msgs.msg.Image, blank, encoding='rgb8')
        
    def image_publish(self):
        self.pub.publish(self.img)

if __name__=='__main__':
    rospy.init_node('image_publish_node')
    Make_image_and_publish('image_1', 2)

        


