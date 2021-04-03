#factorial de un numero
 
def factorial_numero(numero):
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -= 1
    return factorial

print(factorial_numero(6))


print("----------------")
def suma(v1, v2):
    return (v1 + v2)
print(suma(1,2))


print("----------------")
def division(v1, v2):
    return (v1 / v2)
print(division(v2=2, v1=10))


print("----------------")
def multiplicacion(v1=10, v2=10):
    return (v1 * v2)
print(multiplicacion())
print(multiplicacion(1))
print(multiplicacion(20,20))


print("----------------")
def multiples_Valores():
    return "String", 1, True, 4.5
strin, inte, bol, floa = multiples_Valores()
print(strin)
print(inte)
print(bol)
print(floa)



print("----------------")
def mostar_res(funcion):
    print(funcion(10,9))

mi_var = multiplicacion
mostar_res(mi_var)