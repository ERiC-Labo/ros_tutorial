#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

if __name__=='__main__':
    rospy.init_node('node_name') #You have to write initially in ROS main function

    pub = rospy.Publisher('/chatter', String, queue_size=10) #Define message publisher rospy.Publisher('topic_name', Topic_type, queue_size(optinally))
    message = String()  #Construct the String class
    count = 0
    loop_rate = rospy.Rate(10) #10Hz loop step
    while not rospy.is_shutdown():
        count = count + 1
        message.data = str(count) + "message content"  #Making message data contents
        rospy.loginfo(message.data) #Express the str date on console
        pub.publish(message)  #Sending message(Publsihe message)
        loop_rate.sleep()  #Sleep until starting next loop

