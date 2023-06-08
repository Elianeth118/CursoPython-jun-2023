#Se repite algo hasta que indiquemos que no se repite
#WHILE esto se repetira hasta que no se cumpla la indicación

numero=0
while numero <10:
 numero+= 1
 print(numero)
 if numero <5:
         print('es igual que 5')
 elif numero == 5:
     print('es menor que 5')
     break #Termina el ciclo al cumplir la condicion a la que este ligado
print('bye')
 #FOR
 #Imprimir todos los datos de la lista
lista=[12,10,14,25,36]
for number in lista:
     print(number) 
#Imprimir La cantidad de veces que queramos
lista=[12,10,14,25,36]
for number in range(10):
     print(number) 