nombre1 = input("Ingresa el nombre de la persona 1: ")
nombre2 = input("Ingresa el nombre de la persona 2: ")
edad1 = int(input('Escoge edad persona 1: '))
edad2 = int(input('Escoge edad persona 2: '))

if edad1 > edad2:
    print(nombre1+' es mayor que '+nombre2)
elif edad1 < edad2:
    print(nombre2+' es mayor que '+nombre1)
else:
    print(nombre1+' y '+nombre2+' Tienen la misma edad')