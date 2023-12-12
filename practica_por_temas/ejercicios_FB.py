# Contamos con un conjunto de “n” puntos (x,y) en el plano cartesiano. 
# Un par de puntos es el más cercano si la distancia euclidiana entre ellos es menor a la de cualquier otro par. 
# Resuelva el problema mediante un algoritmo naive que nos informe cuales son los 3 pares de puntos más cercanos. 
import math
def distancia_euclideana(punto1, punto2):
    return math.sqrt((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2)

def pares_mas_cercanos_naive(puntos):
    n = len(puntos)
    mejores_pares = []
    mejor_distancia = float('inf')

    for i in range(n - 1):
        for j in range(i + 1, n):
            distancia_actual = distancia_euclideana(puntos[i], puntos[j])
            if distancia_actual < mejor_distancia:
                mejores_pares = [(puntos[i], puntos[j])]
                mejor_distancia = distancia_actual
            elif distancia_actual == mejor_distancia:
                mejores_pares.append((puntos[i], puntos[j]))

    return mejores_pares[:3]
# puntos = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
# print(pares_mas_cercanos_naive(puntos))
#*********************************************************************************************

# Se encuentran en un río 3 caníbales y 3 vegetarianos. En la orilla hay un bote que permite pasar a dos personas atravesarlo. 
# Los 6 quieren cruzar al otro lado. Sin embargo existe un peligro para los vegetarianos: 
# si en algún momento en alguna de las márgenes hay más caníbales que vegetarianos estos los atacarán. 
# Tener en cuenta que el bote tiene que ser manejado por alguien para regresar a la orilla. 
# Determinar si es posible establecer un orden de cruces en el que puedan lograr su objetivo conservando la integridad física. 
# Explicar cómo construir el grafo de estados del problema. Determinar cómo explorarlo para conseguir la respuesta al problema. Brinde, si existe, la respuesta al problema.

def es_seguro(estado):
    # Verifica si en el estado actual hay más caníbales que vegetarianos en alguna orilla
    for margen in estado:
        if margen.count('C') > 0 and margen.count('V') > margen.count('C'):
            return False
    return True

def cruza_river(estado, bote):
    nuevo_estado = [list(margen) for margen in estado]
    for i in range(2):
        if bote[i] == 'B':
            nuevo_estado[0].remove(bote[i])
            nuevo_estado[1].append(bote[i])
        else:
            nuevo_estado[1].remove(bote[i])
            nuevo_estado[0].append(bote[i])
    return tuple(map(tuple, nuevo_estado))

def es_objetivo(estado):
    # Verifica si todos han cruzado al otro lado
    return not estado[0] or all(x == 'C' or x == 'V' for x in estado[0])

def resolver(estado_actual, camino):
    if es_objetivo(estado_actual):
        return camino

    for bote in [('C', 'C'), ('V', 'V'), ('C', 'V'), ('V', 'C'), ('C', ''), ('', 'C'), ('V', ''), ('', 'V'), ('', '')]:
        nuevo_estado = cruza_river(estado_actual, bote)
        if es_seguro(nuevo_estado) and nuevo_estado not in visitados:
            visitados.add(nuevo_estado)
            solucion = resolver(nuevo_estado, camino + [bote])
            if solucion:
                return solucion
            visitados.remove(nuevo_estado)

    return None

#*********************************************************************************************

# Un granjero debe trasladar un lobo, una cabra y una zanahoria a la otra margen de un río. Cuenta con un bote donde solo entra él y un elemento más. 
# El problema es que no puede quedar solo el lobo y la cabra. Dado que la primera se comería a la segunda. De igual manera, tampoco puede dejar solo a la cabra y la zanahoria. 
# La primera no dudaría en comerse a la segunda. ¿Cómo puede hacer para cruzar? Explicar cómo construir el grafo de estados del problema. 
# Determinar cómo explorarlo para conseguir la respuesta al problema. Brinde, si existe, la respuesta al problema.

def es_valido(estado):
    # Verifica si el estado es válido (ningún problema de canibalismo)
    return not (estado['lobo'] and estado['cabra']) or not (estado['cabra'] and estado['zanahoria'])

def es_solucion(estado):
    # Verifica si el estado es una solución (todos los elementos en el lado opuesto)
    return estado['lobo'] == 0 and estado['cabra'] == 0 and estado['zanahoria'] == 0

def generar_siguientes_estados(estado):
    # Genera los siguientes estados posibles desde el estado actual
    movimientos = [
        {'lobo': 0, 'cabra': 1, 'zanahoria': 1},
        {'lobo': 0, 'cabra': 1, 'zanahoria': 0},
        {'lobo': 1, 'cabra': 1, 'zanahoria': 0},
        {'lobo': 1, 'cabra': 0, 'zanahoria': 0},
    ]
    siguientes_estados = []

    for movimiento in movimientos:
        nuevo_estado = {
            'lobo': estado['lobo'] - movimiento['lobo'],
            'cabra': estado['cabra'] - movimiento['cabra'],
            'zanahoria': estado['zanahoria'] - movimiento['zanahoria'],
        }
        nuevo_estado['barco'] = 1 - estado['barco']  # Cambia la posición del barco
        if 0 <= nuevo_estado['lobo'] <= 1 and 0 <= nuevo_estado['cabra'] <= 1 and 0 <= nuevo_estado['zanahoria'] <= 1 and es_valido(nuevo_estado):
            siguientes_estados.append(nuevo_estado)

    return siguientes_estados

def resolver(estado_actual, visitados):
    # Función recursiva que realiza la búsqueda con backtracking
    if es_solucion(estado_actual):
        return [estado_actual]

    visitados.append(estado_actual)
    siguientes_estados = generar_siguientes_estados(estado_actual)

    for siguiente_estado in siguientes_estados:
        if siguiente_estado not in visitados:
            solucion_parcial = resolver(siguiente_estado, visitados)
            if solucion_parcial:
                return [estado_actual] + solucion_parcial

    return None

#*********************************************************************************************

# Contamos con un conjunto de “n” de equipamientos que se deben repartir entre un conjunto de “m” equipos de desarrollo. 
# Cada equipo solicita un subconjunto de ellas. Puede ocurrir que un mismo equipamiento lo soliciten varios equipos o incluso que un equipamiento no lo solicite nadie. 
# Queremos determinar si es posible seleccionar un subconjunto de equipos de desarrollo entregándoles a todos ellos todo lo que soliciten 
# y al mismo tiempo que ninguno de los equipamientos quede sin repartir. Resolver el problema mediante backtracking.

def backtracking_equipos(equipamientos, equipos, asignacion_actual, indice_equipamiento):
    # Verificar si la asignación actual cumple con las condiciones
    if indice_equipamiento == len(equipamientos):
        for equipo in equipos:
            if equipo not in asignacion_actual:
                return False
        return True

    # Caso en el que no asignamos el equipamiento actual a ningún equipo
    if backtracking_equipos(equipamientos, equipos, asignacion_actual, indice_equipamiento + 1):
        return True

    # Caso en el que intentamos asignar el equipamiento actual a cada equipo
    for equipo in equipos:
        if equipo not in asignacion_actual:
            # Intentamos asignar el equipamiento al equipo actual
            asignacion_actual[equipo] = asignacion_actual.get(equipo, []) + [equipamientos[indice_equipamiento]]

            # Llamada recursiva para el siguiente equipamiento
            if backtracking_equipos(equipamientos, equipos, asignacion_actual, indice_equipamiento + 1):
                return True

            # Deshacer la asignación si no lleva a una solución
            asignacion_actual[equipo].remove(equipamientos[indice_equipamiento])

    return False

def resolver_problema(equipamientos, equipos):
    asignacion_actual = {}
    resultado = backtracking_equipos(equipamientos, equipos, asignacion_actual, 0)
    return resultado, asignacion_actual

# Ejemplo de uso
equipamientos = ["A", "B", "C", "D"]
equipos = ["Equipo1", "Equipo2", "Equipo3"]

resultado, asignacion = resolver_problema(equipamientos, equipos)



#*********************************************************************************************

# Se cuenta con “n” servidores especializados en renderización de videos para películas animadas en 3d. 
# Los servidores son exactamente iguales. Además contamos con “m” escenas de películas que se desean procesar. 
# Cada escena tiene una duración determinada. 
# Queremos determinar la asignación de las escenas a los servidores de modo tal de minimizar el tiempo a esperar hasta que la última de las escenas termine de procesarse. 
# Determinar dos metodologías con la que pueda resolver el problema y presente como realizar el proceso.
def backtracking(asignacion_actual, tiempo_actual, servidores, escenas, mejor_asignacion, mejor_tiempo):
    if not escenas:
        if tiempo_actual < mejor_tiempo:
            mejor_asignacion.update(asignacion_actual)
            mejor_tiempo = tiempo_actual
        return mejor_asignacion, mejor_tiempo

    for servidor in servidores:
        escena_actual = escenas.pop(0)
        asignacion_actual[servidor].append(escena_actual)
        tiempo_servidor = sum(asignacion_actual[servidor])
        mejor_asignacion, mejor_tiempo = backtracking(asignacion_actual, max(tiempo_servidor, tiempo_actual), servidores, escenas, mejor_asignacion, mejor_tiempo)
        asignacion_actual[servidor].remove(escena_actual)
        escenas.insert(0, escena_actual)

    return mejor_asignacion, mejor_tiempo

def asignar_escenas(servidores, escenas):
    mejor_asignacion = {servidor: [] for servidor in servidores}
    mejor_tiempo = float('inf')

    asignacion_inicial = {servidor: [] for servidor in servidores}
    return backtracking(asignacion_inicial, 0, servidores, escenas, mejor_asignacion, mejor_tiempo)




#*********************************************************************************************
# En la teoría de gráfos, se conoce como etiquetado de vértices a asignarle a cada vértice una etiqueta diferente. 
# De igual manera se puede realizar un etiquetado de ejes. Generalmente el etiquetado se puede representar mediante un número entero. Existen diferentes etiquetados posibles. 
# Trabajaremos con el “etiquetado elegante” (graceful labeling). Dado un grafo G=(V,E) con m ejes se asignará como etiqueta a cada uno de sus vértices un número entre 0 y m. 
# Se computará para cada eje la diferencia absoluta entre las etiquetas de vértices y esa será su etiqueta. Se espera que los ejes queden etiquetados del 1 al m inclusive 
# (y que obviamente cada una sea única). Construya mediante generar y probar un algoritmo que dado un grafo determine un etiquetado elegante (si es posible).

#*********************************************************************************************

# Un ciclo euleriano en un grafo es un camino que pasa por cada arista una y solo una vez, comenzando por un vértice y finalizando en el mismo. 
# Sea un grafo G=(V,E) se busca generar si es posible un ciclo euleriano. Resolverlo mediante generar y probar. 

#*********************************************************************************************

# Resuelva el problema de las reinas en el tablero de ajedrez mediante backtracking planteado como permutaciones. 
# Brinde el pseudocódigo y determine la cantidad máxima posible de subproblemas a explorar.

#*********************************************************************************************

# En un tablero de ajedrez (una cuadrícula de 8x8) se ubica la pieza llamada “caballo” en la esquina superior izquierda. 
# Un caballo tiene una manera peculiar de moverse por el tablero: Dos casillas en dirección horizontal o vertical y después una casilla más en ángulo recto 
# (formando una forma similar a la letra “L”). El caballo se traslada de la casilla inicial a la final sin tocar las intermedias, dado que las “salta”. 
# Se quiere determinar si es posible, mover esta pieza de forma sucesiva a través de todas las casillas del tablero, 
# pasando una sola vez por cada una de ellas, y terminando en la casilla inicial. Plantear la solución mediante backtracking.
