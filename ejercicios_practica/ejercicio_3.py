# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese su nombre:')
nombre = str(input())
print('Nombre ingresado:', nombre)
print('Ingrese su apellido:')
apellido = str(input())
print('Apellido ingresado:', apellido)
# Imprima su nombre completo
print ("Nombre Completo", nombre + " " + apellido)
# Almacenar su nombre completo en una variable
# nombre_completo = .....
nombre_completo = nombre + apellido

# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)
cantidad_letras = len(nombre_completo)
print ("La cantidad de letras que posee su nombre completo es", cantidad_letras)