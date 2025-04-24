# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. 

numeros = [8, 15, 3, 22, 7]
#Se genera una lista con datos int
numeros.remove(max(numeros))
#Se utiliza el .remove para que el número más grande dentro de esa lista sea eliminado
print (numeros)
#Se procede a imprimir por pantalla la lista sin el número más grande, en este caso el 22.