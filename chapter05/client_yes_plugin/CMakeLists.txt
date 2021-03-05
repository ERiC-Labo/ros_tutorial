cmake_minimum_required(VERSION 3.0.2)
project(client_yes_plugin)


find_package(catkin REQUIRED
    pluginlib
    roscpp
    many_message
    plugin_first
)

catkin_package(
#  INCLUDE_DIRS include
  LIBRARIES client_yes_plugin
  CATKIN_DEPENDS pluginlib 
#  DEPENDS system_lib
)

include_directories(
 include
 ${catkin_INCLUDE_DIRS}
)

add_executable(${PROJECT_NAME} src/yes_client.cpp src/yes_node.cpp)
add_dependencies(${PROJECT_NAME} ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(${PROJECT_NAME}
    ${catkin_LIBRARIES}
)
