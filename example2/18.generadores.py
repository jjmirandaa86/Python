# serven para crear objetos sin meterles
# en la memoria

def return_valores():
    print("hola mundo 1")
    return True

def generador(*args): #los genereadores simpre llevan el yield
    for valor in args:
        yield valor * 10, True #tomar el valor y regresarlo // en vez de colocar return

print(return_valores())

for valor1, valor2 in generador(1,2,3,4,5,6,7,8,9):
    print(valor1, valor2)