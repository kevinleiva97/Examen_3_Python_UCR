from Clases.Ejer_2 import *

print("\n", "-"*20, " Bienvenido a la Agenda electronica ", "-"*20, "\n")
m1 = "n"
while m1.lower() != "s":
    opcion = str(input(
        "Que desea realizar?:  \n 1. Añadir un contacto \n 2. Listar los contactos \n 3. Buscar un contacto \n 4. Editar un contacto \n 5. Cerrar Agenda \n"))
    print("---" * 40, "\n")

    if opcion == "1":
        i = "y"
        while i != "n":
            nombre = input("\n Ingrese el nombre del contacto: \n")
            tel = input("\n Ingrese el numero telefonico: \n")
            email = input("\n Ingrese el email \n")
            global nuevo_contacto
            nuevo_contacto = Agenda()
            nuevo_contacto.nombre = nombre
            nuevo_contacto.tel = str(tel)
            nuevo_contacto.email = str(email)

            nuevo_contacto.agregar()

            i = str(input("\n Desea agregar otro contacto S/N? \n"))
    if opcion == "2":
        i = "y"
        while i != "n":
            nuevo_contacto.listar()
            i = str(input("\n Desea volver a listar los contactos S/N? \n"))
    if opcion == "3":
        i = "y"
        while i != "n":
            nuevo_contacto.buscar()
            i = str(input("\n Desea volver a Buscar en sus contactos S/N? \n"))
    if opcion == "4":
        i = "y"
        while i != "n":
            nuevo_contacto.editar()
            i = str(input("\n Desea Editar otro contacto S/N? \n"))
    if opcion == "5":
        m1 = "s"
        print("Saliendo de la aplicacion ...")
