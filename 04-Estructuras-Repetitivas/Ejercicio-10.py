#  10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#Le pedimos al usuario que ingrese un valor numerico.
num = int(input("Ingrese un número: "))
numInvertido = 0
#Creamos un bucle el cual mientras la variable 'num' el ciclo se repetirá.
#Con la variable 'digitoUser' le indicamos al programa que en cada iteracion vaya guardando solo el ultimo digito usando el modulo '%'
#Con 'numInvertido' se actualiza multiplicando el valor anterior por 10 y sumando el nuevo valor.
#Con '//' eliminamos el ultimo digito ingresado por el usuario mediante una division entera, para que el programa no guarde siempre el mismo digito.
while num > 0:
    digitoUser = num % 10
    numInvertido = numInvertido * 10 + digitoUser
    num = num // 10
#Entregamos al usuario el número invertido.
print(f"El número ingresado invertido es: {numInvertido}")