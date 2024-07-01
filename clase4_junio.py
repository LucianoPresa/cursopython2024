'''print(1+9)
#podes comentar el codigo con # numeral adelante (una sola linea)

print (25+25)

print (30-5)
print (30.5-5)
dni = 35944440 #pones el dni y lo llamas con print abajo
print (dni) '''
# metodo de salida print()
#metodo de entrada input()
# nombre = input("hola, escribi tu nombre:") sin el numeral es para completar

'''
print (nombre)
a = 20
b = 30
print (a+b)


e = 30
f = int(input("cual es tu edad")) 
# print (e+f) sin el numeral se suman las edades
"

cadena_de_texto = "Python"
anio_del_curso = "2024"
print (cadena_de_texto + anio_del_curso)

print (cadena_de_texto[2]) #imprime el caracter numero 2 arranca de 0 (0;1;2;3;4;5. etc)
'''

# funcion LEN sirve para contar los caracteresa
#### ejemplo #### print(LEN("hola soy un string"))

#funcion SLICING [inicio:fin:paso]
#inicio va a ser el indice del primer caracter del string que queremos rebanar
#fin va a ser el indice del ultimo caracter no incluido del string que queremos rebanar
#paso: invida cada cuantos caracteres seleccionaremos entre las posiciones del inicio y fin

'''
saludo = "hola, como estan?"
saludo[0:4:1]
print(saludo[0:4:1])
 
 # listas y tuplas
 
mi_lista = [-11,20,3,41]
print(mi_lista)
otra_lista = ["hola","como", "estas", "?"]

variable_1 = "una variable"
listita = [1, -10, 132.5, "un string","otro string", variable_1]
print(listita)

listita(listita + [otra_lista, "algo random"])
'''

'''
numeros = [0,1,2,3,4,5,6,7,8,9,10]
print(numeros)
                                            
numeros = [0,2,4,5,10,15,20]
numeros[3] = 8
print(numeros)                          se reemplaza el 3 por un 8
'''

#funcion POP es todo lo contrario a "append" porque va a elimiar el ultimo item de la lista
# - pop.()

#FUNCION COUNT cuenta el numero de veces que se repite el item
# numeros_varios = [1,2,3,4,5,6,7,8,9,10,10,10,10,10,11,12,13,14,59]
# print(numeros_varios.count(10))

#____________________TUPLAS hace que no se pueda modificar (se declaran con parentesis)

# mi_tupla = (1,2,3,4,5)
  # print(mi_tupla)
 
 
 #Tarea
lista_1 = ["4567", "UNAHUR"]
print(lista_1)

lista_2 = ["EDUCACION", "789"]
print(lista_2)

lista_3 = [lista_1]
lista_1.pop()
print(lista_1)

lista_4 = [lista_2]
lista_2.pop()
print(lista_4)

lista_5 = [lista_3, lista_4]
print(lista_5)

tupla_luciano = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)
print(tupla_luciano[-1])
print(len(tupla_luciano))
print(tupla_luciano.index(15))
print(tupla_luciano.index(8))
print(tupla_luciano.count(12))
print(tupla_luciano.index[15,16,17,18])