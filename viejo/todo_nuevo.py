#GREEDY
# Tengo un aula donde quiero dar charlas, que cada una tiene un horario
# de inicio y un horario de fin. Quiero dar la mayor cantidad de charlas.

def scheduling(charlas):
    charlas.sort(key=lambda x: x[1])
    print(charlas)
    orden = []
    for horario in charlas:
        if len(orden) == 0 or not hay_interseccion(orden[-1], horario):
            orden.append(horario)
    return orden
def hay_interseccion(anterior, charla_actual):
    if anterior[1] <= charla_actual[0]:
        return False
    return True
# charlas = [(9,10), (9,15), (10,12), (11,12), (17,18), (10,18)]
# print(scheduling(charlas))


# Se tiene un sistema de monetario. Se quiere dar cambio de una determinada cantidad de plata. 
# Implementar un algoritmo que devuelva el
# cambio pedido, usando la m´ınima cantidad de monedas/billetes.
def problema_cambio(cantidad, denominaciones):
    cambio = []
    i = len(denominaciones) -1
    while cantidad > 0 and i >=0:
        while cantidad >= denominaciones[i]:
            cantidad -= denominaciones[i]
            cambio.append(denominaciones[i])
        i -= 1
    return cambio
# cantidad = 74
# denominaciones = [1,2,5,10,50]
# print(problema_cambio(cantidad, denominaciones))

# Ahora tenemos tareas con una duraci´on y un deadline, pero pueden
# hacerse en cualquier momento, siempre que se hagan antes del deadline.
# Para este problema, buscamos minimizar la latencia en el que las tareas
# se ejecuten. Es decir, si definimos que una tarea i empieza en si, entonces
# termina en fi = si + ti, y su latencia es li = fi − di (si fi > di, sino 0).

# Hacemos que los trabajos que se necesiten terminar primero, se hagan primero.
# Esta soluci´on tambi´en es ´optima.
def minimizar_latencia(tareas):
    tareas.sort(key=lambda x: x[1])
    tiempo_actual = 0
    latencia_total = 0
    for tarea in tareas:
        inicio = max(tiempo_actual, tarea[1])
        fin = inicio + tarea[0]
        latencia = max(0, fin - tarea[1])
        latencia_total += latencia
        tiempo_actual = fin
    return latencia_total

# tareas = [(2,5), (1,3), (3,7)]
# print(minimizar_latencia(tareas))

# Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se
# rompen. Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor
# forma de distribuir los productos en la menor cantidad posible de bolsas. Realizar el seguimiento del algoritmo propuesto
# para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. ¿El algoritmo implementado
# encuentra siempre la solución óptima? Justificar.

def bolsas(productos, peso):
    productos.sort(reverse=True)
    bolsas = []
    bolsa_parcial = []
    for i in range(0, len(productos)):
        print(i)
        if sum(bolsa_parcial) + productos[i] <= peso:
            bolsa_parcial.append(productos[i])
        else:
            bolsas.append(bolsa_parcial)
            bolsa_parcial = [productos[i]]
    bolsas.append(bolsa_parcial)
    return bolsas

#PROGRAMACION DINAMICA
# Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. Decidió en este caso robar
# toda una calle en un barrio privado, que tiene la particularidad de ser circular. Gracias a los trabajos de inteligencia
# realizados, sabemos cuánto se puede obtener por robar en cada casa. Podemos enumerar a la primer casa como la casa
# 0, de la cual podríamos obtener g0, la casa a su derecha es la 1, que nos daría g1, y así hasta llegar a la casa n − 1, que
# nos daría gn−1. Como la calle es circular, la casa 0 y la n − 1 son vecinas. El problema con el que cuenta el Lunático
# es que sabe de experiencias anteriores que, si roba en una casa, los vecinos directos se enterarían muy rápido. No le
# daría tiempo a luego intentar robarles a ellos. Es decir, para robar una casa debe prescindir de robarle a sus vecinos
# directos. El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. Dado
# que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema. Implementar un
# algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar, a
# partir de recibir un arreglo de las ganancias obtenibles. Para esto, escribir y describir la ecuación de recurrencia que
# correspondiente. Indicar y justificar la complejidad del algoritmo propuesto.
def juan_el_ladron(casas):
    if len(casas) == 0:
        return []
    if len(casas) == 1:
        return [casas[0]]
    n = len(casas)
    ganancia1 = _juan_el_ladron(0, n-1, casas)
    ganancia2 = _juan_el_ladron(1, n, casas)

    if ganancia1[n-2] > ganancia2[n-1]:
        return ganancia1[n-2]
    return ganancia2[n-1]

