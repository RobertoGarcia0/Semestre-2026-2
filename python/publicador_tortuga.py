#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from geometry_msgs.msg import Twist

class NodoPublicador(Node):
  def __init__(self):
    super().__init__("publicador_tortuga")
    self.pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 5)
    self.create_timer(1, self.send_message)

  def send_message(self):
    msg = Twist()
    msg.linear.x = float(1.0)
    msg.angular.z = float(1.0)
    self.pub.publish(msg)
    self.get_logger().info("Publicando velocidad x: {}, z: {}".format(msg.linear.x, msg.angular.z))

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