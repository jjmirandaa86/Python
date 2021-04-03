#While

variable = 0
while variable < 10:
    variable += 1
    print(variable)
    if variable == 5:
        print("llego al 5")
        continue
    if variable == 8:
        print("llego al 8 y terminara")
        break
else:
    print("termino")