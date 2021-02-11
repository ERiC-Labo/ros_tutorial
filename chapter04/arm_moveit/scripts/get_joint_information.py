#! /usr/bin/env python
import sys
import moveit_commander
import rospy
import tf
import math

if __name__ == '__main__':
    rospy.init_node("moveit_trajectory")
    moveit_commander.roscpp_initialize(sys.argv)
    group = moveit_commander.MoveGroupCommander("manipulator")
    print(group.get_planning_frame())
    print(group.get_end_effector_link())
    print(group.get_current_joint_values())
    print(group.get_current_pose())
    tra = group.get_current_pose().pose.position
    q = group.get_current_pose().pose.orientation
    e = tf.transformations.euler_from_quaternion((q.x, q.y, q.z, q.w))
    deg = 180 / math.pi
    print(tra)
    for i in range(3):
        print(e[i] * deg)
    
    
    
    
   