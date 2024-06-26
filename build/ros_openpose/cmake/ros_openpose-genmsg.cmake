# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "ros_openpose: 4 messages, 0 services")

set(MSG_I_FLAGS "-Iros_openpose:/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg;-Istd_msgs:/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/std_msgs/msg;-Igeometry_msgs:/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/common_msgs/geometry_msgs/msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(ros_openpose_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg" NAME_WE)
add_custom_target(_ros_openpose_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ros_openpose" "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg" ""
)

get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg" NAME_WE)
add_custom_target(_ros_openpose_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ros_openpose" "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg" "geometry_msgs/Point32:ros_openpose/Pixel"
)

get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg" NAME_WE)
add_custom_target(_ros_openpose_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ros_openpose" "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg" "ros_openpose/BodyPart:ros_openpose/Pixel:geometry_msgs/Point32"
)

get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Frame.msg" NAME_WE)
add_custom_target(_ros_openpose_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ros_openpose" "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Frame.msg" "ros_openpose/Person:ros_openpose/Pixel:geometry_msgs/Point32:std_msgs/Header:ros_openpose/BodyPart"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_openpose
)
_generate_msg_cpp(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg"
  "${MSG_I_FLAGS}"
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/common_msgs/geometry_msgs/msg/Point32.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_openpose
)
_generate_msg_cpp(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg"
  "${MSG_I_FLAGS}"
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/common_msgs/geometry_msgs/msg/Point32.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_openpose
)
_generate_msg_cpp(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Frame.msg"
  "${MSG_I_FLAGS}"
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/common_msgs/geometry_msgs/msg/Point32.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/std_msgs/msg/Header.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_openpose
)

### Generating Services

### Generating Module File
_generate_module_cpp(ros_openpose
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_openpose
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(ros_openpose_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(ros_openpose_generate_messages ros_openpose_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_cpp _ros_openpose_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_cpp _ros_openpose_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_cpp _ros_openpose_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Frame.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_cpp _ros_openpose_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ros_openpose_gencpp)
add_dependencies(ros_openpose_gencpp ros_openpose_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ros_openpose_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_openpose
)
_generate_msg_eus(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg"
  "${MSG_I_FLAGS}"
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/common_msgs/geometry_msgs/msg/Point32.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_openpose
)
_generate_msg_eus(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg"
  "${MSG_I_FLAGS}"
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/common_msgs/geometry_msgs/msg/Point32.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_openpose
)
_generate_msg_eus(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Frame.msg"
  "${MSG_I_FLAGS}"
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/common_msgs/geometry_msgs/msg/Point32.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/std_msgs/msg/Header.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_openpose
)

### Generating Services

### Generating Module File
_generate_module_eus(ros_openpose
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_openpose
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(ros_openpose_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(ros_openpose_generate_messages ros_openpose_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_eus _ros_openpose_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_eus _ros_openpose_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_eus _ros_openpose_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Frame.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_eus _ros_openpose_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ros_openpose_geneus)
add_dependencies(ros_openpose_geneus ros_openpose_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ros_openpose_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_openpose
)
_generate_msg_lisp(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg"
  "${MSG_I_FLAGS}"
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/common_msgs/geometry_msgs/msg/Point32.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_openpose
)
_generate_msg_lisp(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg"
  "${MSG_I_FLAGS}"
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/common_msgs/geometry_msgs/msg/Point32.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_openpose
)
_generate_msg_lisp(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Frame.msg"
  "${MSG_I_FLAGS}"
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/common_msgs/geometry_msgs/msg/Point32.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/std_msgs/msg/Header.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_openpose
)

### Generating Services

### Generating Module File
_generate_module_lisp(ros_openpose
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_openpose
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(ros_openpose_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(ros_openpose_generate_messages ros_openpose_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_lisp _ros_openpose_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_lisp _ros_openpose_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_lisp _ros_openpose_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Frame.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_lisp _ros_openpose_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ros_openpose_genlisp)
add_dependencies(ros_openpose_genlisp ros_openpose_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ros_openpose_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_openpose
)
_generate_msg_nodejs(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg"
  "${MSG_I_FLAGS}"
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/common_msgs/geometry_msgs/msg/Point32.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_openpose
)
_generate_msg_nodejs(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg"
  "${MSG_I_FLAGS}"
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/common_msgs/geometry_msgs/msg/Point32.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_openpose
)
_generate_msg_nodejs(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Frame.msg"
  "${MSG_I_FLAGS}"
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/common_msgs/geometry_msgs/msg/Point32.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/std_msgs/msg/Header.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_openpose
)

### Generating Services

### Generating Module File
_generate_module_nodejs(ros_openpose
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_openpose
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(ros_openpose_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(ros_openpose_generate_messages ros_openpose_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_nodejs _ros_openpose_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_nodejs _ros_openpose_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_nodejs _ros_openpose_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Frame.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_nodejs _ros_openpose_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ros_openpose_gennodejs)
add_dependencies(ros_openpose_gennodejs ros_openpose_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ros_openpose_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_openpose
)
_generate_msg_py(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg"
  "${MSG_I_FLAGS}"
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/common_msgs/geometry_msgs/msg/Point32.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_openpose
)
_generate_msg_py(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg"
  "${MSG_I_FLAGS}"
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/common_msgs/geometry_msgs/msg/Point32.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_openpose
)
_generate_msg_py(ros_openpose
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Frame.msg"
  "${MSG_I_FLAGS}"
  "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/common_msgs/geometry_msgs/msg/Point32.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/std_msgs/msg/Header.msg;/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_openpose
)

### Generating Services

### Generating Module File
_generate_module_py(ros_openpose
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_openpose
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(ros_openpose_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(ros_openpose_generate_messages ros_openpose_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Pixel.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_py _ros_openpose_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/BodyPart.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_py _ros_openpose_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Person.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_py _ros_openpose_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arjan/Desktop/ros_noetic_base_2204/catkin_ws/src/ros_openpose/msg/Frame.msg" NAME_WE)
add_dependencies(ros_openpose_generate_messages_py _ros_openpose_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ros_openpose_genpy)
add_dependencies(ros_openpose_genpy ros_openpose_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ros_openpose_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_openpose)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ros_openpose
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(ros_openpose_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(ros_openpose_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_openpose)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ros_openpose
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(ros_openpose_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(ros_openpose_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_openpose)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ros_openpose
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(ros_openpose_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(ros_openpose_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_openpose)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ros_openpose
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(ros_openpose_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(ros_openpose_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_openpose)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_openpose\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ros_openpose
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(ros_openpose_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(ros_openpose_generate_messages_py geometry_msgs_generate_messages_py)
endif()
