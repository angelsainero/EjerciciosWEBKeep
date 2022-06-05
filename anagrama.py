#palabra1=input("escribe una letra")
#palabra2=input("escribe otra letra")

'''
funcion tacha
convierte la palabra en una lista
quita el caracter de la lista 
devuelve la palabra
The join() method takes all items in an iterable and joins them into one string.
A string must be specified as the separator.
'''
def tacha (caracter, palabra):
    lpalabra=list(palabra)
    lpalabra.remove(caracter)
    return "".join(lpalabra)


'''
Creamos la funcion es_anagrama que lo que hacer es recorrer la palabra
   For cada letra in p1
       if letra esta en p2
           <tacha (letra, p2)> "Para cada letra de p1 la eliminamos en p2"
       else
           return false

'''
def es_anagrama (p1,p2):
    for letra in  p1:
        if letra in p2:
            p2=tacha(letra, p2)
        else:
            return False
    return p2==""   

print(es_anagrama("palabra1","palabr1a"))