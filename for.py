
alumno1 = "susana"
alumno2 = "andres"
casa_alumno ="Susanas's home"

#desglosa el nombre en columna

def desglosa (nombre):
    for caracter in nombre:
        print (caracter)

desglosa ("angel")
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
        