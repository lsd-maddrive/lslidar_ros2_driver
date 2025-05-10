cmake_minimum_required(VERSION 3.5)
project(lslidar_cb64s1)

# Поиск необходимых пакетов
find_package(ament_cmake REQUIRED)

# Установка launch-файлов и конфигураций
install(
  DIRECTORY 
    launch
    params
    rviz_cfg
  DESTINATION 
    share/${PROJECT_NAME}
)

# Установка параметров если есть дополнительные файлы
if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/params")
  install(
    DIRECTORY params
    DESTINATION share/${PROJECT_NAME}
  )
endif()

ament_package()