# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: 
# a) Agregar "jugo" a la lista del tercer cliente usando append. 
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
# c) Eliminar "pan" de la lista del primer cliente.  
# d) Imprimir la lista resultante por pantalla 

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 

#Agrego "jugo" a la tercer lista.
compras[2].append("jugo")

#Reemplazo "fideos" por "tallarines" de la segunda lista. 
# Accedo a la lista del segundo cliente con el primer [1] y al segundo prducto  de la lista ("fideos") con el segundo [1].
compras[1][1] = "tallarines"

#Elimino "pan" de la primer lista.
compras[0].remove("pan")

#Imprimo la nueva lista modificada.
print(compras)