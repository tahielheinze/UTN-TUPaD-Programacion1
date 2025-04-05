# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 
#     1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#     2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#     3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.

nombreUsuario = input("Ingrese su nombre: ")
print("Ingrese una opcion: [1] Mayúsculas / [2] Minúsculas / [3] Primer letra mayúscula")
numUsuario = int(input(""))

if numUsuario == 1:
    print(nombreUsuario.upper()) #Si el usuario ingresa el número 1, el programa entrega el nombre con todas las letras en Mayúsculas
elif numUsuario == 2:
    print(nombreUsuario.lower()) #Si el usuario ingresa el número 2, el programa entrega el nombre con todas las letras en Minúsculas
elif numUsuario == 3:
    print(nombreUsuario.capitalize()) #Si el usuario ingresa el número 3, el programa entrega el nombre con la primer letra en Mayúsculas
else:
    print("ERROR: El número ingresado no es valido") #Si el usuario ingresa un número no esperado, el programa entrega un mensaje de ERROR.