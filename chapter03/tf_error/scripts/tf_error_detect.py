#!/usr/bin/env python
import rospy
import tf
import tf2_ros


if __name__ == '__main__':
    rospy.init_node('node_name', anonymous=True)
    
    listener = tf.TransformListener()
    buffer = tf2_ros.Buffer()

    loop = rospy.Rate(100)
    while not rospy.is_shutdown():
        try:
            #(trans, rot) = listener.lookupTransform("/photoneo_center", "/HV8", rospy.Time.now())
            trans = buffer.lookup_transform('world', 'HV8', rospy.Time())
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            print("not come")
            loop.sleep()
            continue

        dof6_xyz = trans.transform.translation
        quaternion = trans.transform.rotation
        dof6_rpy = tf.transformations.euler_from_quaternion((quaternion.x, quaternion.y, quaternion.z, quaternion.w))
        print("error ::  x=" + dof6_xyz.x + " y=" + dof6_xyz.y + " z=" + dof6_xyz.z + " roll=" + dof6_rpy[0] + " pitch=" + dof6_rpy[1] + " yaw=" + dof6_rpy[2])
        loop.sleep()
