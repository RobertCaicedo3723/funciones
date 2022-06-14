print("---------------------------------------------------")
print("----------BUSCAR UN NUMERO EN CONJUNTO-------------")
print("---------------------------------------------------")

#Definición de una función

def buscarDatoEnLista(datoABuscar, lista):
    r = False
    for i in lista:
        if i == datoABuscar:
            r = True
    return r

#Input
dato =int(input("Número a buscar: ")) # Se recibe el numero de datos del usuario

#Procesing
lista = [1, 2, 3, 4, 5] # Se almacena una lista de datos
if buscarDatoEnLista(dato, lista):
    print("Lo encontré :)")
else:
    print("No lo en encontré :(")

#Output
print("\nEso era....")