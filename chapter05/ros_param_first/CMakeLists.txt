cmake_minimum_required(VERSION 3.0.2)
project(ros_param_first)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES ros_param_first
#  CATKIN_DEPENDS roscpp rospy
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(param_display src/param_display.cpp)
target_link_libraries(param_display
  ${catkin_LIBRARIES}
)

add_executable(param2_display src/param2_display.cpp)
target_link_libraries(param2_display
  ${catkin_LIBRARIES}
)