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

#borrar elemento por valor
bicis.remove("orbea")

