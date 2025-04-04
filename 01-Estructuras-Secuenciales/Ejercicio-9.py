# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

cels = float(input("Ingrese la temperatura en Grados Celsius: "))
fahr = (cels * 9 / 5) + 32
print("Los Grados Celsius(",cels,"°C) a Grados Fahrenheit es: ", fahr,"°F")