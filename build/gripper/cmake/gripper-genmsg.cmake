# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "gripper: 2 messages, 0 services")

set(MSG_I_FLAGS "-Igripper:/home/rob/UCD_robot_ws_v2/src/gripper/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(gripper_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetDelta.msg" NAME_WE)
add_custom_target(_gripper_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "gripper" "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetDelta.msg" ""
)

get_filename_component(_filename "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetForce.msg" NAME_WE)
add_custom_target(_gripper_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "gripper" "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetForce.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(gripper
  "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetDelta.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/gripper
)
_generate_msg_cpp(gripper
  "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetForce.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/gripper
)

### Generating Services

### Generating Module File
_generate_module_cpp(gripper
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/gripper
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(gripper_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(gripper_generate_messages gripper_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetDelta.msg" NAME_WE)
add_dependencies(gripper_generate_messages_cpp _gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetForce.msg" NAME_WE)
add_dependencies(gripper_generate_messages_cpp _gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(gripper_gencpp)
add_dependencies(gripper_gencpp gripper_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS gripper_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(gripper
  "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetDelta.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/gripper
)
_generate_msg_eus(gripper
  "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetForce.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/gripper
)

### Generating Services

### Generating Module File
_generate_module_eus(gripper
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/gripper
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(gripper_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(gripper_generate_messages gripper_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetDelta.msg" NAME_WE)
add_dependencies(gripper_generate_messages_eus _gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetForce.msg" NAME_WE)
add_dependencies(gripper_generate_messages_eus _gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(gripper_geneus)
add_dependencies(gripper_geneus gripper_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS gripper_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(gripper
  "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetDelta.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/gripper
)
_generate_msg_lisp(gripper
  "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetForce.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/gripper
)

### Generating Services

### Generating Module File
_generate_module_lisp(gripper
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/gripper
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(gripper_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(gripper_generate_messages gripper_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetDelta.msg" NAME_WE)
add_dependencies(gripper_generate_messages_lisp _gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetForce.msg" NAME_WE)
add_dependencies(gripper_generate_messages_lisp _gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(gripper_genlisp)
add_dependencies(gripper_genlisp gripper_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS gripper_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(gripper
  "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetDelta.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/gripper
)
_generate_msg_nodejs(gripper
  "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetForce.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/gripper
)

### Generating Services

### Generating Module File
_generate_module_nodejs(gripper
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/gripper
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(gripper_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(gripper_generate_messages gripper_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetDelta.msg" NAME_WE)
add_dependencies(gripper_generate_messages_nodejs _gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetForce.msg" NAME_WE)
add_dependencies(gripper_generate_messages_nodejs _gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(gripper_gennodejs)
add_dependencies(gripper_gennodejs gripper_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS gripper_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(gripper
  "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetDelta.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/gripper
)
_generate_msg_py(gripper
  "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetForce.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/gripper
)

### Generating Services

### Generating Module File
_generate_module_py(gripper
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/gripper
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(gripper_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(gripper_generate_messages gripper_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetDelta.msg" NAME_WE)
add_dependencies(gripper_generate_messages_py _gripper_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/rob/UCD_robot_ws_v2/src/gripper/msg/TargetForce.msg" NAME_WE)
add_dependencies(gripper_generate_messages_py _gripper_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(gripper_genpy)
add_dependencies(gripper_genpy gripper_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS gripper_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/gripper)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/gripper
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(gripper_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/gripper)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/gripper
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(gripper_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/gripper)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/gripper
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(gripper_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/gripper)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/gripper
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(gripper_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/gripper)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/gripper\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/gripper
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(gripper_generate_messages_py std_msgs_generate_messages_py)
endif()
