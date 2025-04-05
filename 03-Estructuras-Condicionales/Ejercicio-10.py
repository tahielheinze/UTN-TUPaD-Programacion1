# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año. Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.  
# Desde el 21 de diciembre hasta el 20 de marzo (incluidos) Estación en el hemisferio norte Invierno Estación en el hemisferio sur Verano
# Desde el 21 de marzo hasta el 20 de junio (incluidos) Estación en el hemisferio norte Primavera Estación en el hemisferio sur Otoño
# Desde el 21 de junio hasta el 20 de septiembre (incluidos) Estación en el hemisferio norte Verano Estación en el hemisferio sur Invierno
# Desde el 21 de septiembre hasta el 20 de diciembre (incluidos) Estación en el hemisferio norte Otoño Estación en el hemisferio sur Primavera

hemisferioUser = str(input("Ingrese en el hemisferio que se encuentra [N] Norte o [S] Sur: "))
mesUser = str(input("Ingrese el mes en el que se encuentra [1-12]: "))
diaUser = int(input("Ingrese el número del día en el que se encuentra [1-31]: "))

# Ya recolectamos la informacion que necesitamos que nos proporcione el usuario

# Definir la estacion en que nos encontramos dependiendo del mes,dia,hemisferio
def saberEstacion(hemisferioUser, mesUser, diaUser):
    if hemisferioUser == "N" or hemisferioUser == "n":
        if (mesUser == "3" and diaUser >= 21) or (mesUser == "4") or (mesUser == "5") or (mesUser == "6" and diaUser <= 20):
            return "Primavera"
        elif (mesUser == "6" and diaUser >= 21) or (mesUser == "7") or (mesUser == "8") or (mesUser == "9" and diaUser <= 20):
            return "Verano"
        elif (mesUser == "9" and diaUser >= 21) or (mesUser == "10") or (mesUser == "11") or (mesUser == 12 and diaUser <= 20):
            return "Otoño"
        elif (mesUser == "12" and diaUser >= 21) or (mesUser == "1") or (mesUser == "2") or (mesUser == "3" and diaUser <= 20):
            return "Invierno"
    elif hemisferioUser == "S" or hemisferioUser == "s":
        if (mesUser == "3" and diaUser >= 21) or (mesUser == "4") or (mesUser == "5") or (mesUser == "6" and diaUser <= 20):
            return "Otoño"
        elif (mesUser == "6" and diaUser >= 21) or (mesUser == "7") or (mesUser == "8") or (mesUser == "9" and diaUser <= 20):
            return "Invierno"
        elif (mesUser == "9" and diaUser >= 21) or (mesUser == "10") or (mesUser == "11") or (mesUser == "12" and diaUser <= 20):
            return "Primavera"
        elif (mesUser == "12" and diaUser >= 21) or (mesUser == "1") or (mesUser == "2") or (mesUser == "3" and diaUser <= 20):
            return "Verano"
    else:
        print("El Hemisferio ingresado no es valido")

# Definimos la variable estacion con los datos que recolectamos en saberEstacion
estacion = saberEstacion(hemisferioUser, mesUser, diaUser)
print(f"Te encuentras en la estacion {estacion}.")