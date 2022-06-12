# PREGUNTA 2:

while True:
    calificaciones = input('Ingrese una lista de calificaciones separadas por comas: ')
    lista = calificaciones.split(",")
    lista_entero = []

    try:
        for nota in lista:
            lista_entero.append(int(nota))

        print(f'Notas: {lista_entero}')   
        
        break
        
    except:
        print('''Los valores no pueden ser introducidos debido a un error de tipeo o formato.\nIntente nuevamente.\n''')

# FIN