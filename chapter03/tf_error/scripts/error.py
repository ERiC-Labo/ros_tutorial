#!/usr/bin/env python
import rospy
import tf
import math
import geometry_msgs

rospy.init_node('fe', anonymous=True)
groud_trans = geometry_msgs.msg.Transform()
groud_trans.translation.x = 3.0683e-08
groud_trans.translation.y = -5.40694e-09
groud_trans.translation.z = 4.33466e-05
groud_trans.rotation.x = 8.0067e-5
groud_trans.rotation.y = 0.000578918
groud_trans.rotation.z = 5.47673e-08
groud_trans.rotation.w = 1
gt = groud_trans.translation
q = groud_trans.rotation
groud_rpy = tf.transformations.euler_from_quaternion((q.x, q.y, q.z, q.w))

esti_trans = geometry_msgs.msg.Transform()
esti_trans.translation.x = 0.000704181
esti_trans.translation.y = -0.000498243
esti_trans.translation.z = -0.00780724
esti_trans.rotation.x = -0.612202
esti_trans.rotation.y = 0.471101
esti_trans.rotation.z = 0.612556
esti_trans.rotation.w = -0.16678
et = esti_trans.translation
q = esti_trans.rotation
esti_rpy = tf.transformations.euler_from_quaternion((q.x, q.y, q.z, q.w))

error = []
error.append(gt.x - et.x)
error.append(gt.y - et.y)
error.append(gt.z - et.z)
for i in range(3):
    error.append((groud_rpy[i] - esti_rpy[i])*180/math.pi)

for i in range(6):
    print(error[i])
