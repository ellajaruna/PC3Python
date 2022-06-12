# PREGUNTA 8:

# 1. IMPORTAR MODULO:

import operaciones

# 2. Constantes

BIENVENIDA = 'Bienvenido al menú iterativo. ¿Qué desea hacer?'
MSG = """¿Qué desea hacer? Elija una opción:
    1) Sumar dos números
    2) Restar dos números
    3) Multiplicar dos números
    4) Dividir dos números
    5) Salir
Opción: """

# Codigo

print(BIENVENIDA)
while True:
    try:
        x = int(input(MSG))
        if x == 1:
            a = int(input('Ingrese el primer número: '))
            b = int(input('Ingrese el segundo número: '))
            operaciones.suma(a,b)
        
        elif x==2:
            a = int(input('Ingrese el primer número: '))
            b = int(input('Ingrese el segundo número: '))
            operaciones.resta(a,b)
        elif x == 3:
            a = int(input('Ingrese el primer número: '))
            b = int(input('Ingrese el segundo número: '))
            operaciones.producto(a,b)
        elif x == 4:
            a = int(input('Ingrese el primer número: '))
            b = int(input('Ingrese el segundo número: '))
            operaciones.division(a,b)
        elif x == 5:
            print('Hasta Luego!')
            break
        else:
            print ('¡Opción Inválida! Intente otra vez.')
                
    except:
        print('¡Debe ingresar un número! Intente otra vez.')

# FIN