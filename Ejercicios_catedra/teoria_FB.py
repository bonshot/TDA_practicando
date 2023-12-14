# N Reinas
# Dado un tablero de ajedrez NxN, ubicar (si es posible) a N reinas de tal
# manera que ninguna pueda comerse con ninguna
# def es_compatible(grafo, puestos):
#     for v in puestos:
#         for w in puestos:
#             if v == w:
#                 continue
#             if grafo.hay_arista(v, w):
#                 return False
#     return True

# def _ubicacion_BT(grafo, vertices, v_actual, puestos, n):
#     if v_actual == len(grafo):
#         return False
#     if len(grafo) == n:
#         return es_compatible(grafo, puestos)
#     if not es_compatible(grafo, puestos):
#         return False
#     puestos.add(vertices[v_actual])
#     if _ubicacion_BT(grafo, vertices v_actual +1, puestos, n):
#         return True
#     puestos.remove(vertices[v_actual])
#     return _ubicacion_BT(grafo, vertices, v_actual +1, puestos, n)

#*****************************************************************************

#vertex cover k
def is_vertex_cover(graph, cover):
    # Verifica si el conjunto de vértices 'cover' cubre todas las aristas en 'graph'
    for vertex in cover:
        for neighbor in graph[vertex]:
            if neighbor not in cover:
                return False
    return True

def backtrack_vertex_cover(graph, k, cover, start=0):
    # Caso base: si el tamaño del conjunto de vértices es k
    if k == 0:
        if is_vertex_cover(graph, cover):
            print("Vertex Cover:", cover)
        return
    
    # Recorre los vértices del grafo
    for i in range(start, len(graph)):
        # Prueba agregar el vértice actual al conjunto de vértices
        cover.append(i)
        
        # Realiza la llamada recursiva con un vértice menos
        backtrack_vertex_cover(graph, k - 1, cover, i + 1)
        
        # Retrocede: deshace la elección del vértice actual
        cover.pop()
#*****************************************************************************
#Vertex cover minimo
def es_seguro(vertice, vertices_no_cubiertos, grafo):
    for v in vertices_no_cubiertos:
        if vertice in grafo[v]:
            return False
    return True

def backtrack(grafo, vertices_no_cubiertos, vertex_cover_actual, mejor_vertex_cover):
    if not vertices_no_cubiertos:
        if len(vertex_cover_actual) < len(mejor_vertex_cover):
            mejor_vertex_cover.clear()
            mejor_vertex_cover.extend(vertex_cover_actual)
        return

    vertice = vertices_no_cubiertos.pop()
    # No incluir el vértice actual
    backtrack(grafo, vertices_no_cubiertos, vertex_cover_actual, mejor_vertex_cover)

    # Incluir el vértice actual si es seguro
    if es_seguro(vertice, vertices_no_cubiertos, grafo):
        vertex_cover_actual.append(vertice)
        vecinos_cubiertos = set(grafo[vertice])
        vertices_no_cubiertos -= vecinos_cubiertos
        backtrack(grafo, vertices_no_cubiertos, vertex_cover_actual, mejor_vertex_cover)
        vertices_no_cubiertos.add(vertice)
        vertex_cover_actual.pop()

def encontrar_vertex_cover_minimo(grafo):
    mejor_vertex_cover = []
    vertex_cover_actual = []
    vertices_no_cubiertos = set(grafo.keys())
    
    backtrack(grafo, vertices_no_cubiertos, vertex_cover_actual, mejor_vertex_cover)

    return mejor_vertex_cover

def main():
    grafo = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2]
    }

    vertex_cover_minimo = encontrar_vertex_cover_minimo(grafo)

    print("Vértice de cobertura mínimo:", vertex_cover_minimo)

if __name__ == "__main__":
    main()
























#******************************************************************************

# Independent Set
# Quiero guardar en un grafo N elementos. Debo elegir N v´ertices en
# los cuales guardar cada uno. Restricci´on! Queremos ver de ubicar N
# elementos sin que hayan dos adyacentes con elementos

