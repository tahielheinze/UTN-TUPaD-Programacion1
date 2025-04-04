# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro

radio = float(input("Ingresa el radio de un círculo: "))
pi = 3.1416
diam = 2 * radio
area = pi * (radio ** 2)
perim = pi * diam
print("El área del circulo es:", area, "el perimetro del circulo es:", perim)