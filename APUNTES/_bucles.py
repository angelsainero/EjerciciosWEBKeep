
alumno1 = "susana"
alumno2 = "andres"
casa_alumno ="Susanas's home"

#desglosa el nombre en columna

def desglosa (nombre):
    for caracter in nombre:
        print (caracter)

desglosa ("angel\n")

#-------------------------------------------------------------------------------------------------
#saca vocales, forma 1 
def extrae(nombre):
    vocales=""
    for caracter in nombre:
        if caracter == "a" or caracter =="e" or caracter == "i" or caracter =="o" or caracter == "u":
            vocales += caracter 
    print (vocales)

#-------------------------------------------------------------------------------------------------
#saca vocales, formas 2 (agregamos validación mayúsculas)
def extrae1(nombre):
    textosalida=""
    vocalespermitidas=['a','e','i','o','u']
    nombre=nombre.lower()
    for caracter in nombre:
        if caracter in vocalespermitidas:
            textosalida += caracter 
    print (textosalida)

#-----------------------------------------------------------------------------------------------------

        
#---------------------------------------------------------------------------------------------------
#Diccionarios iteracion
print("imprimiento item")
rv={"A":1,"B":2,"C":3,"D":4}
for item in rv:
    print(item)

print("imprimiento valor")
rv={"A":1,"B":2,"C":3,"D":4}
for item in rv.values():
    print(item)

print("imprimiento ambos")
rv={"A":1,"B":2,"C":3,"D":4}
for item in rv.items():
    print(item)

print("imprimiento ambos")
rv={"A":1,"B":2,"C":3,"D":4}
for item, valor in rv.items():
    print(item,valor)

#------------------------------------------------------------------------------------------------------
#WHILE

i = 1
while i <= 3:
    print(i)
    i += 1
print ("programa terminado")



#Asignar elemento de una lista a valor de otra
def nota_numerica (letra):
    letras=['A','B','C','D','E']
    notas=[1,2,3,4,5]
    puntero=0

    while letras[puntero] != letra:
        puntero +=1
    
    return notas[puntero]

#---------------------------------------------------------------------------------------------------------
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    
print("Thank you, everyone. That was a great magic show!")

    # Alice, that was a great trick!
    # I can't wait to see your next trick, Alice.

    # David, that was a great trick!
    # I can't wait to see your next trick, David.

    # Carolina, that was a great trick!
    # I can't wait to see your next trick, Carolina.
     # Thank you, everyone. That was a great magic show!

#-----------------------------------------------------------------------------------------------------------

   

#Usar range()
for value in range (1,6):
    print (value)
    # 1
    # 2
    # 3
    # 4
    # 5

def multi(numero):
    for n in range (1,11):
        print ("{:>2} x {} = {:>2}".format(n, numero, n*numero))
    #  1 x 5 =  5
    #  2 x 5 = 10
    #  3 x 5 = 15
    #  4 x 5 = 20
    #  5 x 5 = 25
    #  6 x 5 = 30
    #  7 x 5 = 35
    #  8 x 5 = 40
    #  9 x 5 = 45
    # 10 x 5 = 50

# Uso de range () para crear lista de numeros
    # Queremos crear una lista que a partir de un range de 1 a 11 cree una lista con su cuadrado

lista=[]
for valor in range(1,11):
    cuadrado=valor**2
    lista.append(cuadrado)

print(lista)
    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]        