def is_safe(node, current_set, graph):
    for neighbor in graph[node]:
        if neighbor in current_set:
            return False
    return True

def independent_set(graph, current_set, max_set, n):
    if len(current_set) == n:
        max_set.clear()
        max_set.update(current_set)
        return

    for node in graph:
        if node not in current_set and is_safe(node, current_set, graph):
            current_set.add(node)
            independent_set(graph, current_set, max_set, n)
            current_set.remove(node)

def find_independent_set(graph, n):
    max_set = set()
    current_set = set()
    independent_set(graph, current_set, max_set, n)
    return max_set

#******************************************************************************

#Independent sent minimo
def es_seguro(vertice, conjunto_independiente, grafo):
    for vecino in grafo[vertice]:
        if vecino in conjunto_independiente:
            return False
    return True

def backtrack(vertice, grafo, conjunto_independiente_actual, mejor_conjunto):
    if vertice == len(grafo):
        if len(conjunto_independiente_actual) > len(mejor_conjunto):
            mejor_conjunto.clear()
            mejor_conjunto.extend(conjunto_independiente_actual)
        return

    # No incluir el vértice actual
    backtrack(vertice + 1, grafo, conjunto_independiente_actual, mejor_conjunto)

    # Incluir el vértice actual si es seguro
    if es_seguro(vertice, conjunto_independiente_actual, grafo):
        conjunto_independiente_actual.append(vertice)
        backtrack(vertice + 1, grafo, conjunto_independiente_actual, mejor_conjunto)
        conjunto_independiente_actual.pop()

def encontrar_conjunto_independiente_minimo(grafo):
    mejor_conjunto = []
    conjunto_independiente_actual = []
    
    backtrack(0, grafo, conjunto_independiente_actual, mejor_conjunto)

    return mejor_conjunto

def main():
    grafo = {
        0: [1,2],
        1: [0],
        2: [0]
    }

    conjunto_independiente_minimo = encontrar_conjunto_independiente_minimo(grafo)

    print("Conjunto independiente mínimo:", conjunto_independiente_minimo)

if __name__ == "__main__":
    main()









#******************************************************************************

# Camino Hamiltoniano
# Un camino hamiltoniano es un camino de un grafo, que visita todos los
# v´ertices del grafo una sola vez. Si adem´as el ´ultimo v´ertice visitado es
# adyacente al primero, el camino es un ciclo hamiltoniano
def camino_hamiltoniano_dfs(grafo, v, visitados, camino):
    visitados.add(v)
    camino.append(v)
    if len(visitados) == len(grafo):
        return True
    for w in grafo.adyacentes(v):
        if w not in visitados:
            if camino_hamiltoniano_dfs(grafo, w, visitados, camino):
                return True
    visitados.remove(v)
    camino.pop()
    return False

def camino_hamiltoniano(grafo):
    camino = []
    visitados = set()
    for v in grafo:
        if camino_hamiltoniano_dfs(grafo, v, visitados, camino):
            return camino
    return None

#******************************************************************************

# K coloreo
# Dado un grafo y K colores diferentes, ¿es posible pintar los v´ertices de
# tal forma que ning´un par de v´ertices adyacentes tengan el mismo color?
def es_compatible(grafo, colores, v):
    for w in grafo.adyacentes(v):
        if w in colores and colores[v] == colores[w]:
            return False
    return True

def _coloreo_rec(grafo, k, colores, v):
    for color in range(k):
        colores[v] = color
        if not es_compatible(grafo, colores, v):
            continue
        correcto = True
        for w in grafo.adyacentes(v):
            if not _coloreo_rec(grafo, k, colores, w):
                correcto = False
                break
        if correcto:
            return True
        del colores[v]
    return False

def coloreo(grafo, k):
    colores = {}
    return _coloreo_rec(grafo, k, colores, grafo.random_vertex())

#******************************************************************************

