def suma(v1, v2):
    return v1+v2

def multiplica(*argumento):
    print(type(argumento))
    return argumento

def suma_n_cantidad_numeros(*argumento): # es lo mismo con args
    resultado = 0
    for dato in argumento:
        resultado = resultado + dato
    return resultado

def suma_args(*args):
    return args

#Envio de N cantidad de argumentos
def suma_kwargs(**kwargs):
    print(type(kwargs)) #Regresa como un diccionario de datos
    #Recuperando datos enviado es:
    recupe = kwargs.get('nombre', 'No hay nada') # Si no existe el valor 'nombre'
    print("recupera valor:%s" %(recupe))
    return kwargs


print(suma(10,20))
print(multiplica(10,20,30,40)) #Estos argumentos los combierte en una tupla
print(suma_n_cantidad_numeros(1,3,4,5,6,7,8,3,1,5,6,6,3))
print(suma_args(10,1,2,343,5,6,7))
print(suma_kwargs(x=2, tipo = False, num = 10.6, nombre = 'Jefferson'))

#
#     *  n Valores (TUPLAS)            args
#
#    **  n Valores (DICCIONARIO)     kwargs 
#
#