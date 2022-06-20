
class coche:
    def __init__(self, marca, modelo):
        self.marca = marca  # el parametro marca y modelo que has pasado en este metodo quiero asignarlo a marca y modelo de self
        self.modelo = modelo
        self.arrancado = False

    def arrancar(self):
        self.arrancado = True
        print("El", self.marca, self.modelo, "Se ha arrancado")

    def parar(self):
        self.arrancado = False
        print("El", self.marca, self.modelo, "Se ha parado")


laguna = coche("Renault", "Laguna")
tesla = coche("Tesla", "model 3")

print(type(laguna))
print(type(tesla))

print(laguna.marca)
print(tesla.modelo)

laguna.arrancar()
tesla.parar()

print(laguna.arrancado)
print(tesla.arrancado)
