# ....FUNCIONES....

# Función suma:
def suma(a,b):
    s = a + b
    print(f'La suma es: {s}')


# Función resta:
def resta(a,b):
    r = a - b
    print(f'La resta es: {r}')

# Funció producto:
def producto(a,b):
    p = a * b
    print(f'El producto es: {p}')

# Función división:
def division(a,b):
    try:
        d = a / b
        print(f'La divisió es: {d}')
    except ZeroDivisionError:
        print('Error! No es posible dividir entre cero.')

# FIN

