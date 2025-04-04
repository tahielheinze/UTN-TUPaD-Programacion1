# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

seconds = int(input("Ingresa una cantidad de segundos: "))
hora = float(seconds / 3600)
print("La cantidad de segundos (",seconds,") pasados a horas son =", hora)