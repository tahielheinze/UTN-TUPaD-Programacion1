## Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.

#! DEFINIR FUNCIONES

def potencia(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    else:
        # Llamada recursiva: multiplica la base por la potencia decreciendo el exponente
        return base * potencia(base, exponente - 1)

#! PROGRAMA PRINCIPAL

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

#! MOSTRAR RESULTADOS

print("┌───────────────────────────────────────────────")
print(f"│ La potencia de {base} elevado a {exponente} es: {potencia(base, exponente)}")
print("└───────────────────────────────────────────────")






