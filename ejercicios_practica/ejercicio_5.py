# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
# De la segunda palabra tome las primeras dos letras, utilice el operador :
# Formar una nueva palabra con los recortes solicitados
# Imprima en pantalla los resultados
operador_1 = palabra_1 [:3]
operador_2 = palabra_2 [:2]
nueva_palabra = operador_1 + operador_2
print("El recorte de las dos palabras es",nueva_palabra) # metodo 1
print ("El recorte de las dos palabras es", operador_1 + operador_2) #metodo 2