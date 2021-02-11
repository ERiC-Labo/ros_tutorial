#!/usr/bin/env python
import sys
import moveit_commander
import rospy
import moveit_msgs
import tf
from math import pi
import copy
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import Quaternion
import geometry_msgs.msg

if __name__== '__main__':
    rospy.init_node('moveit_node')
    moveit_commander.roscpp_initialize(sys.argv)
    group = moveit_commander.MoveGroupCommander("manipulator")
   
    xyz_step = 0.05  #1cm
    degree = 2
    rpy_step = degree * pi / 180#5 degree

    while 1:
        print('(a) +x (d) -x (q) +y (z) -y (e) +z (x) -z ')
        print('(r) +roll (c) -roll (t) +pitch (v) -pitch (y) +yaw (b) -yaw (n) quit')
        
        wpose = group.get_current_pose().pose
        wq = wpose.orientation
        euler = tf.transformations.euler_from_quaternion((wq.x, wq.y, wq.z, wq.w))
        roll = euler[0]
        pitch = euler[1]
        yaw = euler[2]
        key = input().strip()
        if key == 'a':
            wpose.position.x += xyz_step
        elif key == 'd':
            wpose.position.x = wpose.position.x - xyz_step
        elif key == 'q':
            wpose.position.y = wpose.position.y + xyz_step
        elif key == 'z':
            wpose.position.y = wpose.position.y - xyz_step
        elif key == 'e':
            wpose.position.z = wpose.position.z + xyz_step
        elif key == 'x':
            wpose.position.z = wpose.position.z - xyz_step
        elif key == 'r':
            roll = roll + rpy_step
        elif key == 'c':
            roll = roll - rpy_step
        elif key == 't':
            pitch = pitch + rpy_step
        elif key == 'v':
            pitch = pitch - rpy_step
        elif key == 'y':
            yaw = yaw + rpy_step
        elif key == 'b':
            yaw = yaw - rpy_step
        else:
            break
        q = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
        wpose.orientation.x = q[0]
        wpose.orientation.y = q[1]
        wpose.orientation.z = q[2]
        wpose.orientation.w = q[3]
        waypoints = []
        waypoints.append(copy.deepcopy(wpose))
        
        (plan, fraction) = group.compute_cartesian_path(
            waypoints,
            0.01,
            0.0
        )
        group.execute(plan, wait=True)

    

    
        

    