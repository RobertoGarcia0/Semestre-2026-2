#!/usr/bin/env python3 
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
  # Publicador
  nodo_publicador = Node(
    package="paquete_prueba",
    executable="programa_publicador"
  )
  # Servidor
  nodo_servidor = Node(
    package="paquete_prueba",
    executable="programa_servidor"
  )
  # Servidor de acción
  nodo_accion = Node(
    package="paquete_prueba",
    executable="programa_accion_servidor"
  )

  # Objeto del launcher
  launch_description = LaunchDescription([nodo_publicador, 
                                          nodo_servidor,
                                          nodo_accion])
  return launch_description