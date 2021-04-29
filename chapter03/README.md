# chapter03
## basic_pub_and_sub

### simple_pub simple_sub
```
roscore
```
```
rosrun basic_pub_and_sub simple_publisher.py
```
```
rosrun basic_pub_and_sub simple_subscriber.py
```
You can do message communication

### class type pub and sub
```
roscore
```
```
rosrun basic_pub_and_sub class_publisher.py
```
```
roslaunch basic_pub_and_sub image_view.launch
```
```
rosrun basic_pub_and_sub class_subscriber.py
```
You can show TwistStamp message and please look basic_pub_and_sub/file/twiststamp.txt

### Make color image publishesr and saving subscriber
```
roscore
```
```
rosrun basic_pub_and_sub make_image_and_pub.py
```
```
rosrun basic_pub_and_sub get_image_and_save.py
```





## basic rviz
```
roslaunch basic_rviz express_urdf.launch
```
<img src="https://github.com/ERiC-Labo/ros_tutorial/blob/main/file/img/chapter03/image_1.png">

```
roslaunch basic_rviz express_xacro.launch
```
<img src="https://github.com/ERiC-Labo/ros_tutorial/blob/main/file/img/chapter03/image_2.png">

# basic gazebo
```
roslaunch basic_gazebo simple_box.launch
```
<img src="https://github.com/ERiC-Labo/ros_tutorial/blob/main/file/img/chapter03/image_3.png">

# Next tutorial
<a href="https://github.com/ERiC-Labo/ros_tutorial/tree/main/chapter04">Chapter04</a>