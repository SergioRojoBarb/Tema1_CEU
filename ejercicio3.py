'''
Ejercicio 3
Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, 
pero no debe repetirse ningún elemento en la nueva lista:

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
'''
# Sacar los elementos de una lista en una tercera, sacar los de la 2 en esa, 
# hacer condicionales if dos o delete elem lista 1

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

lista_3 = []

for letra in lista_1:
    if letra in lista_2 and letra not in lista_3:
        lista_3.append(letra)
print(lista_3)

'''
#Borrador: 
lista_3 = lista_1 + lista_2

def eliminar(letra,letra2):
    lista_solucion = []
    for letra in lista_1:
        for letra2 in lista_2:
            if (letra==letra2):
                print(letra)

    lista_solucion.append(letra)

    return lista_solucion

#print(eliminar(lista_solucion))
'''
