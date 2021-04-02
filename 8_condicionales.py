age = input ("Insert your age:")


#============== debo hacer el cast xq es string
#If dentro de oto
if int(age) == 33:
    print("esa es tu edad")
else:
    if int(age) < 45:
        print("age es menor")
    else:
        print("age es mayor")

#if con if y caso contrario
if int(age) == 33:
    print("esa es tu edad")
elif int(age) < 45:
    print("age es menor")
else:
    print("age es mayor")

#===============
x = input ("Insert your number:")
if int(x) > 2 and int(x) < 10:
    print("el numero esta dentro de 2 y 10")
else:
    print("No esta dentro de 2 y 10")