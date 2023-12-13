grafo = {
    1: 2,
    2: 3,
    3: 4,
    4: 5,
    5: 6,
    6: 7,
    7: 8,
}


def aristas_a_nodos_ordenados(grafo):
    tiene_arista_entrante = set()
    for s,d in grafo.items():
        tiene_arista_entrante.add(d)
    
    nodo_inicial = None
    for nodo in grafo.keys():
        if nodo not in tiene_arista_entrante:
            nodo_inicial = nodo
            break
    
    nodos_ordenados = []

    nodo = nodo_inicial
    while nodo:
        nodos_ordenados.append(nodo)
        nodo = grafo.get(nodo, None)

    soluciones = []
    for i,nodo in enumerate(nodos_ordenados):
        anterior = None
        if i-1 >= 0:
            anterior = nodos_ordenados[i - 1]
        
        if i == 0:
            soluciones.append([nodo])
        elif i == 1:
            if nodo > anterior:
                soluciones.append([nodo])
            else: 
                soluciones.append([anterior])
        else:
            sol_anterior = sum(soluciones[i - 1])

            nueva_sol = list(soluciones[i - 2])
            nueva_sol.append(nodo)
            
            if sum(nueva_sol) > sol_anterior:
                soluciones.append(nueva_sol)

    return soluciones.pop()

        
print(aristas_a_nodos_ordenados(grafo))