ALFABETO = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def cesar(caracter, clave):
    posicion = ALFABETO.index(caracter)  # guarda en "posicion" el numero de posición del caracter que introduzcas   
    nposicion = posicion + clave # guarda en "nposición" en numero de posición anterior y sumale la clave.
    nposicion = nposicion % len(ALFABETO) #esta es para que no casque con la Z
    return ALFABETO[nposicion]

print (cesar("A",1)) #TEST1 
print (cesar("Z",1)) #TEST2 


def cifrar (mensaje,clave):
    resultado = ""
    for caracter in mensaje:
        nuevo_caracter=cesar(caracter, clave)
        resultado += nuevo_caracter
    return resultado

print(cifrar("HOLA",3))
    #KRÑD

#CREANDO CIFRADO DE FRASE 02:36




