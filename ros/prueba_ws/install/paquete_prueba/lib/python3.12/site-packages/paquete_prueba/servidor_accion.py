#!/usr/bin/env python3
import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle
from example_interfaces.action import Fibonacci

class NodoServidorAccion(Node):
  def __init__(self):
    super().__init__("nodo_servidor_accion")
    self.action_server = ActionServer(self,
                                      Fibonacci,
                                      "accion_prueba",
                                      self.req_callback)
    self.get_logger().info("Acción 'accion_prueba inicializada'")
    
  def req_callback(self, 
                   goal_handle:ServerGoalHandle):
    # Inicializaciones de objetos
    feedback_msg = Fibonacci.Feedback()
    res = Fibonacci.Result()
    feedback_msg.sequence = [0, 1]
    # Procesamiento
    for i in range(1, goal_handle.request.order):
      feedback_msg.sequence.append(
        feedback_msg.sequence[i] + feedback_msg.sequence[i-1])
      # Retroalimentación
      goal_handle.publish_feedback(feedback_msg)
      self.get_logger().info("Secuencia actual: " + 
                             str(feedback_msg.sequence))
      time.sleep(1)
      
    # Final (Respuesta de finalización)
    goal_handle.succeed()
    res.sequence = feedback_msg.sequence
    return res

def main():
  try:
    rclpy.init()
    
    nodo_servidor = NodoServidorAccion()
    rclpy.spin(nodo_servidor)

    rclpy.shutdown()
  except KeyboardInterrupt as key_ex:
    print(key_ex)


if __name__ == "__main__":
  main()
