#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from example_interfaces.srv import AddTwoInts_Response
from example_interfaces.srv import AddTwoInts_Request

class NodoServidor(Node):
  def __init__(self):
    super().__init__("nodo_servidor")
    self.server = self.create_service(AddTwoInts,
                                      "servicio_prueba",
                                      self.req_callback)
  def req_callback(self, 
                   req:AddTwoInts_Request, 
                   resp:AddTwoInts_Response):
    resp.sum = req.a + req.b
    self.get_logger().info("Solicitud recibida: ")
    self.get_logger().info("a={}, b={}".format(req.a,
                                               req.b))
    self.get_logger().info("respuesta={}".format(resp.sum))
    return resp

def main():
  try:
    rclpy.init()
    
    nodo_servidor = NodoServidor()
    rclpy.spin(nodo_servidor)

    rclpy.shutdown()
  except KeyboardInterrupt as key_ex:
    print(key_ex)


if __name__ == "__main__":
  main()
