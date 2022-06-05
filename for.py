
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
#multiplica
def multi(numero):
    for n in range (1,11):
        print ("{:>2} x {} = {:>2}".format(n, numero, n*numero))
        
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


