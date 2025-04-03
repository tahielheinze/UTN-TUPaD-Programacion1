# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

altu = float(input("Ingrese su altura en metros (ejemplo: 1.75): "))
peso = float(input("Ingrese su peso en Kg: "))
maCo = peso / altu ** 2
print("Su masa corporal es:",peso, "/", altu, "=", maCo)