#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class NodoSuscriptor(Node):
  def __init__(self):
    super().__init__("suscriptor")
    self.sub = self.create_subscription(String, "/topico_prueba", self.topic_callback, 10)

  def topic_callback(self, msg:String):
    self.get_logger().info(msg.data)

def main():
  try:
    rclpy.init()
    
    nodo_suscriptor = NodoSuscriptor()
    rclpy.spin(nodo_suscriptor)

    rclpy.shutdown()
  except KeyboardInterrupt as key_ex:
    print(key_ex)


if __name__ == "__main__":
  main()