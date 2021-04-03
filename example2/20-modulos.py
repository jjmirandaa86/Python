#import modulo_calculadora 
# si deseo importar todos los metodos

#from modulo_calculadora import *
# es como la forma de arriba importa todo


from modulo_calculadora import suma
from modulo_calculadora import resta as r1 
#importo solo los metodos q me importan

#from modulo_calculadora import (suma,
#                                resta,
#                                multiplica)
#Importo en una sola linea los metodos q necesite

resultado = r1(1,3)
print(resultado)

resultado = suma(1,3)
print(resultado)
