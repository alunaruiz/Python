import random

def crear_matriz_1(cantidad_filas, cantidad_columnas):
    m = [[0 for _c in range(cantidad_columnas)] for _f in range(cantidad_filas)]
    return m

def crear_matriz_2(cantidad_filas, cantidad_columnas):
    m = [[0 for _c in range(cantidad_columnas)] for _f in range(cantidad_filas)]
    for i in range(cantidad_filas):
        for j in range(cantidad_columnas):
            m[i][j] = random.randint(1,9)
    return m

def transpuesta(matriz,fil,col):
    for i in range(col):
        print("\n")
        for j in range(fil):
            print(matriz[j][i], end="   ")
    print("\n")
    print("\n")
   

f = int(input("Ingrese cantidad de filas: "))
c = int(input("Ingrese cantidad de columnas: "))
matriz_original = crear_matriz_2(f,c)
for i in range(f):
        print("\n")
        for j in range(c):
            print(matriz_original[i][j], end="   ")
print("\n")
print("\n")
transpuesta(matriz_original,f,c)

