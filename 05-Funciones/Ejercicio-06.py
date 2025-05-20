## Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10.
## Pedir al usuario el número y llamar a la función.

#* Definicion de Funciones

def tabla_multiplicar(numero):
    contador = 0
    while contador < 10:
        contador = contador + 1
        resultado = numero * contador
        print(f"{numero} x {contador} = {resultado}")

#* Programa principal

numero = int(input("Ingrese un valor numérico: "))

tabla_multiplicar(numero)