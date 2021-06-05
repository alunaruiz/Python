#Algoritmo de Aproximación de soluciones para
#calcular la raíz cuadrada de un número
objetivo = int(input('Escoge un entero: '))
#Entre más pequeño epsilon, se tartará mas el resultado
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontró la raíz cuadrada de {objetivo}')
else:
    print(f'La raíz cuadrada de {objetivo} es {respuesta}')


