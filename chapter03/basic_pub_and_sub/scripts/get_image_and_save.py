#!/usr/bin/env python
import cv2
import cv_bridge
from sensor_msgs.msg import Image
import rospy

if __name__=='__main__':
    rospy.init_node('node')
    img = rospy.wait_for_message('image_1', Image)
    img_cv = cv_bridge.CvBridge().imgmsg_to_cv2(img)
    cv2.imshow('image', img_cv)
    cv2.waitKey(3000)
    cv2.imwrite('../file/image' + str(rospy.Time.now()) + '.jpg', img_cv)
    cv2.destroyAllWindows()