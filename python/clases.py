class Ataque():
  """
  Representa un ataque
  """
  def __init__(self, nombre:str, poder:int):
    """
    Inicialización de atque
    Args:
      nombre (str): Nombre del ataque
      nivel (int): Nivel de poder del ataque
    """
    self.nombre = nombre
    self.poder = poder

class Pokemon():
  """
  Esta clase representa un pokemon
  """
  def __init__(self, nombre:str, nivel:int):
    """
    Constructor del pokemon

    Args:
      nombre (str): Nombre del pokemon
      nivel (int): Nivel del pokemon
    """
    self.nombre = nombre
    self.nivel = nivel
    self.ataques = []
  def agregar_ataque(self, ataque:Ataque):
    """
    Agrega un ataque al pokemon

    Args:
      ataque : Ataque a agregar
    """
    self.ataques.append(ataque)


if __name__ == "__main__":
  pokemon = Pokemon("Eevee", 15)
  ataque_nuevo = Ataque("Placaje", 35)
  pokemon.agregar_ataque(ataque_nuevo)
  print(pokemon.ataques[0].nombre)