def _juan_el_ladron(inicio, fin, casas):
    gan = [0] * len(casas)
    gan[inicio] = casas[inicio]
    gan[inicio+1] = max(casas[inicio], casas[inicio+1])
    for i in range(inicio+2, fin):
        gan[i] = max(casas[i] + gan[i-2], gan[i-1])
    return gan

# print(juan_el_ladron([20,12,5,8,9,2,4]))
# Dada una soga de n metros (n ≥ 2) implementar un algoritmo que, utilizando programación dinámica, permita cortarla
# (en partes de largo entero) de manera tal que el producto del largo de cada una de las partes resultantes sea máximo. El
# algoritmo debe devolver el valor del producto máximo alcanzable. Indicar y justificar la complejidad del algoritmo.
# Ejemplos:
# n = 2 --> Debe devolver 1 (producto máximo es 1 * 1)
# n = 3 --> Debe devolver 2 (producto máximo es 2 * 1)
# n = 5 --> Debe devolver 6 (producto máximo es 2 * 3)
# n = 10 -> Debe devolver 36 (producto máximo es 3 * 3 * 4)

def maximo_producto_corte(n):
    # Casos base
    if n == 1:
        return 1
    if n == 2:
        return 1

    # Inicializar una lista para almacenar las soluciones parciales
    dp = [0] * (n + 1)

    # Calcular las soluciones parciales
    for i in range(2, n + 1):
        max_producto = 0
        for j in range(1, i):
            max_producto = max(max_producto, j * (i - j), j * dp[i - j])
        dp[i] = max_producto

    return dp[n]
# print(maximo_producto_corte(2))


# Dado un número n, mostrar la cantidad más económica (con menos términos) 
# de escribirlo como una suma de cuadrados,
# utilizando programación dinámica. Indicar y justificar el orden del algoritmo implementado.
# Aclaración: siempre es posible escribir a n como suma de n términos de la forma 1**2, 
# por lo que siempre existe solución.

# Sin embargo, la expresión 10 = 3**2 + 1**2

# es una manera más económica de escribirlo para n = 10, pues sólo tiene dos
# términos. Además, tener en cuenta que no se piden los términos, 
# sino la cantidad mínima de términos cuadráticos
# necesaria.

def problema_cambio(n, sistema):
    res = ["INF"] * (n+1)
    res[0] = 0
    for i in range(1 ,n+1):
        minimo = i
        for j in sistema:
            if i>= j:
                minimo = min(i, 1+ res[i-j])
        res[i] = minimo
    return res[n]
# print(problema_cambio(28,[1,4,9,16,25]))


# Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren
# sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en
# un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se
# trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden
# sentarse. Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan
# la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos). Indicar
# y justificar la complejidad del algoritmo.

