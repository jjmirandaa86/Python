#for

print("----------")
lista = [1,2,3,4,5,6,7,8,9,10]
for valor in lista:
    print(valor)

print("----------")
nuevo_rango = range(10,30) # lo hace desde el 10 al 30
for valor in nuevo_rango:
    print(valor)

print("----------")
nuevo_rango = range(30) #lo hace desde el 0 hasta el 30
for valor in nuevo_rango:
    print(valor)

print("----------")
nuevo_rango = range(10,30,3) #lo hace desde el 10 hasta el 30, pero de 3 en 3
for valor in nuevo_rango:
    print(valor)

#mostrando el valor y el indice del arreglo
indice = 0
print("----------")
for valor in lista:
    print("Valor: %s, Indice: %s" %(valor, indice))
    indice += 1

print("----------")
#Lo mismo de arriba con una funcion
for indice, valor in enumerate(lista):
    print("Valor: %s, Indice: %s" %(valor, indice))

print("----------")
for valor in range(0, len(lista)):
    print("Valor: %s" %(valor))

print("----------")
for valor in 'HOLA MUNDO':
    print(valor)


print("----------")
diccionari = {'a':10, 'b':100, 'c':1000}
for valor in diccionari.items():
    print(valor)
