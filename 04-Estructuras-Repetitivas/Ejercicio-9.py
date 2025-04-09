# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

#Inicializamos las variables necesarias.
contador = 0
suma = 0
media = 0

# Creamos un bucle que se repite 100 veces. En cada iteración, se solicita un número al usuario.
# Se van aumentandos los contadores especificos como 'contador' para que el bucle no sea infinito y el de 'suma' para ir guardando los valores ingresados por el usuario.
while contador < 100:
    contador = contador + 1
    num = int(input(f"Ingrese el número entero N°{contador} : "))
    suma = suma + num

#Para calcular la media necesitamos la suma de todos los valores ingresados por el usuario dividido por la cantidad de veces que el usuario ingreso valores, en este caso esa cantidad es la misma que almacena la variable 'contador'.

media = suma / contador
print(f"La cantidad de valores ingresados es: {contador}")
print(f"La media de los valores ingresados es: {media}")