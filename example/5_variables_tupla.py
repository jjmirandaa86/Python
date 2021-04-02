#==== Tuplas ======
#No van a cambiar / son mas rapidas que las listas

x = (1,2,3)
print(x)
print(type(x))

print(dir(x))
meses = ('Ene', 'Feb', "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic")
print(meses)
print(meses[2]) # muestro indice 2

# No puedo agregar, cambiar y/o remover

# hacer una tupla funcional X | Y | ubicacion
locacions = {
    (35.47474, 39.7474):"Guayaquil",
    (35.47474, 39.7474):"Quito"
}
print (locacions)