def bodegon(familias, W):
    n = len(familias)
    res =[[0] * (W + 1) for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            if familias[i-1] > j:
                res[i][j] = res[i-1][j]
            else:
                res[i][j] = max(res[i-1][j], res[i-1][j-familias[i-1]] + familias[i-1])
    return res[n][W]
print(bodegon([1,5,8,12,10,3,4], 15))


# Manejamos un negocio que atiende clientes en Londres y en California.
# Nos interesa cada mes decidir si operar en una u otra ciudad. Los costos
# de operaci´on para cada mes pueden variar y son dados: Li y Ci para
# todo n.
# Naturalmente, si en un mes operamos en una ciudad, y al siguiente en
# una distinta, habr´a un costo fijo M por la mudanza.
# Dados los costos de operaci´on en Londres (L) y California (C), indicar
# la secuencia de las n localizaciones en las que operar durante n meses,
# sabiendo que queremos minimizar los costos de operaci´on. Se puede
# empezar en cualquier ciudad

def minimizar_costos(L,C,M):
    n = len(L)

    # Inicializar la tabla de costos acumulativos mínimos
    dp = [[float('inf')] * 2 for _ in range(n)]
    dp[0][0] = L[0]
    dp[0][1] = C[0]

    # Calcular los costos acumulativos mínimos
    for i in range(1, n):
        # Costo de operar en Londres en el mes actual
        dp[i][0] = min(dp[i-1][0], dp[i-1][1] + M) + L[i]
        # Costo de operar en California en el mes actual
        dp[i][1] = min(dp[i-1][1], dp[i-1][0] + M) + C[i]

    # Determinar la secuencia de localizaciones para minimizar costos
    secuencia = [0] if dp[n-1][0] < dp[n-1][1] else [1]

    for i in range(n-1, 0, -1):
        if secuencia[-1] == 0:
            secuencia.append(0 if dp[i-1][0] <= dp[i-1][1] + M else 1)
        else:
            secuencia.append(1 if dp[i-1][1] <= dp[i-1][0] + M else 0)

    secuencia.reverse()

    return secuencia

# # Ejemplo de uso
# L = [10, 20, 15, 25]
# C = [15, 25, 10, 20]
# M = 5

# resultado = minimizar_costos(L, C, M)

#FUERZA BRUTA Y BACKTRACKING
# Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren
# sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en
# un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se
# trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden
# sentarse. Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan
# la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos). Indicar
# y justificar la complejidad del algoritmo.
# 2. Resolver el problema del ejercicio 1 utilizando Backtracking.

def bodegon_backtracking(familias, W, indice, asignacion_actual, mejor_asignacion):
    if len(familias) == indice:
        if sum(asignacion_actual) > sum(mejor_asignacion):
            mejor_asignacion = asignacion_actual
        return mejor_asignacion
    else:
        if sum(asignacion_actual) + familias[indice] <= W:
            mejor_asignacion = bodegon_backtracking(familias, W, indice + 1, asignacion_actual + [familias[indice]], mejor_asignacion)
        mejor_asignacion = bodegon_backtracking(W, familias, indice + 1, asignacion_actual, mejor_asignacion)
    return mejor_asignacion

# Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah
# decidió que en una misma parada de colectivo nunca pararán dos colectivos que usen el mismo
# color. El problema es que ya saben que eso está sucediendo hoy en día, así que van a repintar
# todas las líneas de colectivos. Por problemas presupuestarios, sólo pueden pintar los colectivos
# de k colores diferentes (por ejemplo, k = 4, pero podría se otro valor). Como no quieren parecer
# un grupo de improvisados que malgasta los fondos públicos, quieren hacer un análisis para saber
# si es posible cumplir con lo pedido (pintar cada línea con alguno de los k colores, de tal forma
# que no hayan dos de mismo color coincidiendo en la misma parada).
# Considerando que se tiene la información de todas las paradas de colectivo y qué líneas paran allí,
# modelar el problema utilizando grafos e implementar un algoritmo que determine si es posible resolver
# el problema.
# Indicar la complejidad del algoritmo implementado. 

def es_compatible(grafo, colores, v):
    for w in grafo.adyacentes(v):
        if w in colores and colores[w] == colores[v]:
            return False
    return True

def _colore_rec(grafo, k, colores,v):
    for color in range(k):
        colores[v] = color
        if not es_compatible(grafo, colores, v):
            continue
        correcto = True
        for w in grafo.adyacentes(v):
            if w in colores:
                continue
            if not _colore_rec(grafo, l, colores, w):
                correcto = False
                break
        if correcto:
            return True
    del colores[v]
    return False

def coloreo(grafo, k):
    colores = {}
    if _coloreo_rec(grafo, k, colores, "Argentina"):
        print(colores)
        return True
    else:
        print(colores)
        return False

# Implementar un algoritmo que, por backtracking, obtenga todos los posibles ordenamientos topológicos de un grafo
# dirigido y acíclico.

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

#Redes de flujo

# Dado un flujo máximo de un grafo, implementar un algoritmo que, si se le aumenta la capacidad a una artista, permita
# obtener el nuevo flujo máximo en tiempo lineal en vértices y aristas. Indicar y justificar la complejidad del algoritmo
# implementado.
def aumentar_capacidad(grafo, u, v, capacidad_aumentada):
    grafo[u][v]['capacidad'] += capacidad_aumentada

def bfs(grafo, fuente, destino, padres):
    visitados = [False] * len(grafo)
    cola = deque()
    cola.append(fuente)
    visitados[fuente] = True

    while cola:
        actual = cola.popleft()

        for vecino, datos in grafo[actual].items():
            if not visitados[vecino] and datos['capacidad'] - datos['flujo'] > 0:
                padres[vecino] = actual
                cola.append(vecino)
                visitados[vecino] = True

    return visitados[destino]

def edmonds_karp(grafo, fuente, destino):
    padres = [-1] * len(grafo)
    flujo_maximo = 0

    while bfs(grafo, fuente, destino, padres):
        camino_minimo = float('inf')
        actual = destino

        while actual != fuente:
            padre = padres[actual]
            capacidad_residual = grafo[padre][actual]['capacidad'] - grafo[padre][actual]['flujo']
            camino_minimo = min(camino_minimo, capacidad_residual)
            actual = padre

        actual = destino
        while actual != fuente:
            padre = padres[actual]
            grafo[padre][actual]['flujo'] += camino_minimo
            grafo[actual][padre]['flujo'] -= camino_minimo
            actual = padre

        flujo_maximo += camino_minimo

    return flujo_maximo