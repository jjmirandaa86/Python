

variable = "HoLa MuNdo Jeff, nice, very"

# formas de contatenar
print("nuevo texto, " + variable)
print(f"nuevo texto {variable}")
print("nuevo texto {0}".format(variable))


#Show property of the Variable
print(dir(variable))

#Set Mayus all Text
print("Mayuscula: " + variable.upper())
#Set Minus all Text
print("Minuscula: " + variable.lower())

print("Intercalado: " + variable.swapcase()) 
print("1ra letra mayuscula por palabra: " + variable.capitalize())
print("Reemplazo por:" + variable.replace("HoLa", "Jeffersons")) 

print("Contar caracteres en blanco:")
print(variable.count(' '))

print("Comineza: En el string hay cadena en inicio: ") 
print(variable.startswith("Mundo")) # Falso
print(variable.startswith("HoLa")) # Verdadero

print("Final: En el string hay cadena en final: ") 
print(variable.endswith("MuNdo")) # Verdaderox
print(variable.endswith("HoLa")) # Verdadero

print(variable.split()) # Separa texto por espacios
print(variable.split(",")) # Separa texto por coma
print(variable.split("e")) # Separa texto por e

print(variable.find("e")) # busca la 1era letra
print(len(variable)) # cuenta los caracteres

print(variable.index("e")) # indice de la posicion del caracter

print(variable.isnumeric()) # para saber si es o no numero
print(variable.isalpha()) # para saber si es o no caracter

print(variable[3]) # devuleve el caracter del indice ingresado
print(variable[-1]) # devuleve el caracter del indice ingresado pero desde el final hacia adelante
