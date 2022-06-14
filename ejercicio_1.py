"""Construir una función que reciba su nombre como párametro y que lo muestre 5 veces en la pantalla."""

#Input

nombre = input("Digite su nombre: ")

def mostrar_nombre(nombre):
    for i in range (5):
        print(nombre)

mostrar_nombre(nombre)