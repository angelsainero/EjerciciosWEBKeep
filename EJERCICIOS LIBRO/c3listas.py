invitados=['jose','juan','pepe','matias','andres']
print (f"Hola {invitados[0].title()}, estás invitados a mi fiesta")
print (f"Hola {invitados[1].title()}, estás invitados a mi fiesta")
print (f"Hola {invitados[2].title()}, estás invitados a mi fiesta")
print (f"Hola {invitados[3].title()}, estás invitados a mi fiesta")
print (f"{invitados[3].title()} no puede venir")

invitados[3]="lolo"
print (f"{invitados[3].title()} viene en su lugar ")