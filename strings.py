#Strings

mi_primer_string="Mi string con comillas dobles"
mi_second_string='mi string con comillas somples'
print(mi_primer_string, mi_second_string)
print(f'esto es un texto de una variable {mi_second_string} shshsh')
#Que un string tenga diferentes variables

variable='Hola'
var_a,var_b,var_c, var_d = variable

#Cada variable toma el valor de la primera letra
print(var_a) # =H
print(var_b)# = o
print(var_c) # =l
print(var_d)# =a
print(f'{var_a}{var_b}{var_c}{var_d}')

#Funciones de Strings

print(mi_primer_string.capitalize())#Pone la primera letra en mayuscula

print(mi_primer_string.lower())#Pone todas las letras en minusculas

print(len(mi_primer_string))#Cuenta la cantidad de caracteres que tiene el conteido de la variable con todo y espacio

print(mi_primer_string.upper())# La funcion upper pone todos los caraceres en mayusculas

print(mi_primer_string.find('r'))#Te dice hasta que pocision esta la letra r en la variable 
print(mi_primer_string.count('c')) #Cuanta la cantidad de veces que hay un caracter en  la variable
print(mi_primer_string.upper().isupper())#Pregunta si todo esta escrito en mayusculas
