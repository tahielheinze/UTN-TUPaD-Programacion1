## Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

#! Definir Funciones

def contar_digito(numero,digito):
    if numero == 0: #Si el número es 0, no quedan más digitos que revisar.
        return 0
    else:
        ultimo_digito = numero % 10 #Sacamos el ultimo digito
        resto = numero // 10 #Eliminamos el ultimo digito

        if ultimo_digito == digito:
            return 1 + contar_digito(resto, digito)
        else:
            return 0 + contar_digito(resto, digito)

#! Programa Principal

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito que desea buscar: "))

#! Mostrar Resultado

print(f"La cantidad de veces que aparece el dígito buscado es: {contar_digito(numero, digito)}")