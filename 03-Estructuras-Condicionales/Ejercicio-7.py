# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

fraseUsuario = input("Ingrese una frase o palabra: ")
vocales = ("a","e","i","o","u","á","é","í","ó","ú")

if fraseUsuario.lower().endswith(vocales): 
#fraseUsuario.lower() = Convierte la frase/palabra ingresada por el usuario en minusculas para que no importe como lo ingrese.
#.endswith(vocales) = El programa analiza si la última letra del texto ingresado por el usuario está dentro de la variable vocales, y si es así, devuelve True.
    fraseUsuario += "!" # Al dar el programa True le agrega al final el signo "!" como pide el enunciado.
    print(fraseUsuario)
else:
    print(fraseUsuario) #Si el usuario ingresa una frase/palabra que no termina en vocal el programa devuelve lo mismo que ingreso.