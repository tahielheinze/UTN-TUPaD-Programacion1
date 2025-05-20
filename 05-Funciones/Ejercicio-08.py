## Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC).
## Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

#* Definicion de Funciones

def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc

#* Programa principal
#Bloque Try el cual veerificara que los datos ingresados sean mayores que 0 y en caso de no serlo lanzará un error.
#Dentro del Try el programa analizará segun los datos obtenidos por la funcion 'calcular_imc' si el usuario se encuentra en Bajo peso, Peso normal, Sobrepeso u Obesidad.
try:
    peso= float(input("Ingrese su peso en Kg: "))
    altura= float(input("Ingrese su altura en Metros: "))
    while peso <= 0 or altura <= 0:
        print("ERROR. Los datos ingresados no son aceptables, ingreselos nuevamente")
        peso= float(input("Ingrese su peso en Kg: "))
        altura= float(input("Ingrese su altura en Metros: "))
    else:
        imc= calcular_imc(peso, altura)
        print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")
        if imc < 18.5:
            print("Bajo Peso")
        elif imc >= 18.5 and imc < 25:
            print("Peso normal")
        elif imc >= 25 and imc <30:
            print("Sobrepeso")
        else:
            print("Obesidad")
except ValueError: #En caso de que el usuario no haya ingresado algun valor que no esté permitido el programa lanzará el siguiente error y finalizará el código.
    print("ERROR. Los valores numéricos ingresdos no son válidos.")
