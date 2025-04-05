# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edadUsuario = int(input("Ingrese su edad: "))

if edadUsuario <= 0 or edadUsuario >= 130:
    print("ERROR: Edad Ingresada no valida") # Si el usuario ingresa una edad no valida el programa le indicara que hay un error y debera ejecutar el programa nuevamente.
elif edadUsuario >= 18:
    print("Es mayor de edad") # Si el usuario ingresa una edad de 18 o superior a ella el programa arroja el resultado de "Es mayor de edad"
else:
    print("Es menor de edad") # Si el usuario ingresa una edad de 17 o menor a ella el programa arroja el resultado de "Es menor de edad"