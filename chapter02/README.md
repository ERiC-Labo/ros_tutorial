# Operate robot by mouse

First, register the ROS_PACKAGE_PATH by command
```
source ~/ros_package/ur_ws/devel/setup.bash
```
If you want to register all time
```
echo "source ~/ros_package/ur_ws/devel/setup.bash" >> ~/.bashrc
```

### Setup the simulator
```
roslanch ur_gazebo ur3.launch
```

### Setup the moveit
```
roslanch ur3_moveit_config ur3_moveit_planning_execution.launch sim:=true
```

### Setup the rviz
```
roslaunch ur3_moveit_config moveit_rviz.launch config:=true
```

<img src="https://github.com/tsuchidashinya/arm_tutorial/blob/main/chapter02/img/output_1.gif">

## Next page
<a href="https://github.com/tsuchidashinya/arm_tutorial/tree/main/chapter03">Chapter03</a>
