#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(msg):  #callback function
    rospy.loginfo(msg.data)

if __name__=='__main__':
    rospy.init_node('node')
    sub = rospy.Subscriber('/chatter', String, callback)#Define subscriber rospy.Subscriber(topic_name, topic_type, callback_function)
    rospy.spin()#Execiting callback function

