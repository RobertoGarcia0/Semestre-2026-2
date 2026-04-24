#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.task import Future
from example_interfaces.srv import AddTwoInts
from example_interfaces.srv import AddTwoInts_Response
from example_interfaces.srv import AddTwoInts_Request

class NodoCliente(Node):
  def __init__(self):
    super().__init__("nodo_cliente")
    self.client = self.create_client(AddTwoInts,
                                     "servicio_prueba")
    self.create_timer(2, self.timer_callback)

  def timer_callback(self):
    req = AddTwoInts_Request()
    req.a = 10
    req.b = 15
    future = self.client.call_async(req)
    future.add_done_callback(self.response_callback)
    self.get_logger().info("Solicitud enviada: ")
    self.get_logger().info("a={}, b={}".format(req.a,
                                               req.b))

  def response_callback(self, future:Future):
    resp = future.result()
    resp:AddTwoInts_Response
    self.get_logger().info("Respuesta recibida: ")
    self.get_logger().info(str(resp.sum))

def main():
  try:
    rclpy.init()
    
    nodo_cliente = NodoCliente()
    rclpy.spin(nodo_cliente)

    rclpy.shutdown()
  except KeyboardInterrupt as key_ex:
    print(key_ex)


if __name__ == "__main__":
  main()


