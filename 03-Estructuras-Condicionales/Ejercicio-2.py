# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

notaUsuario = int(input("Ingrese la nota recibida: "))

if notaUsuario <= 0 or notaUsuario > 10:
    print("ERROR: La nota ingresada no es valida") # Si el usuario ingresa un valor no deseado el programa indicara que hay un error y debera ejecutar el prorgrama nuevamente
elif notaUsuario >= 6 and notaUsuario <= 10:
    print("Aprobado") # Si el usuario ingresa un valor entre 6 y 10 (inclusive) el programa arrojara el print "Aprobado"
else:
    print("Desaprobado") # Si el usuario ingresa un valor menor de 6 y mayor que 0 el programa arroja el print "Desaprobado"