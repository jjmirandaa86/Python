def generador(*args):
    """ Recibe cantidad de numeros y regresa el numero, 
    ademas de regresar valida el numero si es mayor o no a 5"""
    for valor in args:
        yield valor, True if valor > 5 else False

for valor1, valor2 in generador(1,2,43,3,5,6,7):
    print(valor1, valor2)

#para guardas los comentarios de las funciones
nombre = generador.__name__
documentacion = generador.__doc__
print(nombre+" - "+documentacion)