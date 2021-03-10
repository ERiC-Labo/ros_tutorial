cmake_minimum_required(VERSION 3.0.2)
project(many_message)

find_package(catkin REQUIRED
    message_generation
)

add_message_files(
    FILES 
    array.msg
)
generate_messages(
    DEPENDENCIES
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES many_message
    CATKIN_DEPENDS  message_runtime
#  DEPENDS system_lib
)

include_directories(
 include
 ${catkin_INCLUDE_DIRS}
)
