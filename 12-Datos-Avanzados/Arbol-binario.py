
#! ======= DEFINIR LAS FUNCIONES y CLASES =======

#* Definir la estructura Nodo del Arbol.
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

#* Inicializar el Arbol.
class ArbolBinario:
    def __init__(self):
        self.raiz = None

#* Insertar un valor en el árbol.
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

#* Buscar la posicion correcta e insertar el valor recursivamente.
    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, valor)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecha, valor)

#* Imprimir el árbol en formato In-Order (izquierda, raiz, derecha).
    def imprimir_en_orden(self, nodo_actual):
        if nodo_actual is not None:
            self.imprimir_en_orden(nodo_actual.izquierda)
            print(nodo_actual.valor)
            self.imprimir_en_orden(nodo_actual.derecha)

#* Mostrar el árbol de manera visual.
    def mostrar_arbol_visual(self, nodo_actual=None, prefijo="", es_ultimo=True):
        if nodo_actual is None:
            nodo_actual = self.raiz
        
        if nodo_actual is None:
            print("\n EL ÁRBOL ESTÁ VACÍO")
            return
        
        #* Mostrar nodo actual
        print(prefijo + ("└── " if es_ultimo else "├── ") + str(nodo_actual.valor))
        
        #* Preparar prefijo para hijos
        nuevo_prefijo = prefijo + ("    " if es_ultimo else "│   ")
        
        #* Contar hijos existentes
        tiene_izquierda = nodo_actual.izquierda is not None
        tiene_derecha = nodo_actual.derecha is not None
        
        #* Mostrar hijo (izquierdo)
        if tiene_izquierda:
            self.mostrar_arbol_visual(nodo_actual.izquierda, nuevo_prefijo, not tiene_derecha)
        
        #* Mostrar hijo (derecho)
        if tiene_derecha:
            self.mostrar_arbol_visual(nodo_actual.derecha, nuevo_prefijo, True)



#! ======= PROGRAMA PRINCIPAL =======

mi_arbol = ArbolBinario()

while True:
    print("="*60)
    entrada_usuario = input("Ingresa un elemento para el árbol (o 'fin' para terminar): ")
    print("="*60)

    if entrada_usuario == "fin" or entrada_usuario == "Fin" or entrada_usuario == "FIN":
        break
    
    mi_arbol.insertar(entrada_usuario)


#! ======= MOSTRRAR EL RESULTADO DEL ARBOL =======

print("╔═══════════════════════════════════╗")
print("║      VISUALIZACIÓN DEL ÁRBOL      ║")
print("╚═══════════════════════════════════╝")

mi_arbol.mostrar_arbol_visual()

print("")
print("═" * 60)

# Ejemplo1 a utilizar: 50, 30, 70, 20, 40, 60, 80, 10, 25, 35.
# Ejemplo2 a utilizar: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100.