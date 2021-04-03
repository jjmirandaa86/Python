#

lista = []
for valor in range(1,101):
    lista.append(valor)
print(lista)

print("---------------")
#es lo mismo de arriba
lista = [valor for valor in range(1,101)]
print(lista)

print("---------------")
#solo los pares
lista = [valor for valor in range(1,101) if valor % 2 == 0]
print(lista)

print("---------------")
# CREANDO TUPLAS
tupla = (valor for valor in range(1,101) if valor % 2 != 0)
print(tupla)
tupla = tuple(valor for valor in range(1,101) if valor % 2 != 0)
print(tupla)

print("---------------")
# CREANDO DICCIONARIO
diccion = {indice:valor for indice, valor in enumerate(lista)}
print(diccion)