# Operate robot by mouse

First, register the ROS_PACKAGE_PATH by command
```
source ~/ros_package/ur_ws/devel/setup.bash
```
If you want to register all time
```
echo "source ~/ros_package/ur_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

### Setup the simulator
```
roslaunch ur_e_gazebo ur3e.launch
```

### Setup the moveit
```
roslaunch ur3_e_moveit_config ur3_e_moveit_planning_execution.launch sim:=true
```

### Setup the rviz
```
roslaunch ur3_e_moveit_config moveit_rviz.launch config:=true
```

<img src="https://github.com/ERiC-Labo/ros_tutorial/blob/main/file/img/chapter02/output_1.gif">

## Next page
<a href="https://github.com/ERiC-Labo/ros_tutorial/tree/main/chapter03">Chapter03</a>
