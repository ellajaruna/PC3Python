# 1. Se importa el modulo random:

import random

# 2. Funciones

def numeros_aleatorios():
    lista = []
    i = 1
    while i <=20:
        lista.append(random.randint(0 , 100))
        i+=1
        
    print(f'Números seleccionados aleatoriamente: {lista}')

    
def ordenar():
    lista = []
    i = 1
    while i <=20:
        lista.append(random.randint(0 , 100))
        i+=1
        
    lista.sort()
    print(f'Valores ordenados: {lista}')

# FIN


