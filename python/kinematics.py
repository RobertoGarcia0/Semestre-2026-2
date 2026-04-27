from sympy import *
class Robot():
  def __init__(self, l:tuple[int]):
    # Cinemática directa
    th1, th2, th3 = symbols("theta_1, theta_2, theta_3")
    self.th1, self.th2, self.th3 = th1, th2, th3
    T_0_1 = self._tr_h(alpha = th1)
    T_1_2 = self._tr_h(x = l[0], alpha = th2)
    T_2_3 = self._tr_h(x = l[1], alpha = th3)
    T_3_p = self._tr_h(x = l[2])
    T_0_p = simplify(T_0_1 * T_1_2 * T_2_3 * T_3_p)
    xi_0_p = Matrix([T_0_p[0, 3],
                     T_0_p[1, 3],
                     th1 + th2 + th3])
    J = Matrix([[diff(xi_0_p, th1),
                 diff(xi_0_p, th2),
                 diff(xi_0_p, th3)]])
    print(J)
    J_inv = J.inv()
    x_dot, y_dot, alpha_dot = symbols("x_dot, y_dot, alpha_dot")
    self.x_dot, self.y_dot, self.alpha_dot = x_dot, y_dot, alpha_dot
    xi_0_p_dot = Matrix([x_dot, y_dot, alpha_dot])
    th_dot = J_inv * xi_0_p_dot
    self.xi_0_p = xi_0_p
    self.th_dot = th_dot
    # Construir una trayectoria
    t = symbols("t")
    self.t = t
    a_0, a_1, a_2, a_3, a_4, a_5 = symbols("a_0, a_1, a_2, a_3, a_4, a_5")
    self.a_0, self.a_1, self.a_2, self.a_3, self.a_4, self.a_5 = a_0, a_1, a_2, a_3, a_4, a_5
    self.lam = a_0 + a_1 * t + a_2 * t**2 + a_3 * t**3 + a_4 * t**4 + a_5 * t**5
    # derivadas del polinomio
    self.lam_dot = diff(self.lam, t)
    self.lam_dot_dot = diff(self.lam_dot, t)

  def def_trayectoria(self, t_f, frec, th_i=(0.1, 0.1, 0.1), xi_fn=(0.7, 0.1, 0)):
    xi_in = self.xi_0_p.subs({self.th1: th_i[0], 
                              self.th2: th_i[1], 
                              self.th3: th_i[0]})
    self.dt = 1.0/frec
    self.muestras = t_f * frec + 1
    eq1 = self.lam.subs({self.t: 0})
    eq2 = self.lam.subs({self.t: t_f}) - 1
    eq3 = self.lam_dot.subs({self.t: 0})
    eq4 = self.lam_dot.subs({self.t: t_f})
    eq5 = self.lam_dot_dot.subs({self.t: 0})
    eq6 = self.lam_dot_dot.subs({self.t: t_f})
    solutions = solve((eq1, eq2, eq3, eq4, eq5, eq6),
                    (self.a_0, self.a_1, self.a_2, self.a_3, self.a_4, self.a_5))
    lam_s = self.lam.subs(solutions)
    lam_dot_s = self.lam_dot.subs(solutions)
    lam_dot_dot_s = self.lam_dot_dot.subs(solutions)
    
    # Posición, velocidad y aceleración en x
    x_eq = xi_in[0] + lam_s * (xi_fn[0] - xi_in[0])
    x_dot_eq = lam_dot_s * (xi_fn[0] - xi_in[0])
    x_dot_dot_eq = lam_dot_dot_s * (xi_fn[0] - xi_in[0])
    # Posición, velocidad y aceleración en y
    y_eq = xi_in[1] + lam_s * (xi_fn[1] - xi_in[1])
    y_dot_eq = lam_dot_s * (xi_fn[1] - xi_in[1])
    y_dot_dot_eq = lam_dot_dot_s * (xi_fn[1] - xi_in[1])
    # Posición, velocidad y aceleración en alpha
    alpha_eq = xi_in[2] + lam_s * (xi_fn[2] - xi_in[2])
    alpha_dot_eq = lam_dot_s * (xi_fn[2] - xi_in[2])
    alpha_dot_dot_eq = lam_dot_dot_s * (xi_fn[2] - xi_in[2])

    # Generar arreglos para guardar muestreo
    # Tiempo
    t_m = Matrix.zeros(1, self.muestras)
    for i in range(self.muestras):
      t_m[i] = self.dt * i
    t_m
    # Arreglos para posición, velocidad y aceleración del E.F.
    xi_m         = Matrix.zeros(3, self.muestras)
    xi_dot_m     = Matrix.zeros(3, self.muestras)
    xi_dot_dot_m = Matrix.zeros(3, self.muestras)
    xi_t = Matrix([x_eq, y_eq, alpha_eq])
    xi_dot_t = Matrix([x_dot_eq, y_dot_eq, alpha_dot_eq])
    xi_dot_dot_t = Matrix([x_dot_dot_eq, y_dot_dot_eq, alpha_dot_dot_eq])
    # Muestreo
    for i in range(self.muestras):
      xi_m[:, i]         = xi_t.        subs({self.t: t_m[i]})
      xi_dot_m[:, i]     = xi_dot_t.    subs({self.t: t_m[i]})
      xi_dot_dot_m[:, i] = xi_dot_dot_t.subs({self.t: t_m[i]})
    xi_m
    #Arreglos para posición, velocidad y aceleración de las juntas
    th_m = Matrix.zeros(3, self.muestras)
    th_dot_m = Matrix.zeros(3, self.muestras)
    th_dot_dot_m = Matrix.zeros(3, self.muestras)
    th_m[:, 0] = Matrix([th_i[0], th_i[1], th_i[2]])
    # Cinemática inversa
    for i in range(self.muestras):
      th_dot_m[:, i] = (self.th_dot.subs({self.th1: th_m[0, i], self.th2: th_m[1, i], 
                                    self.th3: th_m[2, i], self.x_dot: xi_dot_m[0, i],
                                    self.y_dot: xi_dot_m[1, i], 
                                    self.alpha_dot: xi_dot_m[2, i]})).evalf()
      print(i)
      if i < self.muestras - 1:
        th_m[:, i+1] = th_m[:, i] + th_dot_m[:, i] * self.dt
      if i > 0:
        th_dot_dot_m[:, i-1] = (th_dot_m[:, i] - th_dot_m[:, i-1])/self.dt
    th_dot_dot_m
    self.th_m = th_m
  def graficar_theta(self):
    pass
  def graficar_xi(self):
    pass

  def _tr_h(self, x=0, y=0, z=0, gamma=0, beta=0, alpha=0):
    T_x = Matrix([[1,          0,           0, x],
                  [0, cos(gamma), -sin(gamma), 0],
                  [0, sin(gamma),  cos(gamma), 0],
                  [0,          0,           0, 1],])
    T_y = Matrix([[cos(beta),  0, sin(beta), 0],
                  [        0,  1,         0, y],
                  [-sin(beta), 0, cos(beta), 0],
                  [0, 0, 0, 1]])
    T_z = Matrix([[cos(alpha), -sin(alpha), 0, 0], 
                  [sin(alpha),  cos(alpha), 0, 0],
                  [         0,           0, 1, z], 
                  [         0,           0, 0, 1]])
    return T_x * T_y * T_z
    
def main():
  robot = Robot(l=(0.1, 0.1, 0.1))

if __name__ == "__main__":
  main()