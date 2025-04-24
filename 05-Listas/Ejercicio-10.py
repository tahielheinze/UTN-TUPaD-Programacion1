# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
# ● Posición lista_anidada[0]: 15 
# ● Posición lista_anidada[1]: True 
# ● Posición lista_anidada[2][0]: 25.5 
# ● Posición lista_anidada[2][1]: 57.9 
# ● Posición lista_anidada[2][2]: 30.6 
# ● Posición lista_anidada[3]: False 
# Imprimir la lista resultante por pantalla.

lista_anidada = [[15], [True], [25.5, 57.9, 30.6],[False]]
print("---------------------------------------------------------")
print(f"La lista entera se ve asi:", lista_anidada)
print("---------------------------------------------------------")
print(f"La primer lista anidada contiene:",lista_anidada[0])
print("---------------------------------------------------------")
print(f"La segunda lista anidada contiene:",lista_anidada[1])
print("---------------------------------------------------------")
print(f"La tercer lista anidada contiene:",lista_anidada[2])
print(f"En la primer posición contiene:", lista_anidada[2][0])
print(f"En la segunda posición contiene:", lista_anidada[2][1])
print(f"En la tercer posición contiene:", lista_anidada[2][2])
print("---------------------------------------------------------")
print(f"La cuarta lista anidada contiene:",lista_anidada[3])
print("---------------------------------------------------------")