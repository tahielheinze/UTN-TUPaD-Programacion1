## Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.
## Mostrar los resultados de forma clara.

#* Definicion de Funciones

def validar_b(b):
    while b <= 0:
        print("ERROR. El segundo número no puede ser 0")
        b = int(input("Ingrese un valor numérico (mayor que 0) para el N°2: "))
        return b
    else:
        return b


def operaciones_basicas(a, b):
    sumar= (a + b)
    restar= (a - b)
    multiplicar= (a * b)
    dividir= (a // b)
    
    print(f"La suma de {a} + {b} es = {sumar}")
    print(f"La resta de {a} - {b} es = {restar}")
    print(f"La multiplicación de {a} x {b} es = {multiplicar}")
    print(f"La división de {a} / {b} es = {dividir}")



#* Programa principal

a = int(input("Ingrese un valor numérico para el N°1: "))
b = int(input("Ingrese un valor numérico para el N°2: "))
b = validar_b(b)

operaciones_basicas(a, b)