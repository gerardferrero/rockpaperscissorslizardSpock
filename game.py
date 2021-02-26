from random import random
from os import system, name 

def jugada_ordenador():
    return int(random()*5)    

def jugada_humano():
    print("piedra(0), papel(1), tijeras(2), lagarto(3), Spock(4): ",end='')
    return int(input())

jugadas_posibles = ["piedra","papel","tijeras","lagarto","Spock"]
cuadro_ganador = [[0,-1,1,1,-1],
                  [1,0,-1,-1,1],
                  [-1,1,0,1,-1],
                  [-1,1,-1,0,1],
                  [1,-1,1,-1,0]]

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

ronda = 1
puntos_jugador = 0
puntos_ordenador = 0

clear()
while puntos_jugador<3 and puntos_ordenador<3:
    print(f"Ronda: {ronda} [Jugador: {puntos_jugador} - Ordenador: {puntos_ordenador}]")

    jugada_h = jugada_humano()
    jugada_pc = jugada_ordenador()

    print(f"El jugador ha sacado {jugadas_posibles[jugada_h]}. El ordenador ha sacado {jugadas_posibles[jugada_pc]}. ",end = '')

    if cuadro_ganador[jugada_h][jugada_pc] == 1:
        print("¡¡¡Gana el jugador!!!")
        puntos_jugador = puntos_jugador + 1
    elif cuadro_ganador[jugada_h][jugada_pc] == -1:
        print("¡¡¡Gana el ordenador!!!")
        puntos_ordenador = puntos_ordenador + 1
    else:
        print("Empate.")

    print("")

    ronda = ronda + 1

print(f"La partida ha acabado en {ronda-1} rondas.")
print(f"El marcador ha sido:  [Jugador: {puntos_jugador} - Ordenador: {puntos_ordenador}]")