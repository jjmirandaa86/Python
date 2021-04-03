import sys

from hdbcli import dbapi

connection = dbapi.connect('15.15.1.93', 3200, 'ECSUPERUSER3', 'Inicia...222')

#This statement prints true if the connection is successfully established
print(connection.isconnected())

