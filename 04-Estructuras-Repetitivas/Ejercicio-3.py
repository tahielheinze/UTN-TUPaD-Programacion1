#  3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

#Solicitamos al usuario que ingrese dos números enteros
num1 = int(input("Ingrese el valor al primer número: "))
num2 = int(input("Ingrese el valor al segundo número: "))

inicio = min(num1 , num2) + 1  #Hacemos que el programa determine que número es el más chico y por ende empiece despues de ese.
fin = max(num1 , num2) #Hacemos que el programa determine que número es el más grande y por ende termina antes de ese.

suma = 0 # Inicializamos la variable 'suma' con el valor 0

for i in range(inicio,fin): #Sumamos todos los números enteros entre 'inicio' y 'fin', excluyendo los valores ingresados por el usuario.
    suma +=i 

print(f"La suma de los números entre", num1, "y", num2, "es: ", suma)

