## Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.

#! DEFINIR FUNCIONES

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

#! PROGRAMA PRINCIPAL

num = int(input("Ingrese un número: "))

for i in range(1, num +1):
    print("┌─────────────────────────────────────")
    print(f"│ El factorial de {i} es: {factorial(i)}")
    print("└─────────────────────────────────────")

