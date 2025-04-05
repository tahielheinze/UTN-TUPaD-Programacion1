# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".

numeroValido = int(input("Ingrese solamente números pares: "))

if numeroValido % 2 == 0:
    print("Ha ingresado un número par") # Si el usuario ingresa un valor y el resto de la division de ese numero es 0, entonces es un número par y por ende imprime este print.
else:
    print("Por favor, ingrese un número par") # Si el usuario ingresa un valor y el resto de la division de ese numero no es 0, entonces es un número impar y por ende imprime este print.