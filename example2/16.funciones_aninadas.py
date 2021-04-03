#Funcion principal
def division(v1, v2):
    #funcion aninada, si quiero o no le pongo los argumentos, 
    # como esta en la mismas funcion dentro los toma
    # asi mismo puedo tener funciones anidadas y no mandarlas a llamar
    def validacion():
        return v1 > 0 and v2 > 0
    if validacion():
        return v1/v2

print(division(10,10))


#-----------------------
# Closure
# funciones que crean funciones

def functionnueva(n1,n2):
    def validacion():
        return n1 > 0 and n2 > 0
    return validacion # aqui retorno una funcion

nueva = functionnueva(10,4)
print(nueva()) #ya no mando los datos porque al crear la funcion la le envio
