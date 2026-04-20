#!/usr/bin/env python3
import random
import rclpy
from rclpy.node import Node
from rclpy.task import Future
from turtlesim.srv import Spawn
from turtlesim.srv import Spawn_Request
from turtlesim.srv import Spawn_Response

class NodoClienteTortuga(Node):
  def __init__(self):
    super().__init__("nodo_cliente_tortuga")
    self.client = self.create_client(Spawn,
                                     "/spawn")
    self.create_timer(2, self.timer_callback)

  def timer_callback(self):
    req = Spawn_Request()
    req.x = random.uniform(0,11)
    req.y = random.uniform(0,11)
    req.theta = random.uniform(0,3.14*2)
    req.name = "Pedro_" + str(random.randint(0, 500))

    future = self.client.call_async(req)
    future.add_done_callback(self.response_callback)
    self.get_logger().info("Solicitud enviada: ")
    self.get_logger().info("x={}, y={}, theta={}, name".format(req.x,
                                               req.y,
                                               req.theta,
                                               req.name))

  def response_callback(self, future:Future):
    resp = future.result()
    resp:Spawn_Response
    self.get_logger().info("Respuesta recibida: ")
    self.get_logger().info(str(resp.name))

def main():
  try:
    rclpy.init()
    
    nodo_cliente = NodoClienteTortuga()
    rclpy.spin(nodo_cliente)

    rclpy.shutdown()
  except KeyboardInterrupt as key_ex:
    print(key_ex)


if __name__ == "__main__":
  main()


