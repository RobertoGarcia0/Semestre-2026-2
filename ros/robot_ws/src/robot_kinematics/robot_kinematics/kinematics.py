#!/usr/bin/env python3
from sympy import *
import matplotlib.pyplot as plt

class Robot():
  def __init__(self, 
               l:tuple[float]=(0.3, 0.3, 0.3)):
    th1, th2, th3 = symbols("theta_1,theta_2,theta_3")

    T_0_1 = self.tr_h(gamma=pi/2,
                      alpha=th1)
    T_1_2 = self.tr_h(x = l[0],
                      alpha=th2)
    T_2_3 = self.tr_h(x = l[1],
                      alpha=th3)
    T_3_p = self.tr_h(x=l[2])

    T_0_p = T_0_1 * T_1_2 * T_2_3 * T_3_p
    T_0_p = simplify(T_0_p)
    # Vector de postura
    xi_0_p = Matrix([T_0_p[0, 3],
                     T_0_p[2, 3],
                     th1 + th2 + th3])
    # Jacobiano
    J = Matrix([[diff(xi_0_p, th1),
                 diff(xi_0_p, th2),
                 diff(xi_0_p, th3)]])
    J_inv = J.inv()

    # Velocidades del E.F. como variables
    x_dot, z_dot, beta_dot = symbols("x_dot, z_dot, beta_dot")
    # Construir polinomio lambda
    t = symbols("t")
    a_0, a_1, a_2, a_3, a_4, a_5 = symbols("a_0, a_1, a_2, a_3, a_4, a_5")
    lam = a_0 + a_1 * t + a_2 * t**2 + a_3 * t**3 + a_4 * t**4 + a_5 * t**5    
    lam_dot = diff(lam, t)
    lam_dot_dot = diff(lam_dot, t)
    # Almacenar variables en el objeto
    self.th1, self.th2, self.th3 = th1, th2, th3
    self.xi_0_p = xi_0_p
    self.J_inv = J_inv
    self.x_dot, self.z_dot, self.beta_dot = symbols("x_dot, z_dot, beta_dot")
    self.a_0, self.a_1, self.a_2, self.a_3, self.a_4, self.a_5 = a_0, a_1, a_2, a_3, a_4, a_5
    self.t = t
    self.lam, self.lam_dot, self.lam_dot_dot = lam, lam_dot, lam_dot_dot
    pass
  def def_tray(self, t_f:float, frec:float, 
               th_i:tuple[float], xi_f:tuple[float]):
    
    # Posición del efector final substituyendo en la postura (m, rad)
    xi_i = self.xi_0_p.subs({self.th_1: th_i[0], 
                             self.th_2: th_i[1], 
                             self.th_3: th_i[2]})
    # Muestreo y dt
    self.dt = 1.0/frec
    self.muestras = t_f * frec + 1

    #Eq. de restricción para trayectoria
    eq1 = self.lam.subs({self.t: 0})
    eq2 = self.lam.subs({self.t: t_f}) - 1
    eq3 = self.lam_dot.subs({self.t: 0})
    eq4 = self.lam_dot.subs({self.t: t_f})
    eq5 = self.lam_dot_dot.subs({self.t: 0})
    eq6 = self.lam_dot_dot.subs({self.t: t_f})
    solutions = solve((eq1, eq2, eq3, eq4, eq5, eq6),
                  (self.a_0, self.a_1, self.a_2, self.a_3, self.a_4, self.a_5))
    # Sustituyendo solución en polinimio lambda
    lam_s         = self.lam.subs(solutions)
    lam_dot_s     = self.lam_dot.subs(solutions)
    lam_dot_dot_s = self.lam_dot_dot.subs(solutions)
    
    # Ecuación de posiciones, velocidades y acc.
    xi_f = Matrix([xi_f[0], xi_f[1], xi_f[2]])
    xi_eq         = xi_i + (xi_f - xi_i) * lam_s
    xi_dot_eq     = (xi_f - xi_i) * lam_dot_s
    xi_dot_dot_eq = (xi_f - xi_i) * lam_dot_dot_s
    
    # Arreglos para almacenar muestreo
    # Tiempo
    t_m = Matrix.zeros(1, self.muestras)
    for i in range(self.muestras):
      t_m[i] = self.dt * i
    # Posición, velocidad y aceleración del E.F.
    xi_m         = Matrix.zeros(3, self.muestras)
    xi_dot_m     = Matrix.zeros(3, self.muestras)
    xi_dot_dot_m = Matrix.zeros(3, self.muestras)
    # Muestreo E.F.
    for i in range(self.muestras):
      xi_m[:, i]         = xi_eq.        subs({self.t: t_m[i]})
      xi_dot_m[:, i]     = xi_dot_eq.    subs({self.t: t_m[i]})
      xi_dot_dot_m[:, i] = xi_dot_dot_eq.subs({self.t: t_m[i]})


  def tr_h(self, x=0, y=0, z=0,
                 gamma=0, beta=0, alpha=0):
    t_x = Matrix([[1,          0,           0, x],
                  [0, cos(gamma), -sin(gamma), 0],
                  [0, sin(gamma),  cos(gamma), 0],
                  [0,          0,           0, 1]])
    t_y = Matrix([[ cos(beta),          0, sin(beta), 0],
                  [         0,          1,         0, y],
                  [-sin(beta),          0, cos(beta), 0],
                  [         0,          0,         0, 1]])
    t_z = Matrix([[cos(alpha), -sin(alpha), 0, 0],
                  [sin(alpha),  cos(alpha), 0, 0],
                  [         0,           0, 1, z],
                  [         0,           0, 0, 1]])
    tr = simplify(t_x * t_y * t_z)
    return tr

def main():
  robot = Robot()
  print(robot.J_inv)
if __name__ == "__main__":
  main()
