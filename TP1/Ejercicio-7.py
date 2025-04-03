# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese el valor del N°1: "))
num2 = int(input("Ingrese el valor del N°2: "))
while num1 == 0 or num2 == 0:
    print("El número ingresado debe ser distinto de 0 (cero)")
    num1 = int(input("Nuevamente ingrese el valor del N°1: "))
    num2 = int(input("Nuevamente ingrese el valor del N°2: "))
suma = num1+num2
divi = num1/num2
mult = num1*num2
rest = num1-num2
print(num1, "+", num2, "=", suma)
print(num1, "/", num2, "=", divi)
print(num1, "x", num2, "=", mult)
print(num1, "-", num2, "=", rest)