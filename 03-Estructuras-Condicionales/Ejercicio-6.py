#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean #importo el paquete que permite tomar una lista de números y calcular la moda, su mediana y su media
lista = [1,2,5,5,3]
mean(lista)

import random 
numerosAleatorios = [random.randint(1,100) for i in range(50)] #Genera una lista de 50 numeros aleatorios entre 1-100 

media = mean(numerosAleatorios)
mediana = median(numerosAleatorios)
moda = mode(numerosAleatorios)
sesgo = "Sesgo no determinado"
#Definimos las variables correspondiente a lo que plantea el problema, calcular la moda, su mediana y su media.

#Comparamos los valores obtenidos para determinar el Sesgo
if media > mediana and mediana > moda:
    sesgo = "Sesgo positivo o a la derecha"
elif media < mediana and mediana < moda:
    sesgo = "Sesgo negativo o a la izquierda"
elif media == mediana and mediana == moda:
    sesgo = "Sin sesgo"

#Imprimimos los resultados
print(f"Lista de los números aleatorios {numerosAleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Resultado: {sesgo}") #Si la Media > Mediana , Mediana < Moda y Media < Moda = El resultado sería "Sesgo no determinado"