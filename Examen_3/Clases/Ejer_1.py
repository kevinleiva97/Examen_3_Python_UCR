

class Cuenta():
    def __init__(self):
        self.titular = ""
        self.cantidad = int
        print("Cuenta Creada")

    def __str__(self):
        return f"El nombre del titular es: {self.titular} con una cantidad de: {self.cantidad}"


class Plazo_Fijo(Cuenta):
    def __init__(self):
        Cuenta.__init__(self)
        self.plazo = int
        self.interes = float
        print("Plazo Fijo creado")

    def Interes(self):
        total = ((int(self.cantidad) * float(self.interes))/100)
        desc = int(self.cantidad) - total
        return desc

    def __str__(self):
        return f"El nombre del titular es: {self.titular}, con una cantidad total de: {self.cantidad}, con un total de intereses de: {self.interes} y un plazo de: {self.plazo} meses, para un total ya descontado de: {self.Interes()} \n "


class Caja_Ahorro(Cuenta):
    def __init__(self):
        Cuenta.__init__(self)
        print("Caja de Ahorro creada")

    def __str__(self):
        return f"El nombre del titular de la Caja de Ahorro es: {self.titular} con una cantidad de: {self.cantidad}"
