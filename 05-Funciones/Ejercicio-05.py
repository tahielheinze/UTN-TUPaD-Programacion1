## Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes.
## Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#* Definicion de Funciones

def segundos_a_hora(segundos):
    horas = segundos / 3600
    print(f"Los segundos {segundos} pasados a horas son = {horas}")

#* Programa principal
segundos = int(input("Ingrese una cantidad de segundos: "))
segundos_a_hora(segundos)