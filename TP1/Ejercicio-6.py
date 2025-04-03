# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

num1 = int(input("Ingrese el valor al número: "))
cont = 1
for cont in range(1,11):
   cuenta = num1 * cont
print(num1, "x" , cont, "=", cuenta )