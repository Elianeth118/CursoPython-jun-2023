#La diferencia entre las listas y los sets son que en los sets no existe un orden siempre manejara un orden aleatorio de oreden
my_set={'python','javaScript','C++'}
print(type(my_set))
print(my_set)
#No acepta elementos repetidos
my_set.add('python')
print(my_set)
#Funcion que nos manda la diferencia entre dos sets
my_set_1={'python','javaScript','C++','c#'}
my_set_1.difference_update(my_set)
print(my_set_1)
