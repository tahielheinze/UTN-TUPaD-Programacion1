#  5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random #Importo el módulo random.

print("\nBIENVENIDO A UN JUEGO DE AZAR, PARA ESCAPAR DE ESTE BUCLE INFINITO DEL TERROR DEBE ACETAR EL NÚMERO DESCONOCIDO\n")

#Inicializo la variable 'numAzar' para que conserve el numero al azar entre 0 y 9.
numAzar = random.randint(0,9) 

numero = int(input("Para advinar el número al azar ingrese un número entre 0 y 9: "))

#Inicializamos la variable 'contador' para saber la cantidad de intentos que lleva el usuario para adivinar el número al azar.
contador = 1

#Mientras el número ingresado por el usuario, sea incorrecto el programa repite el bucle indefinidamente.
while numero != numAzar: 
    contador= contador + 1
    numero = int(input("FALLASTE. Intenta con otro número: "))

#Una vez que el usuario adivino el número al azar, se arroja el siguiente print.
if numero == numAzar:
    print(f"¡Felicidades! lograste escapar del bucle en tan solo", contador, "intentos")