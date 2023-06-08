#Primera diferencia entre tupla y lista la lista va en [] y la tupla en ()
my_tupla=(43,'eli',7.2,True)
print(type(my_tupla))
#Imprimir un valor especifico de la tupla buscano la posiscion del elemento

print(my_tupla[1])
#Contar la cantidad de veces que aprece el elemento en la tupla

print(my_tupla.count(43))
#Saber la posicion del elemento en la tupla

print(my_tupla.index('eli'))

#En las tuplas no se pueden insertar ni eliminar elementos

#Convertir una tuple en lista
my_tupla=list(my_tupla)
print(type(my_tupla))
#Ahora puedes ocupar las funciones de lista porque ya no es tupla
my_tupla.remove(True)
print(my_tupla)
#Convertir una lista en tupla
my_tupla=tuple(my_tupla)
print(type(my_tupla))