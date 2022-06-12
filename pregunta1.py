# PREGUNTA 1:

while True:
    try:
        fraccion = input('''Ingrese una fracción en formato X/Y . Donde "X" e "Y" son números enteros.
        Fracción: ''')
        
        X , Y = fraccion.split("/")
        
        if int(Y) >= int(X):
           
            porcentaje = round((int(X) / int(Y))*100)

            if porcentaje < 1:
                print("E") 
            elif porcentaje > 99:
                print("F")
            else:
                print(f'{porcentaje}%')
            
            break # Fin de la iteración
                
        else:
            print('"X" debe ser mayor o igual a "Y"\n')
            
    except ValueError:
        # Cuando "X" e "Y" son no son numeros enteros
        print('Solo se permiten numeros enteros. Ingrese nuevamente la fracción.\n')
    except ZeroDivisionError:
        # Cuando Y == 0
        print('El denominador no puede ser 0. Ingrese nuevamente la fracción.\n')
              

# FIN