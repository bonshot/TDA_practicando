# 2. Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah decidió que en una
# misma parada de colectivo nunca pararán dos colectivos que usen el mismo color. El problema es que ya saben que eso
# está sucediendo hoy en día, así que van a repintar todas las líneas de colectivos. Por problemas presupuestarios, sólo
# pueden pintar los colectivos de k colores diferentes (por ejemplo, k = 4, pero podría se otro valor). Como no quieren
# parecer un grupo de improvisados que malgasta los fondos públicos, quieren hacer un análisis para saber si es posible
# cumplir con lo pedido (pintar cada línea con alguno de los k colores, de tal forma que no hayan dos de mismo color
# coincidiendo en la misma parada). Considerando que se tiene la información de todas las paradas de colectivo y qué
# líneas paran allí, modelar el problema utilizando grafos e implementar un algoritmo que determine si es posible resolver
# el problema. Indicar la complejidad del algoritmo implementado.
def hay_conflictos(grafo, coloreados, v):
    for w in grafo.adyacentes(v):
        if coloreados[w] == coloreados[v]:
            return True
    return False

def k_colectivos(grafo, k, vertices, coloreados):
    if len(vertices) == 0:
        return True
    v = vertices.pop(0)
    for color in range(k):
        coloreados[v] = color
        if not hay_conflictos(grafo, coloreados, v):
            if k_colectivos(grafo, k, vertices, coloreados):
                return True
        coloreados[v] = None
    vertices.insert(0, v)
    return False

def colectivos(grafo, k):
    vertices = grafo.obtener_vertices()
    coloreados = {}
    return k_colectivos(grafo, k, vertices, coloreados)

#La funcion hay_conflicos tiene complejidad O(grado(v)), donde grdo(v) es el grado del vertice en el grafo,
#ya que recorre los vecinos del vertice v
#la complejidad de k-colectivos, que utiliza un enfoque de backtracking y realiza un bucle sobre los colores posibles
# k. En cada iteracion, se realiza la llamada recursiva a la funcion. En el peor de los casos
# la complejidad es exponencial, siendo (K**n), donde n es el numero de vertices en el grafo

#***************************************************************************************

# 3. Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados,
# utilizando programación dinámica. Indicar y justificar el orden del algoritmo implementado.
# Aclaración: siempre es posible escribir a n como suma de n términos de la forma 1**2, por lo que siempre existe solución.

# Sin embargo, la expresión 10 = 3**2 + 1**2

# es una manera más económica de escribirlo para n = 10, pues sólo tiene dos
# términos. Además, tener en cuenta que no se piden los términos, sino la cantidad mínima de términos cuadráticos
# necesaria.
# def cuadrados(n):
#     cant = ["inf"]*(n+1)
#     cant[0] = 0
#     sist = [x**2 for x in range(1,n)]
#     for i in range(1, n+1):
#         minimo = i
#         for cuadrado in sist:
#             if cuadrado > i:
#                 continue
#             cantidad = 1 + cant[i-cuadrado]
#             if cantidad < minimo:
#                 minimo = cantidad
#         cant[i] = minimo
#     return cant[n]
# print(cuadrados(10))
# 4. Realizar una reducción polinomial del problema del ejercicio 3 a otro de los vistos durante la cursada. Ayuda: pensar en
# alguno de los vistos de programación dinámica.
# este problema se asemeja al problema del cambio que ya sabemos que es Np-completo, 
# Nosotros queremos ahora reducir este problema al problema del cambio y para eso tenemos que crear una instancia equivalente al problema del cambio
#Definición del Problema de Cuadrados:

# Dado un número entero n, el problema es encontrar la cantidad mínima de cuadrados perfectos (números de la forma x**2) necesarios para representar 
# n como la suma de cuadrados perfectos.
# Definición del Problema del Cambio (Monedas):
# Dado un conjunto de denominaciones de monedas (cuadrados perfectos) y una cantidad objetivo 
# n, el problema del cambio consiste en encontrar la cantidad mínima de monedas necesarias para alcanzar n.
# Construcción de la Instancia del Problema de Cambio:
# Utilizamos el conjunto de cuadrados perfectos menor o igual a n como denominaciones de monedas.
# Mapeo de Términos Cuadráticos a Monedas:
# Cada cuadrado perfecto en la instancia original se considera como una denominación de moneda en el problema de cambio.
# Relación entre Soluciones:
# La solución al problema de cambio (encontrar la cantidad mínima de monedas para alcanzar 
# n) es directamente equivalente a la solución al problema original de suma de cuadrados (encontrar la cantidad mínima de cuadrados perfectos para representar n).
#     Si podemos resolver el Problema de Cambio, podemos resolver el Problema de Cuadrados:
#         Dada una solución eficiente al problema de cambio, podemos determinar la cantidad mínima de cuadrados perfectos necesarios para representar n.
#         Cada moneda en el problema de cambio representa un cuadrado perfecto y la cantidad de monedas necesarias es la cantidad mínima de cuadrados perfectos para representar n.
#     Si podemos resolver el Problema de Cuadrados, podemos resolver el Problema de Cambio:
#         Dada una solución eficiente al problema de cuadrados, podemos utilizar esos cuadrados perfectos como denominaciones de monedas.
#         Resolver el problema de cambio con estas denominaciones nos dará la cantidad mínima de monedas (cuadrados perfectos) necesarias para alcanzar n.
# La complejidad de la resolución del problema de cambio determina la eficiencia de la resolución del problema original de suma de cuadrados después de la reducción.
# La reducción no introduce una complejidad adicional; simplemente utiliza la estructura del problema de cambio para resolver el problema original de suma de cuadrados 
# de manera eficiente.


# 5. Dado un flujo máximo de un grafo, implementar un algoritmo que, si se le aumenta la capacidad a una artista, permita
# obtener el nuevo flujo máximo en tiempo lineal en vértices y aristas. Indicar y justificar la complejidad del algoritmo
# implementado.