"""
Función de utilidad:
La distancia desde la ciudad actual - última visitada- hacia cada ciudad aún no visitada
"""
def calculaUtilidad(actual,porVisitar,mDistancias):
    utilidades = []
    minU = mDistancias[actual,porVisitar[0]]
    maxU = minU
    for c in porVisitar:
        d = mDistancias[actual,porVisitar[0]]
        utilidades.append(d)
        if d < minU:
            minU = d
        if d > maxU:
            maxU = d
    return utilidades, minU, maxU

"""
Función de construcción de la Restricted Candidate List:
Sólo lo elementos (ciudades) que cumplan con la siguiente condición pueden
ser considerados como candidatas:
    MIN_fu : mínimo valor de utilidad calculado para algún elemento aún sin incorporar a la solución.
    MAX_fu : máximo valor de utilidad calculado para algún elemento aún sin incorporar a la solución.
    ALFA : % del rango para discriminar los elementos candidatos.

    Minimización:
        x | {MIN_fu <= fu(x) <= ALFA*(MAX_fu - MIN_fu) + MIN_fu}
    Maximización:
        x | {MIN_fu + (1-ALFA)*(MAX_fu - MIN_fu)  <= fu(x) <= MAX_fu}
"""
def calculaRCL(utility,porVisitar,minU,maxU,alfa):
    rcl = []
    lb = minU
    ub = alfa*(maxU-minU)+minU
    for i in range(len(utility)):
        if lb <= utility[i] and utility[i] <= ub:
            rcl.append(porVisitar[i])
    return rcl

"""
Implementación operador de búsqueda intercambio entre dos ciudades elegidas aleatoriamente:
    Genera un nuevo circuito en el que se intercambian las ciudades en las posiciones posi y posj.
"""
def opIntercambio2C(circuito, posi, posj):
    newCircuito = circuito.copy()

    aux = newCircuito[posi]
    newCircuito[posi] = newCircuito[posj]
    newCircuito[posj] = aux

    return newCircuito

"""
Cálculo del ahorro obtenido si se realiza la aplicación del operador de búsqueda intercambio entre dos ciudades
elegidas aleatoriamente:

    Partiendo del valor inicial del circuito, al ser intercambiadas dos ciudades en las posiciones i y j, se deben 
    realizar los siguientes cálculos para actualizar el nuevo valor del circuito:

    i < j

    RESTAR (i-1) -> (j) -> (i+1) ... (j-1) -> (j) -> (j+1)
    RESTAR (i-1) -> (j) -> (i+1) ... (j-1) -> (i) -> (j+1)

    SUMAR-RESTAR será el valor retornado por la función
"""
def ahorroOptIntercambio2C(circuito, mDistancias, posi, posj):
    posFinal=len(circuito)-1
    a = posi-1 if posi>0 else posFinal
    b = posi+1 if posi<posFinal else 0
    c = posj-1 if posj>0 else posFinal
    d = posj+1 if posj<posFinal else 0

    if abs(posi-posj)==1:   #intercambio de ciudades en posiciones consecutivas
        suma = (mDistancias[circuito[a],circuito[posj]] + mDistancias[circuito[posi],circuito[d]] + mDistancias[circuito[posj],circuito[posi]])
        resta = (mDistancias[circuito[a],circuito[posi]] + mDistancias[circuito[posj],circuito[d]] + mDistancias[circuito[posi],circuito[posj]])
    elif abs(posi-posj)==posFinal:  #condiciones de frontera
        suma = (mDistancias[circuito[posj],circuito[b]] + mDistancias[circuito[c],circuito[posi]] + mDistancias[circuito[posi],circuito[posj]])
        resta = (mDistancias[circuito[posi],circuito[b]] + mDistancias[circuito[c],circuito[posj]] + mDistancias[circuito[posj],circuito[posi]])
    else:
        suma = (mDistancias[circuito[a],circuito[posj]] + mDistancias[circuito[posi],circuito[d]] + mDistancias[circuito[posj],circuito[b]] + mDistancias[circuito[c],circuito[posi]])
        resta = (mDistancias[circuito[a],circuito[posi]] + mDistancias[circuito[posj],circuito[d]] + mDistancias[circuito[posi],circuito[b]] + mDistancias[circuito[c],circuito[posj]])
    
    return suma-resta

