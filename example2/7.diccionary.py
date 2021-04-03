#Save Date
#No rigue indice, no puedo modificar

diccionary = {'a':55, 
              'b':80, 
               5:"Asigno un string", 
               (1,2): False,
               'a':20}
#(1,2) es una tupla
#toma el ultimo dato de la variable agregado 
#por eso no se muestra a=55

print(diccionary)

#agregando otro dato al diccionario / si existe la modifica
diccionary['c'] = "Hola"
print(diccionary)

#Modificar si existe / si no crea una nueva
diccionary['b'] = "nuevo valor"
print(diccionary)

#busca
valor = diccionary['a']
print(valor)

#busca con condiciones si existe o no
valor = diccionary.get('z', False)
print(valor)
valor = diccionary.get(5, False)
print(valor)

#Eliminar
del diccionary['c']
print(diccionary)

#------------
#guarda solo el nombre de las variables agregadas
llave = diccionary.keys()
print(llave)

#Conviertiendo a una lista
llave = list(diccionary.keys())
print(llave)


#------------
#guarda solo el valor de variables
llave = diccionary.values()
print(llave)

#Conviertiendo a una lista []
llave = list(diccionary.values())
print(llave)

#Conviertiendo a una TUPLA ()
llave = tuple(diccionary.values())
print(llave)

#crezca diccionario con otro.
diccionary_2 = {'d': 56, 'e': 10}

diccionary.update(diccionary_2)
print(diccionary)
