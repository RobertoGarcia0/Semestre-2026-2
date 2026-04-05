x = float(10.0)
y = "Hola"

#Lista
a = [0, 1, 2]
b = [0, 1.5, "hola", 'a', "hola"]
b.append(10)
b.remove("hola")

#Conjunto
conjunto={1,2,3,3,4,4,5}
conjunto.add(10)
conjunto.add(8)


#Diccionario
dicc={"Edad": 20, "Nombre": "Alejandro", "Carrera": "Mecatrónica"}


#Tupla
tupla = (1, 2, 4, "Hola", 1, 1)

a, b, c, d, e, f = tupla
_, g, _, h, _, _ = tupla


def funcion_prueba():
  x=20
  print(x)

def funcion_param(a:int, b:int=0, c:int=0):
  #Imprimir (a, b, c)
  print(a, b, c)
  q = "Las variables son: {}, {}, {}".format(a, b, c)
  print(q)
  suma = a+b+c
  print("suma: {}".format(suma))
  return suma

def suma_multiple(*args):
  suma = 0
  for i in args:
    suma+=i
  return suma

def generar_alumno(nombre, edad=20, carrera="mecatrónica", **kwargs):
  dicc = {"Nombre":nombre, 
          "Edad": edad, 
          "Carrera": carrera}
  for i, j in kwargs.items():
    dicc[i] = j
  return dicc

alumno = generar_alumno("Guillermo", Color="Azul", Tenis="SI")
print(alumno)
