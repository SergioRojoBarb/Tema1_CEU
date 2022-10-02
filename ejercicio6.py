'''
Ejercicio 6
Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas. 
La primera con los números pares y la segunda con los números impares.

Por ejemplo:

pares, impares = separar([6,5,2,1,7])

print(pares) #%2 = 0

print(impares)

[2, 6]

[1, 5, 7]

Sugerencia

Para ordenar una lista automáticamente puedes utilizar el método .sort().
'''

num = [2, 35, 40, 23, 91, 7, 64]

def orden (lista_num):

    impares = []

    pares = []

    num.sort()
    print(num)
    for c in num:

        if c%2==0:
            pares.append(c)

        else:
            impares.append(c)

    return impares, pares


impares, pares = orden([6,5,2,1,7])

print("Los números pares son: ", pares)

print("Los números impares son: ", impares)
    

'''
#Borrador:
import random

for c in range:
    lista1 = []
    listar = lista1.append(random.randint(1,9))
    break

print(listar)

def separar(lista):
    for lista in lista1:
        'con el %2=0 para pares!!'
'''

