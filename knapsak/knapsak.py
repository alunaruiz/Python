# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 15:58:48 2021
@author: Alexander Luna Ruiz

ENTRADAS:
    - Deben cargarse los archivos de entrada en formato .in
    - La estructura del archivo debe ser la siguiente:
    Ejemplo para la instancia 1: (input1.in):
        
    4
        1  3  2
        2  4  3
        3  5  4
        4  6  5
    5
    
    Donde:
    - la linea 1 contiene la cantidad de artículos a evaluar: (Ej: 4).
    - las lineas siguientes contienen la información de cada artículo en este orden:
      id valor peso: (Ej: 1 3 2).
    - la línea final contiene el peso máximo que soporta la mochila: (Ej: 5).

SALIDA:
    - El programa imprimirá el resultado por pantalla.
    - El programa generará un archivo llamado grasp-knapsak.out en la carpeta 
      de salida que contendrá de igual manera el resultado.
    
"""
import random
import re
import numpy as np


def costo(solution, weight, value, id, capacity):
    max_value = 0
    for j in range(len(solution)):
        if solution[j] == 1:
            max_value += value[j]

    return max_value


def busqueda_local(solution, weight, value, id, capacity):
    temp = solution[:]
    # print(len(value))
    for i in range(len(temp)):
        max_temp_weight = 0
        max_value_temp = 0
        max_value = 0
        if temp[i] == 0:
            temp[i] = 1
            for j in range(len(temp)):
                if temp[j] == 1:
                    max_value_temp += value[id[j]]
                    max_temp_weight += weight[id[j]]
            temp[i] = 0
        elif temp[i] == 1:
            temp[i] = 0
            max_value_temp = 0
            max_value = 0
            for j in range(len(temp)):
                if temp[j] == 1:
                    max_value_temp += value[id[j]]
                    max_temp_weight += weight[id[j]]

            temp[i] = 1
        for j in range(len(solution)):
            if solution[j] == 1:
                max_value += value[id[j]]
        if capacity - max_temp_weight >= 0 and max_value_temp > max_value:
            solution = temp[:]

    return solution


def Greedy_Randomized_Construction(id, value, weight, capacity):
    solucion = []
    item = {}
    for i in range(len(id)):
        item[i] = np.divide(value[i], weight[i]), value[i], weight[i]
    item = sorted(item.values(), reverse=True)

    capacidade_restante = capacity

    peso = 0

    while len(item) > 0:
        lcr = []
        for i in range(2):
            if i < len(item):
                lcr.append(item[i])

        s = random.choice(lcr)
        if s[2] <= capacidade_restante:
            solucion.append(s[1])
            capacidade_restante -= s[2]
            peso += s[2]

        item.pop(item.index(s))

    sol = [0 for i in range(len(value))]

    for item in value:
        if item in solucion:
            sol[value.index(item)] = 1

    return sol, peso


def grasp(max_iterations, id, value, weight, capacity):
    best = 0
    for k in range(max_iterations):
        id_temp = []
        for i in range(len(id)):
            id_temp.append(id[i])
        solution, peso = Greedy_Randomized_Construction(id_temp, value, weight, capacity)

        solution = busqueda_local(solution, weight, value, id, capacity)
        solution = costo(solution, weight, value, id, capacity)
        if solution > best:
            best = solution
    return best


#Función principal -> Permite leer 10 instancias (entradas) diferentes desde archivos .in
#-------------------------------------
#Las entradas deben estar ubicados en la misma ubicación del archivo .py 
#en una carpeta llamada 'entradas'
#-------------------------------------
#La salida la genera tanto por pantalla, como en un archivo de salida .out 
#ubicado en una carpeta llamada 'salida'

def main():
    iterador = 1
    while iterador <= 5:        
        archivo = open("entradas/input" + str(iterador) + ".in", "r")
        iterador += 1
        peso = []
        valor = []
        id = []
        i = 0
        n = int()
        capacidad = int()
        for linea in archivo:
            i += 1
            linea = linea.rstrip()
            numbers = re.findall("[0-9]+", linea)
            if i == 1:
                n = int(numbers[0])
            elif 1 < i <= n + 1:
                id.append(int(numbers[0]) - 1)
                valor.append(int(numbers[1]))
                peso.append(int(numbers[2]))
            else:
                capacidad = int(numbers[0])

        cant_articulos = n
        s = "Valor óptimo instancia " + str(iterador - 1) + " : " + str(grasp(cant_articulos, id, valor, peso, capacidad)) + "\n"
        file = open("salida/grasp-knapsak.out", "a+")
        file.write(s)
        print(s)


if __name__ == "__main__":
    main()