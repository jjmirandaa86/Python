course = "Curso"
my_string = "Codigo facilito"

result = '{} de {}'.format(course,my_string)
print(result)

#Asigment for method
result = '{a} de {b}'.format(b = course, a = my_string)
print(result)


print(result.lower()) #lower case (Minuscula)
print(result.upper()) #capital letter (Mayuscula)
print(result.title()) #captial letter in each work

print('-----------------')
#Method of find 
pos = result.find('Cur')
print(result)
print(pos)

#count characters repeat in text
count = result.count('o')
print(count)

#replace
new_string = result.replace('o','x')
print(new_string)

#split string in several (Array)
new_string = result.split(' ')
print(new_string)
