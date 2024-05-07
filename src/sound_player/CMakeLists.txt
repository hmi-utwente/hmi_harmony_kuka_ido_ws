cmake_minimum_required(VERSION 3.0.2)
project(sound_player)

find_package(catkin REQUIRED COMPONENTS rospy)

catkin_package()

install(PROGRAMS src/sound_player_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
