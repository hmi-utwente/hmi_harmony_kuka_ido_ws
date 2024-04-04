# Install script for directory: /home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/test_rosmaster/msg" TYPE FILE FILES
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/msg/String.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/msg/Arrays.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/msg/CompositeA.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/msg/CompositeB.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/msg/Composite.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/msg/Embed.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/msg/Floats.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/msg/Simple.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/msg/RosmsgA.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/msg/RosmsgB.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/msg/RosmsgC.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/msg/TestArrays.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/msg/TestHeader.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/msg/TestPrimitives.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/msg/TestString.msg"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/msg/TVals.msg"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/test_rosmaster/srv" TYPE FILE FILES
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/srv/AddTwoInts.srv"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/srv/RossrvA.srv"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/srv/RossrvB.srv"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/test_rosmaster/cmake" TYPE FILE FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/build/ros_comm/test/test_rosmaster/catkin_generated/installspace/test_rosmaster-msg-paths.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/include/test_rosmaster")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/roseus/ros/test_rosmaster")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/common-lisp/ros/test_rosmaster")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/share/gennodejs/ros/test_rosmaster")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/lib/python3/dist-packages/test_rosmaster")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/devel/lib/python3/dist-packages/test_rosmaster")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/build/ros_comm/test/test_rosmaster/catkin_generated/installspace/test_rosmaster.pc")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/test_rosmaster/cmake" TYPE FILE FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/build/ros_comm/test/test_rosmaster/catkin_generated/installspace/test_rosmaster-msg-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/test_rosmaster/cmake" TYPE FILE FILES
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/build/ros_comm/test/test_rosmaster/catkin_generated/installspace/test_rosmasterConfig.cmake"
    "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/build/ros_comm/test/test_rosmaster/catkin_generated/installspace/test_rosmasterConfig-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/test_rosmaster" TYPE FILE FILES "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_comm/test/test_rosmaster/package.xml")
endif()

