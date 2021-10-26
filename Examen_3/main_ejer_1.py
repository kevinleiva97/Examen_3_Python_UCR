from Clases.Ejer_1 import *

"""Menu principal"""

m1 = "n"
while m1.lower() != "s":
    opcion = str(input(
        "Que desea realizar?:  \n 1. Abrir una caja de Ahorro \n 2. Crear un nuevo plazo fijo \n"))
    print("---" * 40)

    if opcion == "1":
        i = "s"
        while i != "n":
            nombre = str(input("Ingrese el nombre del titular de la cuenta: "))
            cantidad = str(
                input("Ingrese la cantidad disponible en la cuenta: "))

            cliente = Caja_Ahorro()
            cliente.titular = nombre
            cliente.cantidad = cantidad
            imp = str(input("\n Desea imprimir los datos?:  "))
            if imp.lower() == "s":
                print("\n", cliente)
            i = str(input("\n \t Desea agregar un nuevo cliente? s/n:   \n"))
            if i.lower() != "s" and i.lower() != "n":
                print("Favor digitar 'S': para salir 'N': para continuar")
            elif i.lower() == "n":
                print("\n Saliendo del menu")

    if opcion == "2":
        i = "s"
        while i != "n":
            nombre = str(
                input("Ingrese el nombre del titular de la cuenta: \n"))
            cantidad = str(
                input("Ingrese la cantidad disponible en la cuenta: \n"))
            plazo = int(input("Ingrese el plazo en meses:... \n"))
            interes = float(input("Ingrese la cantidad de intereses?:   \n"))
            cliente = Plazo_Fijo()
            cliente.titular = nombre
            cliente.cantidad = cantidad
            cliente.plazo = plazo
            cliente.interes = interes
            imp = str(input("\n Desea imprimir los datos?:  "))
            if imp.lower() == "s":
                print("\n", cliente)
            i = str(input("Desea agregar un nuevo cliente? s/n:   \n"))
            if i.lower() != "s" and i.lower() != "n":
                print("Favor digitar 'S': para salir 'N': para continuar")
            elif i.lower() == "n":
                print("\n Saliendo del menu")
    m1 = input("\n desea salir de la aplicacion? S/N   .... ")
    if m1.lower() != "s" and m1.lower() != "n":
        print("Favor digitar 'S': para salir 'N': para continuar")
    elif m1.lower() == "s":
        print("Saliendo de la aplicacion ...")
