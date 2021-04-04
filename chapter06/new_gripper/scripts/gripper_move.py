#!/usr/bin/env python3
 
import rospy
import actionlib
import control_msgs.msg
 
rospy.init_node('gripper_control')
 
# Create an action client
client = actionlib.SimpleActionClient(
    '/left_hand/gripper_cmd',  # namespace of the action topics
    control_msgs.msg.GripperCommandAction # action type
)

    
# Wait until the action server has been started and is listening for goals
client.wait_for_server()

value = rospy.get_param('~value', 0.005)
# Create a goal to send (to the action server)
goal = control_msgs.msg.GripperCommandGoal()
goal.command.position = value   # From 0.0 to 0.8
goal.command.max_effort = -1.0  # Do not limit the effort
feedback = control_msgs.msg.GripperCommandFeedback()
feedback.position
client.send_goal(goal)
 

client.wait_for_result()



