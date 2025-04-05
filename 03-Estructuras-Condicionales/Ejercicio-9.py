# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: 
#     ● Menor que 3: "Muy leve" (imperceptible). 
#     ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#     ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). 
#     ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). 
#     ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#     ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

Magnitud = float(input("Ingrese la magnitud de un terremoto: "))
muyLeve = (Magnitud > 0) and (Magnitud < 3)
Leve = (Magnitud >= 3) and (Magnitud < 4)
Moderado = (Magnitud >= 4) and (Magnitud < 5)
Fuerte = (Magnitud >= 5) and (Magnitud < 6)
muyFuerte = (Magnitud >= 6) and (Magnitud < 7)
Extremo = Magnitud >= 7
#Pre defino las variables para agilizar al momento de crear el algoritmo y si en algun futuro necesita un cambio me resultaria más facil ubicar y cambiarlo.

if muyLeve :
    print("Muy leve")
elif Leve :
    print("Leve")
elif Moderado :
    print("Moderado")
elif Fuerte :
    print("Fuerte")
elif muyFuerte :
    print("Muy Fuerte")
elif Extremo :
    print("Extremo")
else:
    print("ERROR: El número ingresado no es valido")

# Dependiendo del numero que ingreso el usuario y si corresponde a una de las opciones que hay en el programa, el mismo imprimira un mensaje explicando que tipo de terremoto es, en cambio si ingresa un valor no esperado se arroja un mensaje de ERROR.