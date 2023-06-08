
#Operadores comparativos
print(4<8)
print(4>8)
print(4==8) #Si usamos solo un = estamos asignando valor, pero si ponemos == estamos preguntando si es el mismo valor
print(4<=8)
print (4!=8)#Para saber si es diferente a


#Operadores comparativos con letras
print('hola'>'mundo')
print(len('hola')>len('bolas')) #Len cuenta la cantidad de caracteres que tiene cada plabra 
print('a'>'b')#Indica el posicionamiento de las letras dentro del Abecedario
print('a'<='a')


#Operadores Lógicos

#and el resultado se debe a que como hay un true y un false automaticamente lo vuelve false
print(4<6 and 7>9)
#or caso contrario con Or pues como si hay un true o un false pues automaticamente es un true (Una de dos pues)
print(4<6 or 7>9)
# Lo que hace es que si este resultado es falso lo convierte a verdadero y viceversa
print(not(4<6))
#Aplica lo aprendido 
print((not(7!=7)and 6>5 )and ('rozar'<'rotar' or not(3==5)))