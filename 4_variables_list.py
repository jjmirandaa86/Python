demo_list = [1, "hola", 5.5, True, [1,2,3]]
colores = ["blanco", "azul", "negro", "rojo"]

number_lis = list ((1,2,3,4))
print(number_lis)

# crear lista en secuencias
r = list (range(-1,100))
print(r)

# que puedo hacer con una lista
print(dir(colores))
print(len(colores)) # cuantos elementos hay
print(colores[2]) # posicion 3

print("azul" in colores) # saber si existe true  o false

# cambiar el valor clclsde las listas
print(colores)
colores[0] = "white"
print(colores)

colores.append("verde") # agrego un elemento
print(colores)

colores.extend(["violeta", "cafe"])# agregando 2 valores a la vez
print(colores)

colores.insert(0, "rojo") # agregar en cierta poscion del arreglo
print(colores)

colores.pop() # elemina el ultimo elemento
print(colores)

colores.remove("azul") # eliminar un valor por el dato
print(colores)

colores.pop(2) # eliminar por un indice
print(colores)

#============Ordenar========
colores.sort()
print(colores)

colores.sort(reverse=True)
print(colores)

print(colores.index("rojo")) # obetener el indice de un valor
print(colores.count("rojo")) # contar cuantas veces existe


colores.clear() # elimina todos los valores
print(colores)