"""
Acá inicia el código del GRASP en sí mismo
"""
import numpy as np

CIUDADES = 50           #Tamaño del TSP a solucionar
MIN_DISTANCIA = 10      #Parámetro para definir el valor mínimo de las distancias entre ciudades
MAX_DISTANCIA = 100     #Parámetro para definir el valor máximo de las distancias entre ciudades   
N_SOLUCIONES = 100      #Número de soluciones generadas
ALFA = 0.3              #Parámetro discriminación candidatos para RCL
menor_distancia = 0

"Usar 0 como argumento para que siempre se genere la misma secuencia de números aleatorios... y poder hacer el debug"
np.random.seed()

"Generación de matriz de distancias entre ciudades"
distancias = np.random.randint(MIN_DISTANCIA, MAX_DISTANCIA,(CIUDADES, CIUDADES))
"Llenar los valores de la diagonal principal con un valor dado (0 en este caso)"
np.fill_diagonal(distancias,0)
"Circuito de ciudades visitadas"

for i in range (N_SOLUCIONES):
    "Fase I - Constructiva"
    "Inicio con selección aleatoria de una ciudad"
    por_visitar = list(range(CIUDADES))
    solActual = [por_visitar.pop(np.random.randint(0,len(por_visitar)))]
    distanciaTotal = 0
    "Adicion ciudades basada en la escogencia en un subconjunto de 'buenas' opciones"
    while len(por_visitar)>0:
        utilidad, minU, maxU, = calculaUtilidad(solActual[-1],por_visitar,distancias)   #Utilidad para ciudades aún no visitadas
        rcl = calculaRCL(utilidad, por_visitar, minU, maxU, ALFA)   #Construye la Restricted Candidate List
        posSiguiente= np.random.randint(0,len(rcl))     #Aleatoriamente escoger una posición de las candidatas restringidas
        ciudadSiguiente = rcl[posSiguiente]     #Id de la ciudad
        distanciaTotal = distanciaTotal + distancias[solActual[-1],ciudadSiguiente]
        solActual.append(ciudadSiguiente)   #Adicionar ciudad al recorrido
        por_visitar.remove(ciudadSiguiente) #Eliminar ciudad de las pendientes
        
    distanciaTotal = distanciaTotal + distancias[solActual[-1],solActual[0]]    #Distancia a recorrer siguiendo este orden
    print ("Iteración ",i," Distancia circuito fase constructiva: ",distanciaTotal)

    if menor_distancia == 0 or menor_distancia > distanciaTotal:
        menor_distancia = distanciaTotal
        mejor_solucion = solActual.copy()
    
    "Fase Búsqueda Local - II"
    "Necesario proponer los operadores de búsqueda para definir las soluciones adyacentes, vecinos y vecindarios."
    "Se usará como operador, el intercambio de dos ciudades seleccionadas aleatoriamente en el circuito."
    "Se empleará una estrategia First Improvement"

    #En solActual se encuentra la solución obtenida en la fase constructiva
    deltaDistancia = -1
    while deltaDistancia < 0: 
        for ii in range(CIUDADES-1):
            for jj in range(ii+1, CIUDADES):
                deltaDistancia = ahorroOptIntercambio2C(solActual, distancias, ii, jj)
                if(deltaDistancia<0):
                    solActual = opIntercambio2C(solActual, ii, jj)
                    distanciaTotal = distanciaTotal + deltaDistancia
                    print("Nueva solución: ", "distancia: ",distanciaTotal)
                    """
                    Es una forma de reiniciar los ciclos para que vuelva a evalar los vecinos partiendo de este 
                    nuevo circuito
                    """
                    ii=0
                    jj=0
                    if menor_distancia>distanciaTotal:
                        menor_distancia = distanciaTotal
                        mejor_solucion = solActual.copy()

print ("MEJOR SOLUCIÓN (1a) ENCONTRADA: ",mejor_solucion, " DISTANCIA: ",menor_distancia)


