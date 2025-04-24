# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
# pantalla los dos primeros. 

#Genero una lista con un range donde 10 es el valor inicial, 31 el limite y 5 el paso que toma el programa.
listaNum = list(range(10,31,5))

#Le indico al programa que imprima por pantalla los primeros 2 numeros de la lista generada.
print(f"El primer número de la lista es:",listaNum[0])
print(f"El segundo número de la lista es:",listaNum[1])
