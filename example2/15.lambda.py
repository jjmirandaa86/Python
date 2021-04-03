#LAMBDA permite crear funciones anonimas
#no utilizar ciclo ni condicionales
#siempre regresar algun valor


#funcion original
def suma(v1, v2):
    return v1+v2

#Funcion lambda que reemplaza al metodo suma
valorLambda = lambda v1, v2 : v1+v2

instancia_metodo = suma
valor = instancia_metodo(10,20)
print(valor)
print(valorLambda(10,50))

#--------------- Si no recibe valor sera 10
str_valor = lambda : 10
print(str_valor())