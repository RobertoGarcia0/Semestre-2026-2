#!/usr/bin/env python3
from clases import Pokemon, Ataque

pokemon_nuevo = Pokemon("Flareon", 60)
ataque_nuevo = Ataque("Lanzallamas", 90)

pokemon_nuevo.agregar_ataque(ataque_nuevo)

print(pokemon_nuevo.ataques[0].nombre)