#Now we are going to see how it is the String - cuerda

my_string = "Hello Mundo"
print(my_string)
my_string = 'Hello Mundo, "Eduardo" '
print(my_string)
my_string = '''Hello Mundo, "Eduardo" 
                uso de saltos de linea
                con string'''
print(my_string)

my_string = '''Hello Mundo, "Eduardo" \nuso de saltos de linea \ncon string'''
print(my_string)

#showing other forms with variable
course = "Matematicas"
name = "Jeff"
final_message = "New course:"+ course + ", Name:" + name #Opcion 1
print(final_message)
final_message = "New course: %s , Name: %s" %(course, name) #Opcion 2
print(final_message)
final_message = "New course: {} , Name: {}".format(course, name) #Opcion 3
print(final_message)