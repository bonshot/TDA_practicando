grafo = [
    (1,2),
    (2,4),
    (3,4),
    (4,5),
    (1,5),
    (3,6),
    (4,6),
]

def nodos_grado_entrada_0(grafo, solucion_parcial):
    aristas_restantes = set()
    parcial = set(solucion_parcial)
    nodos = set()
    for arista in grafo:
        s, d = arista
        if s not in parcial:
            nodos.add(s)
        if d not in parcial:
            nodos.add(d)

        if s not in parcial and d not in parcial:
            aristas_restantes.add(arista)

    nodos_con_dependencias = set()

    for arista in aristas_restantes:
        s, d = arista
        nodos_con_dependencias.add(d)

    for n in nodos_con_dependencias:
        if n in nodos:
            nodos.remove(n)

    return list(nodos)


def _orden_topologico(grafo, solucion_parcial, soluciones):
    nodos = nodos_grado_entrada_0(grafo, solucion_parcial)

    if len(nodos) == 0:
        soluciones.append(list(solucion_parcial))

    for nodo in nodos:
        solucion_parcial.append(nodo)
        _orden_topologico(grafo, solucion_parcial, soluciones)
        solucion_parcial.remove(nodo)

soluciones = []
_orden_topologico(grafo, [], soluciones)

print(soluciones)