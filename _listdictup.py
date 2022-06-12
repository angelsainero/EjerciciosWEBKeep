#Acceder por posiciones
bicis=["trek","canondale","specialized","orbea"]
print(bicis[0].title())
# el resultado es: Trek

#-----------------------------------------------------------------------------------------------------
#Usar valoreds individuales de una lista
bicis=["trek","canondale","specialized","orbea"]
message=f"Mi primera bici fue una {bicis[0].title()}"
print(message)
#el resultado es: Mi primera bici fue una Trek

#----------------------------------------------------------------------------------------------------
#Modificar elementos de una lista
bicis=["trek","canondale","specialized","orbea"]
bicis[0]="brompthon"
print(bicis)

#----------------------------------------------------------------------------------------------------
#insertar elementos al final de una lista
bicis.append("motillo")
print(bicis)

#borrar elementos de una lista
del bicis[1]

#insertar elementos en una lista
bicis.append("motillo")
print(bicis)

#borrar elementos  por posicion pero creando variable, se puede agregar la posición en los parentesis de .pop(0,1,2, etc)
popbicis=bicis.pop()
print (bicis)
print (popbicis)

# borrar elemento por valor
bicis.remove("orbea")

#mas ejemplos de listas 
names = ['ron', 'tyler', 'dani']
msg = f"Hello, {names[0].title()}!"
print(msg)


#ordenar una lista permanentemente
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
cars.sort()
print(cars)
    # ['bmw', 'audi', 'toyota', 'subaru']
    # ['subaru', 'toyota', 'audi', 'bmw']
    # ['audi', 'bmw', 'subaru', 'toyota']

#ordenar lista temporalmente
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(cars)
    # ['bmw', 'audi', 'toyota', 'subaru']
    # ['audi', 'bmw', 'subaru', 'toyota']
    # ['bmw', 'audi', 'toyota', 'subaru']

#longitud de una lista
print(len(cars))
    #4

#listas con range() intercala de 2 en 2
even_numbers = list(range(2, 11, 2)) 
print(even_numbers)
    # [2, 4, 6, 8, 10]

#min max y suma de los valores de una lista
lista=list(range(1,11))
print(lista)
a=min(lista)
b=max(lista)
c=sum(lista)
print(a)
print(b)
print(c)
    # 1
    # 10
    # 55

# Partir listas
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

        # Here are the first three players on my team:
        # Charles
        # Martina
        # Michael