## Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

#! DEFINIR FUNCIONES

# Calcula el valor de Fibonacci en la posición 'num' de forma recursiva
def fibonacci(num):
    # Caso base: si num es 0 retorna 0
    if num == 0:
        return 0
    # Caso base: si num es 1 retorna 1
    elif num == 1:
        return 1
    # Llamada recursiva para calcular el valor
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

#! PROGRAMA PRINCIPAL

num = int(input("Ingrese un número: "))

for i in range(0, num +1):
    print("┌─────────────────────────────────────")
    print(f"│ El valor de la serie de Fibonacci en la posición {i} es: {fibonacci(i)}")
    print("└─────────────────────────────────────")


