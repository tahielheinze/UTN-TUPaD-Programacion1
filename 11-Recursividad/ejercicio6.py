## Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
## Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.

#! DEFINIR FUNCIONES
#Suma recursivamente los dígitos de un número
def suma_digitos(n):
    if n <= 0:
            print("ERROR. El número ingresado no es valido") #Número debe ser positivo
    elif n <10: #Caso base: número de un dígito
            return n
    else:
            return (n % 10) + suma_digitos(n // 10) #Suma último dígito + recursión con resto

#! PROGRAMA PRINCIPAL

n = int(input("Ingrese un número entero positivo: "))

#! MOSTRAR RESULTADOS

print(f" La suma de todos los dígitos de {n} es: {suma_digitos(n)}")