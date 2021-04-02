# print()    dir()     type()      len()          
print("==================")
def devuelveDato(name):
    print("hola mundo: " + name) 


#Inicia programa
devuelveDato("Jefferson")
devuelveDato("peter")

print("==================")
#poniendo valores por defecto en funcion
#si no quiero mandar el parametro
def devuelveDatoSin(name="No definido"):
    print("hola mundo: " + name) 

devuelveDatoSin()

print("==================")
def suma(n1, n2):
    return n1+n2

print(suma(5,10))
print(suma(244,23))

#funciones lambda
print("==================")
sumalambda = lambda nu1, nu2: nu1+nu2

print(sumalambda(838,7373))