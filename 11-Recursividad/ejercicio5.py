## Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos: La solución debe ser recursiva. No se debe usar [::-1] ni la función reversed().

#! DEFINIR FUNCIONES

def es_palindromo(palabra):
    # Caso base: cadena vacía o de un solo carácter
    if len(palabra) == 0 or len(palabra) == 1:
        return True
    else:
        # Compara primer y último carácter
        if palabra[0] == palabra[-1]:
            # Recursión: verifica el resto de la cadena
            return es_palindromo(palabra[1:-1])
        else:
            # Caracteres diferentes, no es palíndromo
            return False

#! PROGRAMA PRINCIPAL

palabra = str(input("Ingrese una cadena/palabra: "))

#! MOSTRAR RESULTADO

if es_palindromo(palabra):
    print(f"{palabra} SI es Palíndromo")
else:
    print(f"{palabra} NO es Palíndromo")