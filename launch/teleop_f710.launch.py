from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    config_file = os.path.join(
        get_package_share_directory('robot_bringup'),
        'config',
        'f710_teleop.yaml'
    )

    joy_node = Node(
        package='joy',
        executable='game_controller_node',
        name='game_controller_node',
        output='screen',
        parameters=[{
            'device_id': 0,
            'deadzone': 0.08,
            'autorepeat_rate': 30.0,
            'sticky_buttons': False,
            'coalesce_interval_ms': 1
        }]
    )

    teleop_node = Node(
        package='teleop_twist_joy',
        executable='teleop_node',
        name='teleop_twist_joy',
        output='screen',
        parameters=[config_file]
    )

    return LaunchDescription([
        joy_node,
        teleop_node
    ])