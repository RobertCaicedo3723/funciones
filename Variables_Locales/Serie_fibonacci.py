a= int(input("Ingrese la cantidad de números que quiere ver: "))

def luk(x):
    if x > 1:
        return luk(x-1) + luk(x-2)
    return x
for i in range(a):
    print(luk(i))
