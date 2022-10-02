'''
Ejercicio 2
Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

Guarda en una variable numero_magico el valor 12345679 (sin el 8)
Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
Multiplica el numero_usuario por 9 en sí mismo
Multiplica el numero_magico por el numero_usuario en sí mismo
Finalmente muestra el valor final del numero_magico por pantalla
'''

import random

numero_magico = 12345679

numero_usuario = random.randint(1,9)

print("El numero usuario es igual a: ", numero_usuario)

multiplica_por_nueve = numero_usuario * 9

print("El numero usuario por 9 es igual a: ", multiplica_por_nueve)

valor_final = numero_magico * numero_usuario

print("El valor final de multiplicar el numero magico por el numeo usuario es igual a: ", valor_final)

#No estoy del todo seguro lo que se pide en el ejercicio, es decir si necesitamos multiplicar
# el numero mágico por el numero usuario o si en vez de por este ultimo por el multiplica por nueve, 
# por ello a continuación lo hago también por el multiplica por nueve:

valor_final2 = numero_magico * multiplica_por_nueve

print("El valor final de multiplicar el numero magico por el multiplicado por nueve es igual a: ", valor_final2)
