#!/usr/bin/env python
import rospy
from geometry_msgs.msg import TwistStamped
import random

class Class_publsiher:
    def __init__(self, topic_name, loop_r):
        self.pub = rospy.Publisher(topic_name, TwistStamped, queue_size=10)
        self.count = 1
        self.loop = rospy.Rate(loop_r)
        while not rospy.is_shutdown():
            self.count = self.count + 1
            twitst_message = self.make_message()
            self.pub.publish(twitst_message)
            rospy.loginfo(twitst_message)
            self.loop.sleep()
            
    def make_message(self):
        twist_mes = TwistStamped()
        twist_mes.header.frame_id = 'base_link'
        twist_mes.header.stamp = rospy.Time.now()
        twist_mes.header.seq = self.count
        twist_mes.twist.linear.x = random.uniform(0, 1)
        twist_mes.twist.linear.y = random.uniform(0, 1)
        twist_mes.twist.linear.z = random.uniform(0, 1)
        twist_mes.twist.angular.x = random.uniform(0, 1)
        twist_mes.twist.angular.y = random.uniform(0, 1)
        twist_mes.twist.angular.z = random.uniform(0, 1)
        return twist_mes


if __name__=='__main__':
    rospy.init_node('node_32')
    Class_publsiher('first_topic', 10)


        