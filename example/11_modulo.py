#escribir nosostos mismo
#el que descargamos  //  https://pypi.org/
#modulos de Python // https://docs.python.org/3/py-modindex.html

import datetime

print(datetime.date.today())
print(datetime.timedelta(minutes=70))

#es lo mismo de arriba pero ya no uso en las llamadas datetime
#  from datetime import date, timedelta
#  print(date.today())

#importar clase propias
import f_matematicas

print("Suma es:")
f_matematicas.suma(18,19)
print("resta es:")
f_matematicas.resta(18,19)
print("Multiplicación es:")
f_matematicas.multiplica(18,19)
