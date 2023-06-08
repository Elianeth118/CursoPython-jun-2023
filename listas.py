#LISTAS
my_list=['python',53,False, 45, 'elianeth']
print(type(my_list))
#Imprime la lista de todos los datos almavenados en la variable 
print(my_list)
# imprime 53 dado que en la programacion las cosas empiezan desde 0
print(my_list[1])
#Si utilizas el -1 te ayuda a imprimir el ultimo valor de la lista digamos que hace un conteo regresivo
print(my_list[-1])
#Ayuda a agregar un elemento a la lista
my_list.append(43)
print(my_list)
#Insertar un dato a la lista en un lugar especifico
my_list.insert(3,'Hola bola')
print(my_list)
#Eliminar datos de mi lista
my_list.remove('Hola bola')
print(my_list)
#Remover un dato en cierta posicion
my_list.pop(2)
print(my_list)
#podemos imprimir el valor que borró
print(my_list.pop(2))
print(my_list)
#Contar las cantidad de veces que aparece el dato en la lista
print(my_list.count(43))

#poner la lista al reves
my_list.reverse()
print(my_list)
#Borrar todo lo que contiene la lista
my_list.clear()
print(my_list)

