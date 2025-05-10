#!/usr/bin/python3
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import LifecycleNode, Node
from launch.actions import DeclareLaunchArgument
import os


def generate_launch_description():
    # Get paths to configuration files
    driver_config = os.path.join(
        get_package_share_directory('lslidar_ch_driver'),
        'params',
        'lslidar_ch.yaml'
    )
    rviz_config = os.path.join(
        get_package_share_directory('lslidar_ch_driver'),
        'rviz_cfg',
        'lslidar_ch_driver.rviz'
    )

    # LiDAR driver node (supports all ROS 2 versions with modern API)
    driver_node = LifecycleNode(
        package='lslidar_ch_driver',
        namespace='CH',
        executable='lslidar_ch_driver_node',
        name='lslidar_ch_driver_node',
        output='screen',
        emulate_tty=True,
        parameters=[driver_config]
    )

    # RViz2 node
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config],
        output='screen'
    )

    return LaunchDescription([
        driver_node,
        rviz_node
    ])