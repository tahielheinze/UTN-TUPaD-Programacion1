# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

edadUsuario = int(input("Ingrese su edad: "))

edadNinio = edadUsuario < 12
edadAdoles = edadUsuario >= 12 and edadUsuario <= 18
edadAdulJoven = edadUsuario >= 18 and edadUsuario < 30
edadAdulMayor = edadUsuario >= 30 and edadUsuario < 130
# Defino variables para cada uno de los resultados que pide el problema para que a la hora de usar la estructura condicional no tenga que repetir tantas veces las edades con su respectiva categoría.

if edadUsuario <= 0 or edadUsuario >= 130:
    print("ERROR: Edad ingresada no válida") #Si el usuario ingresa una edad no válida el programa arroja un error.
elif edadNinio:
    print("Usted es un Niño/a") #Si el usuario ingresa un valor que coincida con la variable predefinida edadNinio el programa arroja como resultado "Usted es un Niño/a"
elif edadAdoles:
    print("Usted es un Adolescente") #Si el usuario ingresa un valor que coincida con la variable predefinida edadAdoles el programa arroja como resultado "Usted es un Adolescente"
elif edadAdulJoven:
    print("Usted es un Adulto/a Joven") #Si el usuario ingresa un valor que coincida con la variable predefinida edadAdulJoven el programa arroja como resultado "Usted es um Adulto/a Joven"
elif edadAdulMayor:
    print("Usted es un Adulto/a Mayor") #Si el usuario ingresa un valor que coincida con la variable predefinida edadAdulMayor el programa arroja como resultado "Usted es un Adulto/a Mayor"