
#? 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola Mundo!")

#? 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”.

nombre = input("Ingresa tu nombre: ")
saludo = "Hola "+nombre
print(saludo)

#? 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 

nombre = input("Ingresa tu nombre y apellido: ")
edad = input("Ingresa tu edad: ")
lugar = input("Ingresa el lugar donde vivis: ")
print(nombre, "de edad", edad, "años", "con lugar de residencia en", lugar )

#? 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro

radio = float(input("Ingresa el radio de un círculo: "))
pi = 3.1416
diam = 2 * radio
area = pi * (radio ** 2)
perim = pi * diam
print("El área del circulo es:", area, "el perimetro del circulo es:", perim)

#? 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

seconds = int(input("Ingresa una cantidad de segundos: "))
hora = float(seconds / 3600)
print("La cantidad de segundos (",seconds,") pasados a horas son =", hora)

#? 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

num1 = int(input("Ingrese el valor al número: "))
cont = 1
for cont in range(1,11):
   cuenta = num1 * cont
print(num1, "x" , cont, "=", cuenta )

#? 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

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

#? 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

altu = float(input("Ingrese su altura en metros (ejemplo: 1.75): "))
peso = float(input("Ingrese su peso en Kg: "))
maCo = peso / altu ** 2
print("Su masa corporal es:",peso, "/", altu, "=", maCo)

#? 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

cels = float(input("Ingrese la temperatura en Grados Celsius: "))
fahr = (cels * 9 / 5) + 32
print("Los Grados Celsius(",cels,"°C) a Grados Fahrenheit es: ", fahr,"°F")

#? 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num1 = int(input("Ingrese el valor del N°1: "))
num2 = int(input("Ingrese el valor del N°2: "))
num3 = int(input("Ingrese el valor del N°3: "))
prom = (num1 + num2 + num3) / 3
print("El promedio de los numeros ingresados es:", prom)