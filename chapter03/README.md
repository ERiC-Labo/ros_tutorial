# chapter03
## basic_pub_and_sub
### Initially
```
echo "source (your ros workspace folder)/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
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
roslanch basic_rviz express_urdf.launch
```
<img src="https://github.com/tsuchidashinya/arm_tutorial/blob/main/file/img/chapter03/image_1.png">

```
roslanch basic_rviz express_xacro.launch
```
<img src="https://github.com/tsuchidashinya/arm_tutorial/blob/main/file/img/chapter03/image_2.png">

# basic gazebo

# Next tutorial
<a href="https://github.com/tsuchidashinya/arm_tutorial/tree/main/chapter04">Chapter04</a>