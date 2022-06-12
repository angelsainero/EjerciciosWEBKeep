def creaContador(ini=0):
    clicks=ini

    def click():
        nonlocal clicks
        clicks = clicks + 1
        return clicks
    
    return click



'''
lo ideal sería hacer un contador reutilizable

c1 <-- creutilizable(valor)
c1 ( meter algún parametro )
    () --> si no meto nada que haga un click (*1)
    (consulta) --> si pongo la palabra consulta que devuelva el valor de clicks (*2)
    (reset, (opcional) ) --> Haga reset y empiece por el parametro opcional (*3)

 '''

def creaContadorReutilizable(ini=0):
    clicks=ini
    
    def contador(**kwargs): #parametros clave valor
        if len(kwargs)==0: #si no has metido nada 

        pass

    return contador

#Un prototipo con PF codigo 1 funciona clic 
minuto 2,34