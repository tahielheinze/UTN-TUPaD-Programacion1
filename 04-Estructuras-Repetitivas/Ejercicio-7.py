# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario. 

numUser = int(input("Ingrese un número entero positivo: "))
num = 0

#Si el usuario ingresa un número menor o igual que 0 el programa le arroja un 'error' y le pide que ingrese nuevamente otro número.
while numUser <= 0:
    print("ERROR. El número ingresado no es un número entero positivo")
    numUser = int(input("Ingrese nuevamente un número entero positivo: "))

inicio = num #Definimos el número más chico y por donde empieza la suma.
fin = numUser #Definimos el número más grande y por donde finaliza la suma.

suma = 0

#Sumamos todos los números enteros entre 'inicio' y 'fin'.
for i in range(inicio,fin): 
    suma +=i

print(f"La suma de los números entre", num, "y", numUser, "es: ", suma)
