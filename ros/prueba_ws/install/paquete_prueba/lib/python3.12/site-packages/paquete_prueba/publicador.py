#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class NodoPublicador(Node):
  def __init__(self):
    super().__init__("publicador")
    self.pub = self.create_publisher(String, "/topico_prueba", 5)
    self.create_timer(1, self.send_message)

  def send_message(self):
    msg = String()
    msg.data = "Mensaje"
    self.pub.publish(msg)

def main():
  try:
    rclpy.init()
    
    nodo_publicador = NodoPublicador()
    rclpy.spin(nodo_publicador)

    rclpy.shutdown()
  except KeyboardInterrupt as key_ex:
    print(key_ex)


if __name__ == "__main__":
  main()
