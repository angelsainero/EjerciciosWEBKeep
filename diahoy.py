'''
un año es bisiesto si es divisible entre 4 a menos que sea divisible entre 100. Pero si un año
es divisible enetre 1'' u además entre 400, también . 

'''


dias=[31,28,31,30,31,30,31,31,30,31,30,31]
def es_bisiesto(year):
    if year %4 !=0:
        return False
    if year % 100 == 0 and year % 400 != 0:
        return False
    return True
dia=int(input("Dia:"))
mes=int(input("Mes:"))
anyo=int(input("Año:"))

#comprobar bisiesto
#anyo sobreescribe el valor de year
#if es_bisiesto(anyo) == True
if es_bisiesto(anyo):
    dias[1]=29
contador_dias=0
puntero=0
while puntero < mes -1:
    contador_dias=contador_dias+ dias[puntero]
    puntero=puntero+1
#tambien puede escribirse puntero += 1
contador_dias=contador_dias+dia
print(contador_dias)
