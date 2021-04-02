#=================== FOR ================================
foods = ["bread", "swetberry", "meat", "egg", "vegtable"]
x=0
for food in foods:
    x = x+1
    if food == "egg":
        break  # si pongo continuo se salta egg y pasa a los siguientes
    print(str(x) + " - " + food)

print("================")
#
for number in range(1,10):
        print(number)

print("================")
#
for st in "HOLA_COMO_ESTAS":
        print(st)


#=================== WHILE ================================
print("========= While ==========")
count = 8
while count <= 10:
    print(count)
    count = count + 1