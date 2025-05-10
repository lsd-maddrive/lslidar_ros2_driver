#!/usr/bin/python3
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    # Получение путей к конфигурационным файлам
    driver_config_left = PathJoinSubstitution([
        FindPackageShare('lslidar_ch_driver'),
        'params',
        'lslidar_ch_driver_1.yaml'
    ])
    
    driver_config_right = PathJoinSubstitution([
        FindPackageShare('lslidar_ch_driver'),
        'params',
        'lslidar_ch_driver_2.yaml'
    ])

    # Конфигурация для левого лидара
    driver_left = Node(
        package='lslidar_ch_driver',
        executable='lslidar_ch_driver_node',
        name='lslidar_left',
        namespace='left',
        output='screen',
        emulate_tty=True,
        parameters=[driver_config_left],
        remappings=[
            ('scan', 'lidar_left/scan'),
            ('pointcloud', 'lidar_left/pointcloud')
        ]
    )

    # Конфигурация для правого лидара
    driver_right = Node(
        package='lslidar_ch_driver',
        executable='lslidar_ch_driver_node',
        name='lslidar_right',
        namespace='right',
        output='screen',
        emulate_tty=True,
        parameters=[driver_config_right],
        remappings=[
            ('scan', 'lidar_right/scan'),
            ('pointcloud', 'lidar_right/pointcloud')
        ]
    )

    return LaunchDescription([
        driver_left,
        driver_right
    ])