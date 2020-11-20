cmake_minimum_required(VERSION 3.0.2)
project(algorithm)


find_package(catkin REQUIRED COMPONENTS
  message_generation
  rospy
  std_msgs
)
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES algorithm
  CATKIN_DEPENDS rospy std_msgs
#  DEPENDS system_lib
)

