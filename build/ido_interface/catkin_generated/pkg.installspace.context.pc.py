# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "hardware_interface;controller_manager;roscpp;control_msgs;trajectory_msgs;pluginlib;transmission_interface;urdf;control_toolbox;joint_limits_interface".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lMyRobot_hardware_interface".split(';') if "-lMyRobot_hardware_interface" != "" else []
PROJECT_NAME = "ido_interface"
PROJECT_SPACE_DIR = "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/install"
PROJECT_VERSION = "0.0.0"
