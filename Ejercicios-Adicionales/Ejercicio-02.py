## -=_Sumar elementos pares de una lista con una función._=-
## Define una función suma_pares que reciba una lista de enteros. 
## Retorna la suma de los números pares.

#* =============================================
#* DEFINIR FUNCIONES
#* =============================================

def validar_cant_numeros(cantidad_numeros):
    """
    Valida la cantidad de números que desea ingresar el usuario.
    - Si el valor es valido, lo retorna.
    - Si no, solicita un nuevo valor hasta que sea
    """
    while cantidad_numeros <= 0:
        print("ERROR. Debes ingresar un número entero positivo")
        cantidad_numeros = int(input("Ingresa nuevamente cuantos números deseas analizar: "))
    return cantidad_numeros

def suma_pares(lista_numeros):
    """
    Procesa una serie de números ingresados por el usuario:
    - Suma y verifica los números pares.
    - Cuenta el total de números pares e impares ingresados.
    """
    total_par = 0
    total_impar = 0
    total_suma = 0
    for numero_ingresado in lista_numeros:
        if numero_ingresado % 2 == 0:
            total_suma += numero_ingresado
            total_par += 1
        else:
            total_impar += 1
    return total_suma, total_par, total_impar

#* =============================================
#* PROGRAMA PRINCIPAL
#* =============================================

cantidad_numeros = int(input("¿Cuantos números deseas ingresar? "))
cantidad_numeros = validar_cant_numeros(cantidad_numeros)

"""
Una vez validada la cantidad de números que desea ingresar el usuario.
- Se guardan en la lista_numeros los numeros que vaya ingresando el usuario.
- Dependiendo de la cantidad de numeros que ingreso el usuario, determinará el largo de la lista.
"""
lista_numeros = []
for i in range(cantidad_numeros):
    numero_ingresado = int(input(f"Ingrese el valor para el N°{i+1}: "))
    lista_numeros.append(numero_ingresado)

total_suma, cant_pares, cant_impares = suma_pares(lista_numeros)

print(f"\n|===|RESULTADOS|===|\n")
print(f"Se analizarán {cantidad_numeros} números.")
print(f"Suma total de números pares: {total_suma}")
print(f"Cantidad de números pares: {cant_pares}")  
print(f"Cantida de números impares: {cant_impares}")


#* =============================================
#* PREGUNTAS de REFLEXIÓN
#* =============================================
#? ¿Cómo manejarías listas vacías o con decimales?
"""
Para listas vacias:
    - Agregaría una validación al inicio de suma_pares
    - Retornaría (0, 0, 0) o mostraría un mensaje especial
Para decimales:
    - 1) Convertir a int (truncando decimales)
    - 2) Usar float y modificar la función para manejar decimales
    - 3) Rechazar inputs con decimales mostrando error
"""
#? ¿Qué ventaja tiene usar una función en lugar de código inline?
"""
Reutilización: Puedes llamar la función muchas veces.

Modularidad: Cada función hace una cosa específica (principio SOLID).

Mantenibilidad: Es más fácil corregir errores en un solo lugar.

Legibilidad: El código principal se vuelve más claro.

"""