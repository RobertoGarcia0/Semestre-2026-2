from sympy import *
import matplotlib.pyplot as plt
class Robot():
  def __init__(self, l:tuple[int]=(0.3, 0.3, 0.3)):
    # Cinemática directa
    th1, th2, th3 = symbols("theta_1, theta_2, theta_3")
    self.th1, self.th2, self.th3 = th1, th2, th3
    T_0_1 = self._tr_h()
    T_1_2 = self._tr_h()
    T_2_3 = self._tr_h()
    T_3_p = self._tr_h()
    T_0_p = simplify()
    # Postura
    xi_0_p = Matrix([])
    # Jacobiano
    J = Matrix([])
    J_inv = J.inv()
    # Variables de velocidad del EF
    x_dot, y_dot, alpha_dot = symbols("x_dot, y_dot, alpha_dot")
    self.x_dot, self.y_dot, self.alpha_dot = x_dot, y_dot, alpha_dot
    # Vector de velocidad del efector final
    xi_0_p_dot = Matrix([x_dot, y_dot, alpha_dot])
    # Velocidad de las juntas en términos de la velocidad del efector final (Cinemática inversa)
    th_dot = J_inv * xi_0_p_dot
    #Guardar variables
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

    xi_in = 
    self.dt = 1.0/frec
    self.muestras = t_f * frec + 1
    eq1 = 
    eq2 = 
    eq3 = 
    eq4 = 
    eq5 = 
    eq6 = 
    solutions = solve((eq1, eq2, eq3, eq4, eq5, eq6),
                    (self.a_0, self.a_1, self.a_2, self.a_3, self.a_4, self.a_5))
    
    lam_s = self.lam.subs(solutions)
    lam_dot_s = self.lam_dot.subs(solutions)
    lam_dot_dot_s = self.lam_dot_dot.subs(solutions)
    
    # Posición, velocidad y aceleración en x
    x_eq = 
    x_dot_eq = lam_dot_s * (xi_fn[0] - xi_in[0])
    x_dot_dot_eq = lam_dot_dot_s * (xi_fn[0] - xi_in[0])
    # Posición, velocidad y aceleración en y
    y_eq = 
    y_dot_eq = lam_dot_s * (xi_fn[1] - xi_in[1])
    y_dot_dot_eq = lam_dot_dot_s * (xi_fn[1] - xi_in[1])
    # Posición, velocidad y aceleración en alpha
    alpha_eq = 
    alpha_dot_eq = lam_dot_s * (xi_fn[2] - xi_in[2])
    alpha_dot_dot_eq = lam_dot_dot_s * (xi_fn[2] - xi_in[2])

    # Generar arreglos para guardar muestreo
    # Tiempo
    t_m = Matrix.zeros(1, self.muestras)
    for i in range(self.muestras):
      t_m[i] = self.dt * i

    # Arreglos para posición, velocidad y aceleración del E.F.
    xi_m         = Matrix.zeros(3, self.muestras)
    xi_dot_m     = Matrix.zeros(3, self.muestras)
    xi_dot_dot_m = Matrix.zeros(3, self.muestras)
    xi_t         = 
    xi_dot_t     = 
    xi_dot_dot_t = 
    # Muestreo
    for i in range(self.muestras):
      xi_m[:, i]         = 
      xi_dot_m[:, i]     = 
      xi_dot_dot_m[:, i] = 

    #Arreglos para posición, velocidad y aceleración de las juntas
    th_m         = Matrix.zeros(3, self.muestras)
    th_dot_m     = Matrix.zeros(3, self.muestras)
    th_dot_dot_m = Matrix.zeros(3, self.muestras)
    # Posición inicial de las juntas
    th_m[:, 0] = Matrix([th_i[0], th_i[1], th_i[2]])
    # Cinemática inversa
    for i in range(self.muestras):
      th_dot_m[:, i] = (self.th_dot.subs({})).evalf()
      print("Iteración: {}".format(i))
      if i < self.muestras - 1:
        th_m[:, i+1] = th_m[:, i] + th_dot_m[:, i] * self.dt
      if i > 0:
        th_dot_dot_m[:, i-1] = (th_dot_m[:, i] - th_dot_m[:, i-1])/self.dt

    self.th_m = th_m
    self.xi_m = xi_m
    self.t_m = t_m
    self.graficar_xi()
    self.graficar_th()

  def graficar_xi(self):
    fig, (x_g, y_g, al_g) = plt.subplots(nrows = 1, ncols = 3)
    fig.suptitle("Posiciones del efector final")
    x_g.set_title("x")
    y_g.set_title("y")
    al_g.set_title("alpha")
    x_g.plot(self.t_m.T, self.xi_m[0, :].T, color="RED")
    y_g.plot(self.t_m.T, self.xi_m[1, :].T, color="green")
    al_g.plot(self.t_m.T, self.xi_m[2, :].T, color=(0,0,1))
    plt.show()
    pass
  def graficar_th(self):
    fig, (x_g, y_g, al_g) = plt.subplots(nrows = 1, ncols = 3)
    fig.suptitle("Posiciones del efector final")
    x_g.set_title("x")
    y_g.set_title("y")
    al_g.set_title("alpha")
    x_g.plot(self.t_m.T, self.th_m[0, :].T, color="RED")
    y_g.plot(self.t_m.T, self.th_m[1, :].T, color="green")
    al_g.plot(self.t_m.T, self.th_m[2, :].T, color=(0,0,1))
    plt.show()
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
  robot = Robot()
  robot.def_trayectoria()
if __name__ == "__main__":
  main()