## Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

#! DEFINIR FUNCIONES

def binario(num):
    # Caso base: si el número es 0, retorna cadena vacía
    if num == 0:
        return ""  
    else:
        # Caso recursivo: divide por 2 y concatena el residuo
        return binario(num // 2) + str(num % 2)


#! PROGRAMA PRINCIPAL

num = int(input("Ingrese un número: "))

#! MOSTRAR RESULTADOS

print("┌─────────────────────────────────────────────────────────────")
print(f"│ La representación en binario de {num} es: {binario(num)}")
print("└─────────────────────────────────────────────────────────────")







