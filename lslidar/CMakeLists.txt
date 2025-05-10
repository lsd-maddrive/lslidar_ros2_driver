cmake_minimum_required(VERSION 3.5)
project(lslidar)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY 
    launch
    params
    rviz_cfg
  DESTINATION 
    share/${PROJECT_NAME}
)

if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/params")
  install(
    DIRECTORY params
    DESTINATION share/${PROJECT_NAME}
  )
endif()

ament_package()