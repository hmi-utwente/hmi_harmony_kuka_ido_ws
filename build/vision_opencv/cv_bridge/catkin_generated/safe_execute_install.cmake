execute_process(COMMAND "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/build/vision_opencv/cv_bridge/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/build/vision_opencv/cv_bridge/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
