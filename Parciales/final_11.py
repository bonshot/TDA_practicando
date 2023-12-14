# 1. Implementar un algoritmo que, por backtracking, obtenga todos los posibles ordenamientos topológicos de un grafo
# dirigido y acíclico.
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

# 3. Dada una soga de n metros (n ≥ 2) implementar un algoritmo que, utilizando programación dinámica, permita cortarla
# (en partes de largo entero) de manera tal que el producto del largo de cada una de las partes resultantes sea máximo. El
# algoritmo debe devolver el valor del producto máximo alcanzable. Indicar y justificar la complejidad del algoritmo.
# Ejemplos:
# n = 2 --> Debe devolver 1 (producto máximo es 1 * 1)
# n = 3 --> Debe devolver 2 (producto máximo es 2 * 1)
# n = 5 --> Debe devolver 6 (producto máximo es 2 * 3)
# n = 10 -> Debe devolver 36 (producto máximo es 3 * 3 * 4)

cortes = dict()


def calcular_cortes(n):
    if cortes.get(n) != None:
        return cortes[n]

    m = 0
    for i in range(1, n):
        valor = i * calcular_cortes(n - i)
        if valor > m:
            m = valor
    
    if n > m:
        m = n
    
    cortes[n] = m

    return m

print(calcular_cortes(10))
print(calcular_cortes(11))

# 4. Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos.
# Implementar un algoritmo que Greedy que dé la cantidad mínima de faros que se necesitan para que todos los
# submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las
# diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”). Indicar y justificar la complejidad
# del algoritmo implementado. ¿El algoritmo implementado da siempre la solución óptima?
#El algoritmo no es optimo porque pueden haber mejores ubicaciones para ubicar los faros y asi
#poner menos faros que la solucion dada por el algoritmo