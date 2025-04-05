# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

contraseniaUsuario = len(input("Ingrese una contraseña de entre 8 y 14 caracteres: "))

if contraseniaUsuario >= 8 and contraseniaUsuario <= 14:
    print("Ha ingresado una contraseña correcta") # Si el usuario ingresa una contraseña que equivalga a un valor entre 8 y 14 inclusive arroja el print "Ha ingresado una contraseña correcta"
else:
    print("ERROR: Por favor, ingrese una contraseña entre 8 y 14 caracteres") #Si el usuario ingresa una contraseña que no equivalga al valor anteriormente especificado arroja un "ERROR"