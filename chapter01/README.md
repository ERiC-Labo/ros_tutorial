# arm_tutorial

Please execute in ros **noetic**
## install catkin 
```
sudo apt install python3-catkin-tools
sudo apt install python3-catkin-pkg
sudo apt install python3-osrf-pycommon
```
## Please command
```
mkdir -p ~/ros_package/ur_ws/src
cd ~/ros_package/ur_ws/src
git clone https://github.com/ERiC-Labo/ros_tutorial
cd ..
rosdep update
rosdep install --from-paths src --ignore-src -r -y
catkin build

source ~/ros_package/ur_ws/devel/setup.bash
roslaunch ur_e_gazebo ur3e.launch
```
### Other terminal
```
python3 ~/ros_package/ur_ws/src/ros_tutorial/chapter01/python_file/arm_control.py
```

## Please register local repository(GitHub)
```
rm -r -f ~/ros_package/ur_ws/src/*
cd ~/ros_package/ur_ws/src
git init
git remote add origin https://github.com/ERiC-Labo/ros_tutorial
git pull origin main
git branch -M main
catkin build
```
## Download command is
```
cd ~/ros_package/ur_ws/src
git pull origin main
```

## Upload command  is(GitHub)
```
cd ~/ros_package/ur_ws/src
git add .
git commit -m "(Your favorite name)"
git push -u origin main
```

## Go to next tutorial
[Chapter2](https://github.com/ERiC-Labo/ros_tutorial/tree/main/chapter02)