#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
  # Ruta del paquete robot_description
  description_path = get_package_share_directory(
    "robot_description"
  )
  # Rutas de urdf y rviz conf
  urdf_path = description_path + "/urdf/robot_rrr.urdf"
  rviz_path = description_path + "/rviz/rviz.conf.rviz"
  # URDF como xacro
  urdf_xacro  = Command(["xacro ", urdf_path])
  # Modelo URDF como parámetro
  urdf_param = {"robot_description": 
                ParameterValue(urdf_xacro, value_type=str)}
  
  # Nodos
  
  # Rviz
  rviz_node = Node(
    package="rviz2",
    executable="rviz2",
    arguments=["-d", rviz_path]
  )
  # Robot description (publica urdf)
  robot_description_node = Node(
    package="robot_state_publisher",
    executable="robot_state_publisher",
    parameters=[urdf_param]
  )
  # Interfaz gráfica para publicar estado de juntas
  joint_publisher_node = Node(
    package="joint_state_publisher_gui",
    executable="joint_state_publisher_gui"
  )
  launch_description = LaunchDescription([
    rviz_node, robot_description_node, 
    joint_publisher_node
  ])
  return launch_description
  