##Ejercicio 1
''''
Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. 
Al parecer contiene el nombre de un alumno y la nota de un exámen. 
¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?

Nombre Apellido ha sacado un Nota de nota.

Ayuda

Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]

cadena = "zeréP nauJ,01"
'''
'''
cadena = "zeréP nauJ,01"
operacion=len(cadena)
volteo=cadena[operacion::1]
print(volteo)
'''

cadena = "zeréP nauJ,01"


volteo = cadena [::-1].split(',')
#print(volteo)

solucion = print(volteo[1], 'ha sacado una nota de' , volteo[0])
solucion


'''
#Borrador:

def volteo (cadena):
    solucion = ''
    for i in range(len(cadena)-1, -1, -1):
        solucion += cadena[i]
    return solucion

cadena = ["zeréP nauJ,01"]

print(volteo(cadena))
'''



