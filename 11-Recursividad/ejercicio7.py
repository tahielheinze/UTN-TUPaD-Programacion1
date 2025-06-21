## Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
## Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

#! Definir Funciones.

def contar_bloques(n):
    if n <= 0: #Caso base: la cantidad va a ser 0
        return 0
    else:
        return n + contar_bloques(n - 1) #Recursividad sumando la cantidad de bloques necesarios hasta llegar a 0.

#! Programa Principal.

n = int(input("Ingrese un valor numérico mayor que 0: "))

#! Mostrar Resultados.

print(f"El total de bloques necesarios para construir una piramide con base {n} es: {contar_bloques(n)}")