
'''
# Cálculo de la jubilación

Incorpora el año actual al programa. Crea un programa que cuente cuantos años faltan para tu jubilación y que te diga el año en que te jubilarás. Algo así

```
¿Cuantos años tienes? 48
¿A qué edad te jubilarás? 67
Te quedan 19 años para jubilarte
Estamos en 2018, te jubilarás en 2037.
```
## Restricciones

1. Convertir las cadenas de entrada en números
2. Obten el año actual como lo haga python (no vale ponerlo como constante en el programa)

'''
import datetime

ahora = datetime.datetime.now()
año = ahora.year

strEdad = input("¿Cuantos años tienes? ")
strJubilacion = input("¿A qué edad quieres jubilarte? ")

edad = int(strEdad)
jubilacion = int(strJubilacion)

faltan = jubilacion - edad
cuando = año + faltan

print("Te quedan {} años para jubilarte".format(faltan))

print("Estamos en {}, te jubilarás en {}".format(año, cuando))
