# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "intention_application: 1 messages, 1 services")

set(MSG_I_FLAGS "-Iintention_application:/home/hamza/ros_ws/src/intention_application/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(intention_application_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/hamza/ros_ws/src/intention_application/msg/Array.msg" NAME_WE)
add_custom_target(_intention_application_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "intention_application" "/home/hamza/ros_ws/src/intention_application/msg/Array.msg" ""
)

get_filename_component(_filename "/home/hamza/ros_ws/src/intention_application/srv/snapshot.srv" NAME_WE)
add_custom_target(_intention_application_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "intention_application" "/home/hamza/ros_ws/src/intention_application/srv/snapshot.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(intention_application
  "/home/hamza/ros_ws/src/intention_application/msg/Array.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/intention_application
)

### Generating Services
_generate_srv_cpp(intention_application
  "/home/hamza/ros_ws/src/intention_application/srv/snapshot.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/intention_application
)

### Generating Module File
_generate_module_cpp(intention_application
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/intention_application
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(intention_application_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(intention_application_generate_messages intention_application_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hamza/ros_ws/src/intention_application/msg/Array.msg" NAME_WE)
add_dependencies(intention_application_generate_messages_cpp _intention_application_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hamza/ros_ws/src/intention_application/srv/snapshot.srv" NAME_WE)
add_dependencies(intention_application_generate_messages_cpp _intention_application_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(intention_application_gencpp)
add_dependencies(intention_application_gencpp intention_application_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS intention_application_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(intention_application
  "/home/hamza/ros_ws/src/intention_application/msg/Array.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/intention_application
)

### Generating Services
_generate_srv_eus(intention_application
  "/home/hamza/ros_ws/src/intention_application/srv/snapshot.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/intention_application
)

### Generating Module File
_generate_module_eus(intention_application
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/intention_application
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(intention_application_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(intention_application_generate_messages intention_application_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hamza/ros_ws/src/intention_application/msg/Array.msg" NAME_WE)
add_dependencies(intention_application_generate_messages_eus _intention_application_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hamza/ros_ws/src/intention_application/srv/snapshot.srv" NAME_WE)
add_dependencies(intention_application_generate_messages_eus _intention_application_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(intention_application_geneus)
add_dependencies(intention_application_geneus intention_application_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS intention_application_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(intention_application
  "/home/hamza/ros_ws/src/intention_application/msg/Array.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/intention_application
)

### Generating Services
_generate_srv_lisp(intention_application
  "/home/hamza/ros_ws/src/intention_application/srv/snapshot.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/intention_application
)

### Generating Module File
_generate_module_lisp(intention_application
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/intention_application
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(intention_application_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(intention_application_generate_messages intention_application_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hamza/ros_ws/src/intention_application/msg/Array.msg" NAME_WE)
add_dependencies(intention_application_generate_messages_lisp _intention_application_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hamza/ros_ws/src/intention_application/srv/snapshot.srv" NAME_WE)
add_dependencies(intention_application_generate_messages_lisp _intention_application_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(intention_application_genlisp)
add_dependencies(intention_application_genlisp intention_application_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS intention_application_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(intention_application
  "/home/hamza/ros_ws/src/intention_application/msg/Array.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/intention_application
)

### Generating Services
_generate_srv_nodejs(intention_application
  "/home/hamza/ros_ws/src/intention_application/srv/snapshot.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/intention_application
)

### Generating Module File
_generate_module_nodejs(intention_application
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/intention_application
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(intention_application_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(intention_application_generate_messages intention_application_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hamza/ros_ws/src/intention_application/msg/Array.msg" NAME_WE)
add_dependencies(intention_application_generate_messages_nodejs _intention_application_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hamza/ros_ws/src/intention_application/srv/snapshot.srv" NAME_WE)
add_dependencies(intention_application_generate_messages_nodejs _intention_application_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(intention_application_gennodejs)
add_dependencies(intention_application_gennodejs intention_application_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS intention_application_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(intention_application
  "/home/hamza/ros_ws/src/intention_application/msg/Array.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/intention_application
)

### Generating Services
_generate_srv_py(intention_application
  "/home/hamza/ros_ws/src/intention_application/srv/snapshot.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/intention_application
)

### Generating Module File
_generate_module_py(intention_application
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/intention_application
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(intention_application_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(intention_application_generate_messages intention_application_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hamza/ros_ws/src/intention_application/msg/Array.msg" NAME_WE)
add_dependencies(intention_application_generate_messages_py _intention_application_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hamza/ros_ws/src/intention_application/srv/snapshot.srv" NAME_WE)
add_dependencies(intention_application_generate_messages_py _intention_application_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(intention_application_genpy)
add_dependencies(intention_application_genpy intention_application_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS intention_application_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/intention_application)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/intention_application
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(intention_application_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/intention_application)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/intention_application
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(intention_application_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/intention_application)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/intention_application
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(intention_application_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/intention_application)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/intention_application
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(intention_application_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/intention_application)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/intention_application\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/intention_application
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(intention_application_generate_messages_py std_msgs_generate_messages_py)
endif()
