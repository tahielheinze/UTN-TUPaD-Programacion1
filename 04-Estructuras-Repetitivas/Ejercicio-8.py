# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#Inicializamos las variables necesarias para el problema.
contador = 0
numPar = 0
numImpar = 0

# Creamos un bucle que se repite 100 veces. En cada iteración, se solicita un número al usuario.
# Luego se verifica si el número ingresado es par o impar utilizando el operador módulo (%) y se actualizan los contadores.
while contador < 100:
    contador = contador + 1
    num = int(input(f"Ingrese el número entero N°{contador} : "))
    if num % 2 == 0:
        numPar = numPar + 1
    else:
        numImpar = numImpar + 1

print(f"La cantidad de números ingresados totales son: {contador}")
print(f"La cantidad de números pares ingresados son: {numPar}")
print(f"La cantidad de números impares ingresados son: {numImpar}")