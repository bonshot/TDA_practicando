# Sea G un grafo dirigido “camino” (las aristas son de la forma (vi, vi+1)). 
# Cada vertice tiene un valor (positivo).
# Implementar un algoritmo que, utilizando programación dinámica, 
# obtenga el Set Independiente de suma máxima
# dentro de un grafo de dichas características. 
# Indicar y justificar la complejidad del algoritmo implementado.

def max_independent_set(graph):
    n = len(graph)
    if n == 0:
        return []

    # Inicializar una lista para almacenar la suma máxima en cada vértice
    max_sum = [0] * n

    # Inicializar la lista de seguimiento para reconstruir el conjunto independiente
    prev_vertex = [-1] * n

    # Calcular la suma máxima en cada vértice utilizando programación dinámica
    for i in range(n):
        if i == 0:
            max_sum[i] = graph[i]
        elif i == 1:
            max_sum[i] = max(graph[i], max_sum[i - 1])
            if max_sum[i] == graph[i]:
                prev_vertex[i] = i - 1
        else:
            # Elegir el máximo entre incluir el vértice actual o excluirlo
            incl_current = graph[i] + max_sum[i - 2]
            excl_current = max_sum[i - 1]

            if incl_current > excl_current:
                max_sum[i] = incl_current
                prev_vertex[i] = i - 2
            else:
                max_sum[i] = excl_current
                prev_vertex[i] = i - 1

    # Reconstruir el conjunto independiente
    independent_set = []
    i = n - 1
    while i >= 0:
        if i == 0 or i == 1 or prev_vertex[i] == -1:
            independent_set.append(i)
            break
        else:
            independent_set.append(i)
            i = prev_vertex[i]
    result = []
    for i in independent_set:
        result.append(graph[i])
    return result
graph_values = [3, 2, 7, 1, 4]
result = max_independent_set(graph_values)
print("Conjunto Independiente de Suma Máxima:", result)
#La complejidad del algoritmo es O(N) donde n es el largo de nodos en el grafo

#******************************

# Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se
# rompen. Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor
# forma de distribuir los productos en la menor cantidad posible de bolsas. Realizar el seguimiento del algoritmo propuesto
# para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. ¿El algoritmo implementado
# encuentra siempre la solución óptima? Justificar.

def bolsas(W, objetos):
    objetos.sort(reverse=True)
    bolsas = []
    bolsa_actual = []
    for objeto in objetos:
        if sum(bolsa_actual) + objeto <= W:
            bolsa_actual.append(objeto)
        else:
            bolsas.append(bolsa_actual)
            bolsa_actual = [objeto]
    bolsas.append(bolsa_actual)
    return bolsas

# print(bolsas(7, [3,3,2,2,2,2]))
# La complejidad del algoritmo es O(N log N), donde N es el largo de los objetos.
# Porque al ordenar la lista de objetos de mayor a menor,
#  que tiene una logitud N, la complejidad del mismo
# es O(N log N), luego iterar la lista de objetos tiene una complejidad de O(N).
# Por lo tanto, la complejidad del algoritmo es  O(N log N) si la lista se encuentra
# desordenada, En el caso que ya este ordenada, la complejidad mejora a O(N)
# El algoritmo es greedy porque ordenando los objetos de mayor a menor por peso,
# se busca maximizar el peso de la bolsa actual hasta que tenga que agarrar la siguiente bolsa
#hasta llegar a obtener el total de bolsas minimas para guardar todos los objetos
# El algoritmo no es optimo porque para el ejemplo dado, el resultado es
# [3,3], [2,2,2], [2], pero una solucion mas optima seria [3,2,2] y [3,2,2]

#*******************************************************************************
# En el reino de Gondor ha incrementado enormemente la delincuencia luego de su urbanización. El rey Aragorn no
# quiere que todo su esfuerzo en construir calles resulte en vano, por lo que quiere poner guardianes a vigilar las calles por
# las noches. El problema es que cuesta mucho dinero entrenar a dichos guardianes, por lo que quiere reducir al mínimo
# la cantidad que sean necesarios entrenar. Sabe que cada guardian puede estar vigilando desde una esquina, y desde allí
# tener visibilidad hasta cualquier otra esquina directa. Necesita determinar la cantidad mínima de guardianes que son
# necesarios para cubrir todas las calles de su reino. Como primera medida, consulta con el oráculo Alumnus Teorius
# Algoritmus (es decir, quien lee esta consigna), para determinar si esto es conseguible en corto tiempo (el oráculo le
# pregunó algo sobre tiempo polinomial, que Aragorn no entendió y le dijo “si, eso”).
# Tenemos que explicarle a Aragorn que este pedido no es realizable (y debe armarse de paciencia, o no buscar el mínimo
# exacto), porque el problema de Guardianes de Gondor es, en realidad, un problema NP-Completo (en su versión de
# problema de decisión: “¿Se pueden vigilar todas las calles con esta topología con máximo K guardianes?”).


# Para demostrar que el problema de gondor, es NP-Completo, primero que nada
# tenemos que mostrar que el mismo pertenece a NP
# Para eso creamos un certificador en tiempo polinomial, que dado un k que 
# representa a la cantidad de guardianes y una solucion
# verificar que para ese k de guardianes cubren todas las calles de la solucion
# de esta manera, de forma linea, podemos corroborrar si la solucion es valida o no
# De esta manera, el problema es NP

# Ahora para demostrar que el mismo tambien es NP-completo,
# primero creamos una instancia del problema a reducir, que en este caso el que nos sirve
# es el vertex cover.
# Dado una instancia de Vertex cover, un grafo no dirigido = (V,E) y un k, transforemos una instancia
# equivalente del problema de gondor
#     Cada vertice en V se convertira en una esquina en el reindo de gondor
#     cada arista en E se convertira en una calle entre las esquinas correspondientes a esos vertices
#         conectados por la arista
#     k se mantedra como el numero maximo de guardianes permitidos
# Se entiende que un conjunto de vertices en VC se traduce directamente en un conjunto de esquinas
# del reino de gondor
# Si existe un conjunto k de vertices que cubra todas las aristas, existe un conjunto k de esquinas
# que cubra todas las calles del reino de gondor
# Se entiende tambien, al reves que al menos un guardian este en cada calle en gondor se traduce
# en la condicion de que al menos un extremo de cada arista en el conjunto de vertices en VC
# De esta manera podemos demostrar que existe un VC de k vertices si y solo si existe una solucion
# del problema de gondor de k guardianes. Podemos decir que el problema de gondor es al menos
# tan dificil como el VC y dado que VC es NP-completo, el problema de gondor tambien pertenece
# a NP-completo
