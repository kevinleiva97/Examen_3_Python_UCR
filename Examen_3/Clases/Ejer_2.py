contactos = {}


class Agenda():
    """
Clase que guardara la informacion de una lista de contactos
"""

    def __init__(self):
        self.nombre = ""
        self.tel = ""
        self.email = ""

    def agregar(self):
        contactos[self.nombre] = self.tel, self.email

    def listar(self):
        for k, v in contactos.items():
            print(
                f"Nombre: {k} Num tel: {v[0]} Email: {v[1]}")

    def buscar(self):
        search = input("Digite el nombre a buscar:   ")
        for k, v in contactos.items():
            if k == search:
                print(f"Nombre: {k} Num tel: {v[0]} Email: {v[1]}")

    def editar(self):
        search = input("Digite el nombre del contacto que quiera editar:   ")
        for k in contactos:
            new_key = k
            if new_key.lower() == search:
                nuevos_tel = input(
                    "Ingrese el numero telefonico: ")
                nuevo_email = input(
                    "Ingrese el nuevo email ")
                contactos[new_key] = nuevos_tel, nuevo_email
