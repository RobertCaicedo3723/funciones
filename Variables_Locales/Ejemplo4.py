"""Se omite el parametro x en el llamado de la funcion ya que ña variable es global"""



def f():
    global x
    x= x+1
    print("Valor de x dentro de f(x)=",x)
    return x

# ALGORITMO PRINCIPAL

x=3 
print("Valor inicial de x=", x)
z= f()
print("Valor de x despues de llamar a f(x)=",x)
"""Salida
Valor inicial de x= 3
valor de x dentro de f(x)= 4
valor de x _summary_despues de llamar a f(x)=4 """