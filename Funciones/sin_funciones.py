print("---------------------------------------------------")
print("----------BUSCAR UN NUMERO EN CONJUNTO-------------")
print("---------------------------------------------------")

#input

b = int(input("Numero a buscar: ")) #Se recibe el dato del usuario

#Procesing

a = [1, 2, 3, 4, 5] # Se almacena una lista de datos
r = False # Se inicia una variable r con un valor Falso

for i in a:
    if i==b:
        print("Lo encontorĂ©  :) ")
        r = True
    if i==False:
        print("No lo encontrĂ© :( ")

#Output

print("\nEso era....")