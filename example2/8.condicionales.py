
fruta = 'naranja2'

if fruta == 'naranja':
    print("es naranja")
    print("entro en if")
else:
    print("no es naranja")
    print("entro en else")

mensaje = 'El valor es naranja' if fruta == 'naranja' else 'No es naranja'
print(mensaje)

#--------
print("-----------")
fruta = 'Manzana'
if fruta == 'naranja':
    print("es naranja")
elif fruta == 'Manzana':
    print('es manzana')
elif fruta == 'limon':
    pass # Aca con este pass es para la identacion, la tabulacion
else:
    print("no es ninguna")

# True = 1
# False= 0

if 0:
    print("es true")
else:
    print("es false")

#-------------------
#si hay dato es verdadero y si no hay datos es falso.
#    []  ()  {}  0   ''   None
# Util para saber si una variable tiene o no valor

if None:
    print("es true")
else:
    print("es false")

# None -> permite decir q no tiene valor como decir NULL

#---------------------
valor = 'Hola'
valor2 = 19
# V AND V = V      ||    V OR V = V
if valor or valor2 >20:
    print("es true")
else:
    print("es false")