# Sudoku
# Se desea encontrar si un tablero de sudoku tiene soluci´on o no.
def sudoku(cant_elem, M):
    cant_elem = sig_pos_a_usar(cant_elem, M)
    if cant_elem >= 9*9: return True
    for num in range(1,10):
        if puedo_poner(num, cant_elem, M):
            M[fila(cant_elem)][columna(cant_elem)] = num
            if sudoku(cant_elem, M): return True
    M[fila(cant_elem)][columna(cant_elem)] = 0
    return False

#******************************************************************************

# Knight-Tour
# Dado una pieza de caballo de ajedrez (knight o caballero) dentro de un
# tablero, determinar los movimientos a hacer para que el caballo logre
# pasar por todos los casilleros una vez
def caballo(paso = 0):
    if completo(): return True
    x, y = obtener_posicion_actual_caballo()
    for fila, col in movimientos_cabalo(x,y):
        if not dentro_de_tablero(fila, col):continue
        if casillero_ya_marcado(fila, col):continue
        mover_a_posicion(fila, col, paso)
        if (caballo(paso+1)):
            return True
        volver_a_posicion(x,y)
    return False

#******************************************************************************

# Materias Compatibles
# Se tiene una lista de materias que deben ser cursadas en el mismo cuatrimestre, 
# cada materia est´a representada con una lista de cursos/horarios posibles a cursar 
# (solo debe elegirse un horario por cada curso).
# Cada materia puede tener varios cursos.
# Implementar un algoritmo de backtracking que devuelva un listado con
# todas las combinaciones posibles que permitan asistir a un curso de cada
# materia sin que se solapen los horarios. Considerar que existe una funci´on
# son compatibles(curso1, curso2) que dados dos cursos devuelve un valor
# booleano que indica si se pueden cursar al mismo tiempo.
def solucion_posible(horarios):
    ultimo = horarios.ver_ultimo()
    for curso in horarios:
        if curso == ultimo:continue
        if not son_compatibles(curso, ultimo):
            return False
    return True

def horarios_posibles(materias, solucion_parcial):
    if len(materias) == 0:
        if solucion_posible(solucion_parcial):
            return [solucion_parcial]
        else:
            return []
    if not solucion_parcial(solucion_parcial):
        return []
    materia_actual = materias.ver_primero()
    materias.borrar_primero()
    soluciones = []
    for curso in materia_actual:
        soluciones.extend(horarios_posibles(materias_restantes, solucion_parcial+[curso]))
    materias.guardar_primero(materia_actual)
    return soluciones

#******************************************************************************

# Sumatoria de dados
# Escribir un algoritmo de tipo Backtracking que reciba una cantidad de
# dados n y una suma s. La funci´on debe devolver todas las tiradas posibles
# de n dados cuya suma es s. Por ejemplo, con n = 2 y s = 7, debe imprimir
# [1, 6] [2, 5] [3, 4] [4, 3] [5, 2] [6, 1].

def lanzar_dados(n, s):
    resultados = []
    tirada_actual = []
    backtrack(n, 0, tirada_actual, s, resultados)
    return resultados

def backtrack(dados_restantes, suma_actual, tirada_actual, s, resultados):
    if dados_restantes == 0:
        if suma_actual == s:
            resultados.append(tirada_actual[:])
        return

    for cara in range(1, 7):
        tirada_actual.append(cara)
        backtrack(dados_restantes - 1, suma_actual + cara, tirada_actual, s, resultados)
        tirada_actual.pop()
#******************************************************************************

# Subset Sum
# Escribir una funci´on que, utilizando backtracking, dada una lista de enteros positivos
#  L y un entero n devuelva todos los subconjuntos de L que
# suman exactamente n.
def subset_sum(L, index, n, solucion_parcial, soluciones):
    if sum(solucion_parcial) == n:
        soluciones.append(solucion_parcial[:])
        return
    if sum(solucion_parcial) >n:
        return
    for i in range(index, len(L)):
        solucion_parcial.append(L[i])
        subset_sum(L, index+1, n,solucion_parcial, soluciones)
        solucion_parcial.pop()
    return
