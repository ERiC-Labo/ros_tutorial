# arm_tutorial

## Please command
```
mkdir -p ~/ros_package/ur_ws/src
cd ~/ros_package/ur_ws/src
git clone https://github.com/ericlab/arm_tutorial
cd ..
rosdep update
rosdep install --from-paths src --ignore-src -r -y
catkin build

source ~/ros_package/ur_ws/devel/setup.bash
roslanch ur_gazebo ur3.launch
```
### Other terminal
```
python ~/ros_package/ur_ws/src/arm_tutorial/python_file/arm_control.py
```

## Please register local repository
```
rm -r -f ~/ros_package/ur_ws/src/*
cd ~/ros_package/ur_ws/src
git init
git remote add origin https://github.com/ericlab/arm_tutorial
git pull origin main
git branch -M main
catkin build
```
## Download command is
```
cd ~/ros_package/ur_ws/src
git pull origin main
```

## Upload command  is
```
cd ~/ros_package/ur_ws/src
git add .
git commit -m "(Your favorite name)"
git push -u origin main
```

## Go to next tutorial
[Chapter2](https://github.com/tsuchidashinya/arm_tutorial/tree/main/chapter02)