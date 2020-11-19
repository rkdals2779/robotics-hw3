cmake_minimum_required(VERSION 3.0.2)
project(common_msgs)


find_package(catkin REQUIRED COMPONENTS
  message_generation
  rospy
  std_msgs
)
# Generate services in the 'srv' folder
add_service_files(
  FILES
  BatteryNum.srv
)
# Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
)
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES common_msgs
  CATKIN_DEPENDS rospy std_msgs
#  DEPENDS system_lib
)

