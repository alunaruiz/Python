class Nodo(object):
    def __init__(self, dato=None, prox = None):
        self.dato = dato
        self.prox = prox
    def __str__(self):
        return str(self.dato)


v3=Nodo("Bananas")
v2=Nodo("Peras", v3)
v1=Nodo("Manzanas", v2)

def verLista(nodo):
    """ Recorre todos los nodos a través de sus enlaces,
        mostrando sus contenidos. """

    # cicla mientras nodo no es None
    while nodo:
        # muestra el dato
        print(nodo)
        # ahora nodo apunta a nodo.prox
        nodo = nodo.prox

verLista(v1)