# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

#Solicitamos al usuario que ingrese dos números enteros
num1 = int(input("Ingrese el valor del primer número: "))
num2 = int(input("Ingrese el valor del segundo número: "))
suma = 0

while num1 != 0 or num2 != 0: #Mientras el usuario no indique que desea terminar el bucle, el programa repetira el bloque de código.
    suma = suma + num1 + num2 #Sumamos los valores que vaya ingresando el usuario y lo guardamos en la variable 'suma'
    print(suma)
    num1 = int(input("Ingrese el valor del primer número, si desea finalizar ingrese 0 [cero]: "))
    num2 = int(input("Ingrese el valor del segundo número, si desea finalizar ingrese 0 [cero]: "))

print(f"El total de la suma de los números ingresados es: ", suma)