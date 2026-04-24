#!/usr/bin/env python3
import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.task import Future
from rclpy.action.client import ClientGoalHandle
from example_interfaces.action import Fibonacci
from example_interfaces.action import Fibonacci_GetResult_Response
from example_interfaces.action import Fibonacci_GetResult_Request
from example_interfaces.action._fibonacci import Fibonacci_FeedbackMessage

class NodoClienteAccion(Node):
  def __init__(self):
    super().__init__("nodo_cliente_accion")
    self.action_client = ActionClient(self,
                                      Fibonacci,
                                      "accion_prueba")
    # Para que se ejecute una vez al inicio 
    # y después cada 10 segundos
    self.timer_callback()
    self.create_timer(10, self.timer_callback)
    self.get_logger().info("Cliente 'accion_prueba inicializada'")
  
  # Enviar solicitud
  def timer_callback(self):
    self.goal = Fibonacci.Goal()
    self.goal.order = 5
    self.future = self.action_client.send_goal_async(
                                    self.goal,
                                    self.feedback_callback)
    self.future:Future
    self.future.add_done_callback(self.accept_callback)

  # Solicitud aceptada
  def accept_callback(self, future:Future):
    self.goal_handle = future.result()
    self.goal_handle:ClientGoalHandle
    self.get_logger().info("Solicitud aceptada")
    self.result_future = self.goal_handle.get_result_async()
    self.result_future:Future
    self.result_future.add_done_callback(self.done_callback)
  # Retroalimentación
  def feedback_callback(self, 
                        feedback_msg:Fibonacci_FeedbackMessage):
    feedback = feedback_msg.feedback
    self.get_logger().info("Retroalimentación: {}".format(
                                    str(feedback.sequence)))
  
  # Finalización
  def done_callback(self, future:Future):
    res = future.result()
    res:Fibonacci_GetResult_Response
    self.get_logger().info("Resultado final: {}".format(
      res.result.sequence
    ))


def main():
  try:
    rclpy.init()
    
    nodo_cliente = NodoClienteAccion()
    rclpy.spin(nodo_cliente)

    rclpy.shutdown()
  except KeyboardInterrupt as key_ex:
    print(key_ex)


if __name__ == "__main__":
  main()
