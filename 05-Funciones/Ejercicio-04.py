## Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
## calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
## Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

## Importamos el modulo math que contiene el valor de Pi
import math 

#* Definicion de Funciones

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro


#* Programa principal

radio = int(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El Área del círculo es: {area:.3f} y el Perímetro del círculo es: {perimetro:.3f}")
# La funcion :.3f redondea el numero a 3 decimales