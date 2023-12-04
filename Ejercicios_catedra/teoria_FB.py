# N Reinas
# Dado un tablero de ajedrez NxN, ubicar (si es posible) a N reinas de tal
# manera que ninguna pueda comerse con ninguna
def es_compatible(grafo, puestos):
    for v in puestos:
        for w in puestos:
            if v == w:
                continue
            if grafo.hay_arista(v, w):
                return False
    return True

def _ubicacion_BT(grafo, vertices, v_actual, puestos, n):
    if v_actual == len(grafo):
        return False
    if len(grafo) == n:
        return es_compatible(grafo, puestos)
    if not es_compatible(grafo, puestos):
        return False
    puestos.add(vertices[v_actual])
    if _ubicacion_BT(grafo, vertices v_actual +1, puestos, n):
        return True
    puestos.remove(vertices[v_actual])
    return _ubicacion_BT(grafo, vertices, v_actual +1, puestos, n)

#******************************************************************************

# Independent Set
# Quiero guardar en un grafo N elementos. Debo elegir N v´ertices en
# los cuales guardar cada uno. Restricci´on! Queremos ver de ubicar N
# elementos sin que hayan dos adyacentes con elementos

#******************************************************************************

#Independent sent minimo


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
