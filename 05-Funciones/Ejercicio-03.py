##Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) 
# que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

#* Definicion de Funciones
def validar_edad(edad):
    while edad < 1 or edad > 120:
        print("ERROR. El valor ingresado no es valido")
        edad = int(input("Ingrese su edad nuevamente: "))
    else:
        return edad


def validar_residencia(residencia):
    while not residencia.isalpha():
        print("ERROR. Ingrese un lugar correcto para su residencia")
        residencia = input("Ingrese su residencia nuevamente: ")
    else:
        return residencia


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


#* Programa principal
nombre= input("Ingrese su nombre: ")
apellido= input("Ingrese su apellido: ")
edad= int(input("Ingrese su edad: "))
edad = validar_edad(edad)
residencia= input("Ingrese su lugar de residencia: ")
residencia = validar_residencia(residencia)

informacion_personal(nombre,apellido,edad,residencia)