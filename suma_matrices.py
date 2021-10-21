import random

def crear_matriz_2(cantidad_filas, cantidad_columnas):
    m = [[0 for _c in range(cantidad_columnas)] for _f in range(cantidad_filas)]
    for i in range(cantidad_filas):
        for j in range(cantidad_columnas):
            m[i][j] = random.randint(1,9)
    return m

def sumamatriz(fil,col):
    matriz_a = crear_matriz_2(fil,col)
    matriz_b = crear_matriz_2(fil,col)
    for i in range(fil):
        print("\n")
        for j in range(col):
            print(matriz_a[i][j], end="   ")
    print("\n")
    print("\n")
    for i in range(fil):
        print("\n")
        for j in range(col):
            print(matriz_b[i][j], end="   ")
    print("\n")
    print("\n")
    matriz_res = crear_matriz_2(fil,col)
    for i in range(fil):
        for j in range(col):
            matriz_res[i][j] = matriz_a[i][j] + matriz_b[i][j]
    return matriz_res

f = int(input("Ingrese cantidad de filas: "))
c = int(input("Ingrese cantidad de columnas: "))
matriz = sumamatriz(f,c)

for i in range(f):
    print("\n")
    for j in range(c):
        print(matriz[i][j], end="   ")
