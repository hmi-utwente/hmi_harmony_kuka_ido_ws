# Install script for directory: /home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/control_msgs/control_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/control_msgs/action" TYPE FILE FILES
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/control_msgs/control_msgs/action/FollowJointTrajectory.action"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/control_msgs/control_msgs/action/GripperCommand.action"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/control_msgs/control_msgs/action/JointTrajectory.action"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/control_msgs/control_msgs/action/PointHead.action"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/control_msgs/control_msgs/action/SingleJointPosition.action"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/control_msgs/msg" TYPE FILE FILES
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/FollowJointTrajectoryAction.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/FollowJointTrajectoryActionGoal.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/FollowJointTrajectoryActionResult.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/FollowJointTrajectoryActionFeedback.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/FollowJointTrajectoryGoal.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/FollowJointTrajectoryResult.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/FollowJointTrajectoryFeedback.msg"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/control_msgs/msg" TYPE FILE FILES
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/GripperCommandAction.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/GripperCommandActionGoal.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/GripperCommandActionResult.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/GripperCommandActionFeedback.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/GripperCommandGoal.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/GripperCommandResult.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/GripperCommandFeedback.msg"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/control_msgs/msg" TYPE FILE FILES
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/JointTrajectoryAction.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/JointTrajectoryActionGoal.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/JointTrajectoryActionResult.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/JointTrajectoryActionFeedback.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/JointTrajectoryGoal.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/JointTrajectoryResult.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/JointTrajectoryFeedback.msg"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/control_msgs/msg" TYPE FILE FILES
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/PointHeadAction.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/PointHeadActionGoal.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/PointHeadActionResult.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/PointHeadActionFeedback.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/PointHeadGoal.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/PointHeadResult.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/PointHeadFeedback.msg"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/control_msgs/msg" TYPE FILE FILES
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/SingleJointPositionAction.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/SingleJointPositionActionGoal.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/SingleJointPositionActionResult.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/SingleJointPositionActionFeedback.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/SingleJointPositionGoal.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/SingleJointPositionResult.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/control_msgs/msg/SingleJointPositionFeedback.msg"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/control_msgs/msg" TYPE FILE FILES
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/control_msgs/control_msgs/msg/GripperCommand.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/control_msgs/control_msgs/msg/JointControllerState.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/control_msgs/control_msgs/msg/JointJog.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/control_msgs/control_msgs/msg/JointTolerance.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/control_msgs/control_msgs/msg/JointTrajectoryControllerState.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/control_msgs/control_msgs/msg/PidState.msg"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/control_msgs/srv" TYPE FILE FILES
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/control_msgs/control_msgs/srv/QueryCalibrationState.srv"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/control_msgs/control_msgs/srv/QueryTrajectoryState.srv"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/control_msgs/cmake" TYPE FILE FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/build/control_msgs/control_msgs/catkin_generated/installspace/control_msgs-msg-paths.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/include/control_msgs")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/roseus/ros/control_msgs")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/common-lisp/ros/control_msgs")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/gennodejs/ros/control_msgs")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/lib/python3/dist-packages/control_msgs")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/lib/python3/dist-packages/control_msgs")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/build/control_msgs/control_msgs/catkin_generated/installspace/control_msgs.pc")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/control_msgs/cmake" TYPE FILE FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/build/control_msgs/control_msgs/catkin_generated/installspace/control_msgs-msg-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/control_msgs/cmake" TYPE FILE FILES
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/build/control_msgs/control_msgs/catkin_generated/installspace/control_msgsConfig.cmake"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/build/control_msgs/control_msgs/catkin_generated/installspace/control_msgsConfig-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/control_msgs" TYPE FILE FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/control_msgs/control_msgs/package.xml")
endif()

