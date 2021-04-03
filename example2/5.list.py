my_list = ["Hola",15,34.5,True]
print(my_list)
my_list.append(6) #Add new records
print(my_list)

my_list.insert(1, "en campo 1") #Add new records in possition definite
print(my_list)
print(my_list[1])

my_list.remove(15) #remove element than it's with data 15 (integer)
print(my_list)

my_list.pop() #remove last element
print(my_list)

my_list2 = [1,5,8,3,1,9,10,4,42,54,121,1]
my_list2.sort() #order asc
print(my_list2)

my_list2.sort(reverse=True) #order desc
print(my_list2)
