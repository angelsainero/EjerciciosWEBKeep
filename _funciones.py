""" def nombredelafuncion(parametro):
    resutado = ""
    for variable in iterable:
        if variable in "xxxx" """

#SIN PARAMETRO 
def funcion():
    return "hola mundo"
frase=funcion()
print(frase)

#CON PARAMETRO
def resta(a,b):
    return a-b
print(resta(5,3))


def suma(a=3, b=5, c=0):
    return a+b+c
print(suma())

#----------------------------------------------------------------------------------------------------------------
# FUNCIONES EJEMPLO
def voz_alta(texto):
    return texto.upper() + "!!!"

def voz_baja(texto):
    return texto.lower() + "ssssshh"

print(voz_alta("hola"))
print(voz_baja("Adios"))

gritando = voz_alta
susurrando = voz_baja

print(gritando("hola"))
print(susurrando("adiós"))

    # HOLA!!!
    # adiosssssshh
    # HOLA!!!
    # adiósssssshh

#---------------------------------------------------------------------------------------------------------------
# FUNCIONES DE PRIMERA CLASE
# Se pueden asociar a variables 
# Se pueden asociar a estructuras de datos


def voz_alta(texto):
    return texto.upper() + "!!!"

def voz_baja(texto):
    return texto.lower() + "ssssshh"

gritando = voz_alta
susurrando = voz_baja

dialogo=[
    ("hola", gritando), 
    ("porfa no grites", None),
    ("perdona quieres una aspirina ", voz_baja) #aqui en vez de poner la variable pongo la funcion para que se vea que tb funciona
]

# for frase, in dialogo:
#     print(frase[1](frase[0]))

for frase, modo in dialogo:
    if modo==None:
        print(frase)
    else:
        print(modo(frase))

    # HOLA!!!
    # porfa no grites
    # perdona quieres una aspirina ssssshh
