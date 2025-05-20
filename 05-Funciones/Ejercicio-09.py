## Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.
## Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

#* Definicion de Funciones

def celsiues_a_fahrenheit(celsius):
    fahrenheit= (celsius * 1.8) + 32
    return fahrenheit

#* Programa principal

celsius= int(input("Ingrese los grados Celsius: "))
fahrenheit= celsiues_a_fahrenheit(celsius)

print(f"El pasaje de Celsius {celsius}°C  a Fahrenheit es: {fahrenheit}°F")