cmake_minimum_required(VERSION 3.0.2)
project(plugin_first)
add_compile_options(-std=c++14)

find_package(catkin REQUIRED COMPONENTS
  pluginlib
  roscpp
  rospy
  many_message
)


catkin_package(
  INCLUDE_DIRS include
  LIBRARIES plugin_first
  CATKIN_DEPENDS pluginlib roscpp rospy
#  DEPENDS system_lib
)

include_directories(
 include
  ${catkin_INCLUDE_DIRS}
)

add_library(${PROJECT_NAME} src/yes_base.cpp src/yes_sum.cpp)
add_dependencies(${PROJECT_NAME} ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(${PROJECT_NAME} ${catkin_LIBRARIES})

