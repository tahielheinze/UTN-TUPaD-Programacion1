## -=_Generar una tabla de multiplicar usando funciones._=-
## Crea una función tabla_multiplicar que reciba un número entero positivo. 
## Devuelve una lista con su tabla de multiplicar del 1 al 10. 

#* =============================================
#* DEFINIR FUNCIONES
#* =============================================

def validar_numero_positivo(num):  
    """
    Valida que el número ingresado sea entero positivo. Si no lo es, solicita un nuevo valor hasta que sea válido.
    """
    while num <= 0:  # Repetir el bucle hasta que el usuario ingrese un número valido.
        print("ERROR. El número ingresado debe ser entero positivo")
        num = int(input("Ingrese nuevamente un número entero positivo: "))
    else:
        return num 

def tabla_multiplicar(num): 
    """
    Imprime la tabla de multiplicar del número dado, ya validado, desde 1 hasta 10 inclusive.
    """
    contador = 1 # Inicia en 1 porque no se multiplica por cero.
    while contador <= 10: # Genera tabla hasta 10 inclusive.
        resultado = num * contador 
        print(f"{num} x {contador} = {resultado}")
        contador = contador + 1 # Incrementar para avanzar en la tabla.

#* =============================================
#* PROGRAMA PRINCIPAL
#* =============================================

num = int(input("Ingrese un número entero positivo: ")) # Solicitar número al usuario.

num_validado = validar_numero_positivo(num) # Validar el número ingresado.

tabla_multiplicar(num_validado) # Generar y mostrar la tabla de multiplicar.

#* =============================================
#* PREGUNTAS de REFLEXIÓN
#* =============================================
# ¿Cómo adaptarías la función para recibir el rango (ej: hasta 12)? 
"""
    Cambiaría el limite del bucle while en la funcion de 'tabla_multiplicar'
    while contador <= 12:
"""
# ¿Qué ocurre si se ingresa un número negativo? 
"""
    Si se ingresa un número negativo, el programa lo detectará como un 'ERROR' debido a la funcion 'validar_numero_positivo', la cual le pedirá al usuario que ingrese otro número indefinidamente hasta que el usuario ingrese un número entero positivo.
"""