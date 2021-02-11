#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import TwistStamped
import random

class Class_Subscriber:
    def __init__(self, topic_name):
        self.sub = rospy.Subscriber(topic_name, TwistStamped, self.sub_callback)
        self.f = open('/home/tsuchidashinya/twiststamp.txt', 'w')

    def sub_callback(self, msg):
        self.f.write(str(msg) + '\n')
        rospy.loginfo(msg)

if __name__=='__main__':
    rospy.init_node('node')
    Class_Subscriber('first_topic')
    rospy.spin()
