## Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
## Solicitar los números al usuario y mostrar el resultado usando esta  función.

#* Definir funciones

def calcular_promedio(a,b,c):
    numeros= [a, b, c] #almaceno los numeros ingresados por el usuario en una variable.
    divisor= len(numeros) #identifico la cantidad exacta de números que ingreso el usuario y luego ese dato pasará a ser el divisor para obtener el promedio.
    promedio = sum(numeros) / divisor
    return promedio

#* Programa principal

a= int(input("Ingrese el valor del primer número: "))
b= int(input("Ingrese el valor del segundo número: "))
c= int(input("Ingrese el valor del tercer número: "))

promedio = calcular_promedio(a,b,c)

print(f"El promedio de los numeros ingresados es: {promedio}")