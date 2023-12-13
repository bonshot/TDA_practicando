from grafo import Grafo

g = Grafo([1,2,3,4], [
    (1, 2, 10),
    (2, 3, 5),
    (1, 3, 2),
    (3, 4, 6), 
])

def copiar_grafo(g):
    return Grafo(g.nodos, g.aristas())

def obtener_inicio(g):
    grados_de_entrada = dict()
    nodos = set()
    for s,d,w in g.aristas():
        nodos.add(s)
        nodos.add(w)
        grados_de_entrada[d] = grados_de_entrada.get(d, 0) + 1
    
    for nodo in nodos:
        if grados_de_entrada.get(nodo, 0) == 0:
            return nodo
        

def obtener_fin(g):
    for nodo in g.nodos:
        if len(g.adyacentes(nodo)) == 0:
            return nodo

def camino(g, inicio, fin):
    cola = [inicio]
    visitados = set()
    visitados.add(inicio)
    nodos_previos = dict()
    hay_camino = False
    
    while len(cola) > 0:
        nodo = cola.pop(0)
        
        print(nodo)

        if nodo == fin:
            hay_camino = True
            break

        for ady,w in g.adyacentes(nodo):
            if ady in visitados:
                continue
            print(f"{nodo} -> {ady}")
            nodos_previos[ady] = nodo
            visitados.add(ady)
            cola.append(ady)

    if not hay_camino:
        return None

    print(nodos_previos)

    camino = [nodo]
    anterior = nodos_previos[nodo]

    while anterior:
        camino.append(anterior)
        anterior = nodos_previos.get(anterior)
    
    camino.reverse()
    return camino
    


def flujo_maximo(g):
    residual = copiar_grafo(g)
    inicio = obtener_inicio(g)
    fin = obtener_fin(g)

    print(camino(residual, inicio, fin))

flujo_maximo(g)