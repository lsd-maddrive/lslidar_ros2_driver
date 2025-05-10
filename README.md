# LSlidar ROS2 Driver

ROS2 драйвер для лидаров LSlidar серии CH. Обеспечивает получение, обработку и публикацию данных лидара в ROS2-экосистеме.

## Особенности
- Поддержка ROS2 Jazzy
- Реализация через libpcap для сетевого взаимодействия
- Публикация данных в форматах:
  - PointCloud2
  - LaserScan
- Настройка параметров через YAML-файлы
- Поддержка нескольких лидаров одновременно

## Зависимости
- ROS2 (в том числе и Jazzy)
- libpcap
- PCL

## Установка

### 1. Установка зависимостей

```bash
sudo apt-get update
sudo apt-get install -y libpcap-dev ros-${ROS_DISTRO}-pcl-conversions
```

### 2. Сборка пакета

```bash
mkdir -p ~/lidar_ws/src
cd ~/lidar_ws/src
git clone https://github.com/your_repo/lslidar_ros2_driver.git
cd ~/lidar_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
```
