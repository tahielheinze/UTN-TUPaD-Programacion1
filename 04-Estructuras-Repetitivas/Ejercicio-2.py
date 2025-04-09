#  2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numUser = input("Ingrese un número entero: ") #Pido el número al usuario y queda guardado como string

if numUser.startswith("-"): 
    numUser = numUser[1:]
#Si el usuario ingresa un número negativo por ejemplo -12, el programa borra el "-" para contar los dígitos que contiene
if numUser.isdigit(): 
    cantDigitos = len(numUser) 
    print(F"La cantidad de dígitos que contiene el número ingresado es: {cantDigitos}")
#.isdigit() = devuelve un True si todos los caracteres de la string ingresada por el usuario son dígitos
#len() = se encarga de contar la cantidad de digitos que contiene la variable numUser.
else:
    print("ERROR. El número ingresado no es valido") 
#Si el usuario ingresa por ejemplo 12-32 el programa lo detecta y le lanza este error.
