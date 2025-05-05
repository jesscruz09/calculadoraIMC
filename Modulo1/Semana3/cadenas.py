# texto_variado = 'palabra 123 &%$#'
# print(type(texto_variado))

#"podemos utiliozar comillas triples para que se muestre como la cadena que hemos escrito "
# print(""" 
# funcionamiento de  \
# programa: (opciones)
#     -1 para acceder a opciones
#         -2 para salir
# """)

# Subscripting e indexado

# texto = 'python'
# print(texto[0])
# print(texto[5])
# print(texto[-1])
# print(texto[-6])

# print(texto[6]) # error! no podemos acceder a una posicion que no existe
# print(texto[-7]) # Error! no podemos acceder a una posicion que no existe

# letra = texto[0]
# print(letra)

# texto[0] = 'P' # Error! no podemos modificar una cadena de texto

# letra = 'P'
# print(letra)

# texto_compuesto = letra + texto[1] # concatenar
# print(texto_compuesto)

###############################################################################

# Slicing o Substringing
# texto = 'Python'
# print(texto[0:3])
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:])
# print(texto[:3])

# print(texto[-3::-1]) # invertir la cadena desde la posicion -3 hasta el inicio 
# print(texto[::-1]) # invertir la cadena
# print(texto[2:2])

###############################################################################
# cadenas y formatos

# texto = 'Hola mundo! Buenas tardes'
# print(texto.lower()) # convertir a minusculas
# print(texto.upper()) # convertir a mayusculas
# print(texto.capitalize()) # convertir la primera letra a mayuscula
# print(texto.title()) # convertir la primera letra de cada palabra a mayuscula
# print(texto.swapcase()) # intercambiar mayusculas y minusculas
# texto = texto.upper() # convertir a mayusculas
# print(texto) # convertir a mayusculas
# print(texto.count('a')) # contar el numero de veces que aparece una letra


# print('{} + {} = {}'.format(2, 3, 2+3)) # se puede usar el formato de cadenas para mostrar variables
# print('{} + {} = {}'.format('hola', 'mundo', 'hola mundo')) 
# print('{:.3f} + {:.4f} = {}'.format(2, 3, 2+3)) # se puede especificar el numero de decimales
# print('{1} + {0} = {2}'.format(2, 3, 2+3)) # se puede usar el formato de cadenas para mostrar variables en un orden diferente
# print('{2} + {0} = {1}'.format('hola', 'mundo', 'hola mundo')) # se puede usar el formato de cadenas para mostrar variables en un orden diferente
# print('{:d} + {:b} = {:o} = {:x}'.format(15, 15, 15, 15))

