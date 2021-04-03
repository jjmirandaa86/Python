def metodo_global():
    #Sin el global es Variable local de la clase
    global valor_global #_______________________________________->>
    valor_global = 'cambio el valor'

def metodo_nuevo():
    print(valor_global+"new")    

#variables glogables frase
valor_global = 'anita lava la tina'

print(valor_global)
metodo_global()
print(valor_global)
metodo_nuevo()

