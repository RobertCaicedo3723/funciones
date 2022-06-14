def palindrome(x):
    pesos= input("¿Cuantos pesos "+ tipo_pesos+ " tienes? ")
    pesos = float(pesos)
    dolares= pesos / valor_dolar
    dolares= round(dolares, 2)
    dolares= str(dolares)
    print("Tienes $"+dolares+" dolares")

def funcion_principal():
    menu= """
    BIenvenidos al conversor de monedas
    1- Pesos colombiano
    2- Pesos argentinos
    3- Pesos Mexicanos
    
    Elija la opción: """

    opcion= int(input(menu))
    if opcion==1:
        convertir("Colombianos",3966)
    elif opcion==2:
        convertir("Argentinos",122.52)
    elif opcion ==3:
        convertir("Mexicanos",20.62)
    else:
        print("No esta esa opcion... ")

if __name__=='__main__':
    funcion_principal()