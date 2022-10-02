''''
Ejercicio 7
Realiza una función llamada agregar_una_vez(lista, el) que reciba una lista y un elemento. 
La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento. 
Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError que debes 
capturar y mostrar este mensaje en su lugar:

Error: Imposible añadir elementos duplicados => [elemento].
Cuando tengas la función intenta añadir los siguiente valores a la lista 10, -2, "Hola" y luego muestra su contenido.

Sugerencia

Puedes utilizar la sintaxis "elemento in lista"

elementos = [1, 5, -2]
'''

elementos = [1, 5, -2]

def agregar_una_vez(lista, el):
    
    if el in lista:

        raise ValueError("ERROR: Imposible añadir elementos duplicados => [{}]".format(el))

    lista.append(el)


try:
    agregar_una_vez(elementos, 10)
    agregar_una_vez(elementos, -2)

except ValueError as c:
    print(c.args[0])

else:
    print("Elementos agregados correctamente")

finally:
    print("Solución: {}".format(elementos))


'''
#Borrador:
def agregar_una_vez (lista, elemento):
    lista = [0,1]
    elemento = 3

    if len(lista) == 0:

        lista.append(elemento)

        print(lista)
    
    else:
        for c in lista:
            if c == elemento:
                print(f"Error: Imposible añadir elementos duplicados => [{elemento}]")
            else:
                lista.append(elemento)

                break
    return(lista)

'''
'''

from calendar import c
import random

lista_random = random.sample(range(6), 6)
print(lista_random)
listaf = []
for i in range(10):
    if lista_random[0] == lista_random[1] or lista_random[2] or lista_random[3] or lista_random[4] or lista_random[5] :
        listaf.append(lista_random[0])

print(listaf)


'''
'''
def agregar_una_vez(lista, el):
    for c in range(9):
        lista = []
        el = random.randint(1,9)
        lista.append(el)
        break
    return lista

    if lista_random[1] == lista_random[0] or lista_random[2] or lista_random[3] or lista_random[4] or lista_random[5] :
        listaf.append(lista_random[1])
    if lista_random[2] == lista_random[0] or lista_random[1] or lista_random[3] or lista_random[4] or lista_random[5] :
        listaf.append(lista_random[2])
    if lista_random[3] == lista_random[0] or lista_random[1] or lista_random[2] or lista_random[4] or lista_random[5] :
        listaf.append(lista_random[3])
    if lista_random[4] == lista_random[0] or lista_random[1] or lista_random[2] or lista_random[3] or lista_random[5] :
        listaf.append(lista_random[4])
    if lista_random[5] == lista_random[0] or lista_random[1] or lista_random[2] or lista_random[3] or lista_random[4] :
        listaf.append(lista_random[5])
'''


    