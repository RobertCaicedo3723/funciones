# Ecuaciones de segundo grado con funciones
import math

def halllar_discriminante(a1, b1, c1):
    d= math.sqrt(b1*b1 - 4*a*c)
    return d

a= float(input("Coeficiente de x²: "))
b= float(input("Coeficiente de x: "))
c= float(input("Termino independiente: "))

d1= halllar_discriminante(a,b,c)

x1= (-b + d1)/2*a
x2= (-b - d1)/2*a

print("Primera raíz:,",x1)
print("Segunda raíz:,",x2)
