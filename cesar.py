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

print(cifrar("ABS",-1)) #TEST1 
    #ZAR
print(cifrar("ZAR",1)) #TEST2
    #ABS    

#AHORA EMPEZAMOS CON LAS FUNCIONES DE ORDEN SUPERIOR
'''
CrearCifrador(Clave) --> cifra7
cifra7(m)
'''

def creaEncriptador(clave):
    def encriptar(mensaje):
        res = ""
        for caracter in mensaje:
            nuevo_caracter=cesar(caracter, clave) #caracter pertenece a la de dentro y clave a la de fuera
            res += nuevo_caracter
        return res
    return encriptar

_encrypt=creaEncriptador(5)
_desencrypt=creaEncriptador(-5)

print(_encrypt("HOLA"), cifrar("HOLA", 5))