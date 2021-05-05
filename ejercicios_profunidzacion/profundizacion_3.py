# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica numérica y cadenas
'''
Enunciado:
Realice un programa que determine cual sería el apellido de una persona
si se ingresaran los dos nombres completos de sus padres.
Dicha persona deberá tener los apellidos de ambos padres

- Primero el programa debe consultar el nombre completo del padre_1
- Luego el programa debe consultar el nombre completo del padre_2
- Luego debe consultar el nombre del hijo/a
- Debe extraer los apellidos de los padres
- Luego formar el nombre completo del hijo/a utilizando los apellidos
  de sus padres
  y el nombre ingresado de dicha persona
- Imprimir en pantalla el resultado

NOTA: Para extraer el apellido del nombre completo recomendamos usar
el método "split"
Mostraremos un ejemplo:

direccion_completa = 'Monroe 2716'
calle, altura = direccion_completa.split(' ')

Les dejo por su cuenta a que busquen un poco más acerca de este método
que seguramente utilizarán mucho de acá en adelante.
Les dejamos un link con algunos ejemplos más:
https://www.pythonforbeginners.com/dictionary/python-split

Cualquier duda con el método split pueden consultarla por el campus
'''

print('Jugando con texto')
# Empezar aquí la resolución del ejercicio
print('Ingrese nombre completo padre:') #nombre padre
nombre_completo_1 = str(input())
print('Ingrese nombre completo madre:') #nombre madre
nombre_completo_2 = str(input())
print('Ingrese nombre hijo:') #nombre hijo
nombre_hijo = str(input())
apellido_1, nombre_1 = nombre_completo_1.split(' ')
print('El apellido paterno es:', apellido_1)
apellido_2, nombre_2 = nombre_completo_2.split(' ')
print('El apellido materno es:', apellido_2)
print('El nombre completo del hijo es:', apellido_1, apellido_2, nombre_hijo)
