# Una empresa que realiza ciencia de datos debe realizar en las
# próximas “n” semanas procesos y cálculos intensivos. Para eso debe
# contratar tiempo de cómputo en un data center. Realizando una
# estimación conocen cuantas horas de cómputo necesitarán para cada
# una de las semanas. Por otro lado luego de negociar con los
# principales proveedores tienen 2 opciones que pueden combinar a
# gusto:
# ● Opción 1: Contratar a la empresa “Arganzón” por semana. En
# esa semana se cobra proporcional al tiempo de cómputo según
# un parámetro “r” (horas computo x r).
# ● Opción 2: Contratar a la empresa “Fuddle” por un lapso de 3
# semanas contiguas. Durante el lapso contratado se paga una
# tarifa fija de “c”.
# Proponer una solución utilizando programación dinámica que nos
# indique la secuencia de elecciones a realizar para minimizar el
# costo total de cómputo. Analizar su complejidad temporal y
# espacial.
def empresa(horas, r, c):
    n=len(horas)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + horas[i - 1] * r
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + c)

    return dp[n]
horas = [4, 2, 8, 6, 5]
r = 2
c = 10

# resultado = empresa(horas, r, c)
# print("Costo mínimo:", resultado)

# Se conoce como “Longest increasing subsequences” al problema de
# encontrar la subsecuencia más larga de números (no necesariamente
# consecutivos) donde cada elemento sea mayor a los anteriores en
# una secuencia de números.
# Ejemplo: En la lista → 2, 1, 4, 2, 3, 9, 4, 6, 5, 4, 7. Podemos
# ver que la subsecuencia más larga es de longitud 6 y corresponde a
# la siguiente (marcada en negrita) “2, 1, 4, 2, 3, 9, 4, 6, 5, 4,
# 7”
# Este problema se puede resolver de varias maneras. Entre ellas,
# utilizando programación dinámica. Se pide: resolverlo mediante
# programación dinámica. Usar el ejemplo del enunciado para explicar
# paso a paso el método.
def longest_increasing_subsecuencia(lista):
    lis = [1]*len(lista)
    for i in range(1, len(lista)):
        for j in range(0,i):
            if lista[i] > lista[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    long_max = max(lis)

    sub = []
    for i in range(len(lista) -1 , -1, -1):
        if lis[i] == long_max:
            sub.append(lista[i])
            long_max -= 1
    return sub[::-1]
# print(longest_increasing_subsecuencia([2, 1, 4, 2, 3, 9, 4, 6, 5, 4, 7]))

# Luego de aprender programación dinámica un estudiante en una
# charla de café le explica a un amigo que atiende un negocio el
# algoritmo de cambio mínimo de monedas. Con eso, afirma, podrá
# optimizar el despacho de mercadería. El comerciante despacha
# pedidos de cierto producto que viene en empaques prearmados de
# distintas cantidades o en unidades sueltas. Sin embargo, el amigo
# le replica que su algoritmo es poco realista. Supone que uno tiene
# una cantidad ilimitada de empaques de cada presentación. Luego de
# pensar unos momentos, el estudiante llega a una variante de este
# problema teniendo en cuenta esta restricción. ¿Podría usted
# detallar cuál es esta solución? Describa paso a paso y explique
# con un ejemplo cómo funciona.

def cafeteria(empaques, cant_objetivo):
    dp = [float('inf')] * (cant_objetivo + 1)
    dp[0] = 0
    decisiones = [-1] * (cant_objetivo+1)
    for i in range(1, cant_objetivo + 1):
        for empaque in empaques:
            if i - empaque >= 0:
                dp[i] = min(dp[i], dp[i - empaque] + 1)
    return dp[cant_objetivo]

empaques_disponibles = [1, 3, 12]
cantidad_objetivo = 11
# print(cafeteria(empaques_disponibles, cantidad_objetivo))

# Una empresa multinacional está revisando su lista de
# proveedores. Tienen una lista de “n” productos, materias primas e
# insumos que adquieren todos los meses. Su proceso de compras es
# muy descentralizado y tienen un número actual de “m” proveedores.
# Piensan que pueden bajar los costos si reducen la cantidad de
# proveedores. Saben qué productos ofrece cada proveedor. Las
# diferencias de precios son despreciables, lo que quieren es
# encontrar el conjunto menor posible de proveedores para cubrir
# toda su necesidades de productos. Proponer un algoritmo eficiente
# que aproxime la solución óptima. Explique su funcionamiento.
# Detalle complejidad temporal y que tan diferente a la solución
# óptima puede lograr con su método.

def empresa(provedores, productos):
    provedores.sort(key=lambda x: len(x[1]), reverse=True)
    productos_cubiertos = set()
    provedores_selec = []
    for provedor in provedores:
        productos_no_cubiertos = set(provedor[1]) - productos_cubiertos
        if productos_no_cubiertos:
            provedores_selec.append(provedor)
            productos_cubiertos.update(productos_no_cubiertos)
    return productos_cubiertos, provedores_selec

productos = ["A", "B", "C", "D", "E"]
proveedores = [
    (1, ["A", "B"]),
    (2, ["B", "C"]),
    (3, ["C", "D", "E"]),
]
print(empresa(proveedores, productos))

# Un centro de distribución de repuestos ferroviarios se
# encuentra en un punto de la red de este transporte. Es la
# encargada de distribuir a demanda los materiales y recursos para
# las reparaciones que solicitan las diferentes estaciones. Como la
# red es antigua y está mal mantenida la cantidad de kilos que se
# puede transferir sobre cada trayecto es variable. Esto para ellos
# es un problema porque quieren enviar la mayor cantidad posible de
# material por viaje. Tanto es así que no les importa realizar un
# camino más largo siempre que eso implique transportar más
# materiales.
# Se pueden armar diferentes caminos que unan el centro de
# distribución con cada estación. Estos estarán conformados por una
# secuencia de trayectos, cada uno con su propia limitación de kilos
# que soporta. Llamamos cuello de botella al valor mínimo entre
# ellos.
# Construir un algoritmo greedy que permita calcular el camino con
# el máximo cuello de botella entre el punto de partida y el resto
# de los puntos. ¿Qué complejidad tiene? Demuestre que es óptima su
# solución.

def max_cuello_botonella(trayectos, inicio):
    # trayectos es una lista de tuplas (destino, limite_kilos) que representan los trayectos desde el inicio
    # inicio es el punto de partida (centro de distribución)
    
    cuello_botonella = {}  # Almacena el cuello de botella máximo para cada estación
    
    # Inicialización: asignar infinito como cuello de botella para todas las estaciones excepto el punto de inicio
    for destino, _ in trayectos:
        cuello_botonella[destino] = 0
    
    cuello_botonella[inicio] = float('inf')
    
    for _ in range(len(cuello_botonella)):
        # Seleccionar la estación con el mayor límite de kilos
        estacion_actual = max((estacion for estacion in cuello_botonella if cuello_botonella[estacion] > 0), key=lambda x: cuello_botonella[x])
        
        # Actualizar el cuello de botella para las estaciones vecinas
        for destino, limite_kilos in [(destino, limite_kilos) for destino, limite_kilos in trayectos if destino == estacion_actual]:
            cuello_botonella[destino] = max(cuello_botonella[destino], min(cuello_botonella[estacion_actual], limite_kilos))
    
    return cuello_botonella

# Ejemplo de uso
# trayectos = [('B', 10), ('C', 5), ('B', 8), ('C', 8)]
# inicio = 'A'
# resultado = max_cuello_botonella(trayectos, inicio)
# print(resultado)

# Para satisfacer la producción de un producto electrónico una
# empresa debe comprar un componente a sus diferentes proveedores.
# Cada proveedor tiene una cantidad máxima que puede ofrecer
# mensualmente. Además las diferentes plantas de producción demandan
# una cantidad mensual del mismo. Por cuestiones logísticas algunos
# proveedores no pueden enviar a ciertas plantas de producción. El
# mes próximo por una promoción se va a tener que producir al 100%
# de la capacidad. Determinar en forma eficiente si es posible
# satisfacer esta demanda.
# Explicar detalladamente y paso a paso la solución propuesta. Se
# puede afirmar que para resolver el problema se ha realizado una
# reducción polinomial? ¿Por qué?

# aplicamos ford_fulkerson
# inicializamos el flujo en vacio
# por cada arista en mi grafo, agrego esa arista a mi flujo con peso 0
# realizo una copia de mi grafo, con la que voy a trabajar
# mientras haya camino aumentante desde la fuente al sumidero
#     obtengo el peso minimo del camino
#     recorro el camino
#     si hay camino entre el anterior y el actual
#         aumento el flujo con el min peso del camino
#         actualizo el grafo residual
#     sino
#         disminuyo el flujo del camino con el min peso del camino
#         actualizo el grafo residual
# retorno el flujo final

# Un grupo de científicos han liberado “n” boyas en diferentes
# puntos de los océanos para realizar un estudio sobre las
# corrientes marinas. Cada boya tiene un emisor de posición que
# informa a una computadora central su ubicación cada minuto. Entre
# los estudios que desean realizar se encuentra determinar cuales
# dos boyas se encuentran más cerca entre sí. Ese proceso lo tienen
# que realizar en forma eficiente, ya que se realiza de forma
# constante y solo es uno de los tantos análisis que realizan.
# Utilizando división y conquista proponga una forma de
# solucionarlo. Explique paso a paso su solución y analice su
# complejidad.

import math

def distancia(p1, p2):
    # Función para calcular la distancia euclidiana entre dos puntos
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def distancia_minima_en_franja(franja, d_minima):
    # Función para encontrar la distancia mínima entre boyas en la franja
    for i in range(len(franja)):
        j = i + 1
        while j < len(franja) and (franja[j][1] - franja[i][1]) < d_minima:
            d_minima = min(d_minima, distancia(franja[i], franja[j]))
            j += 1
    return d_minima

def distancia_minima_divide_y_conquista(puntos):
    # Función principal que implementa la estrategia de divide y conquista
    n = len(puntos)

    # Caso base: usar fuerza bruta para conjuntos pequeños
    if n <= 3:
        return min(distancia(puntos[i], puntos[j]) for i in range(n) for j in range(i + 1, n))

    # Ordenar puntos por coordenada x
    puntos_ordenados = sorted(puntos, key=lambda x: x[0])

    # Dividir el conjunto en dos mitades
    mitad = n // 2
    puntos_izquierda = puntos_ordenados[:mitad]
    puntos_derecha = puntos_ordenados[mitad:]

    # Resolver recursivamente para ambas mitades
    d_izquierda = distancia_minima_divide_y_conquista(puntos_izquierda)
    d_derecha = distancia_minima_divide_y_conquista(puntos_derecha)

    # Encontrar la distancia mínima entre ambas mitades
    d_minima = min(d_izquierda, d_derecha)

    # Encontrar puntos en la franja alrededor de la línea de división
    franja = [punto for punto in puntos_ordenados if abs(punto[0] - puntos[mitad][0]) < d_minima]

    # Calcular la distancia mínima en la franja
    return min(d_minima, distancia_minima_en_franja(franja, d_minima))







# Recordemos al problema 2-Partition: Se cuenta con un conjunto de
# “n” elementos. Cada uno de ellos tiene un valor asociado. Se desea
# separar los elementos en 2 conjuntos que cumplan con: La suma de
# los valores de cada conjunto sea igual entre ellos. Se puede ver
# que este corresponde a un problema NP-C. Sin embargo - al igual
# que otros problemas en esta clase como el problema de la mochila -
# puede ser resuelto utilizando programación dinámica.
# Proponga un algoritmo utilizando programación dinámica que
# resuelva cualquier instancia de 2-Partition. Analice su
# complejidad temporal y espacial.

def can_partition(arr):
    total_sum = sum(arr)
    
    # Si la suma total es impar, no es posible una partición
    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    n = len(arr)

    # Inicializar una tabla de memoización para almacenar resultados intermedios
    dp = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]

    # Caso base: La suma de cero siempre es posible
    for i in range(n + 1):
        dp[i][0] = True

    # Llenar la tabla utilizando programación dinámica
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= arr[i - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j - arr[i - 1]]

    # El resultado final estará en la esquina inferior derecha de la tabla
    return dp[n][target_sum]

# Una ciudad tiene una red inalámbrica interna para interconectar
# diferentes servidores de varias instituciones públicas. Existen un
# conjunto "A" de antenas de interconexión que están dispersas por
# la ciudad. Cada una de ellas tiene una localización "x,y", un
# alcance de recepción limitado (un radio "R_a") y una cantidad
# máxima de conexiones que puede tener en forma simultánea. Se
# recopiló una lista "S" de servidores, cada uno de ellos con su
# ubicación "x,y"
# Determinar si es posible que todos los servidores pueden estar
# conectados a una antena respetando las restricciones impuestas.
# Explique paso a paso la solución propuesta y analice su
# complejidad temporal.

# Modelado del Grafo Bipartito:

# Crea un grafo bipartito con un conjunto de nodos para las antenas (A) y otro conjunto para los servidores (S).
# Agrega un borde dirigido desde cada antena a cada servidor si la distancia entre la antena y el servidor es menor o igual al radio de la antena.
# Aumento de Flujo (Ford-Fulkerson):

# Inicializa el flujo en todas las aristas a cero.
# Encuentra un camino aumentante en el grafo residual.
# Actualiza el flujo a lo largo del camino aumentante.
# Repite estos pasos hasta que no haya caminos aumentantes en el grafo residual.
# Verificación de Asignación:

# Después de ejecutar Ford-Fulkerson, verifica si todos los servidores tienen una antena asignada.
# Si todos los servidores están asignados, entonces la asignación es válida.

#******************************************************************************

# El dueño de una cosechadora está teniendo una demanda muy elevada
# en los próximos 3 meses. Desde “n” campos lo quieren contratar
# para que preste sus servicios. Lamentablemente no puede hacer
# todos los contratos puesto que varios de ellos se superponen en
# sus tiempos. Cuenta con un listado de los pedidos donde para cada
# uno de ellos se consigna: fecha de inicio, fecha de finalización,
# monto a ganar por realizarlo. Su idea es seleccionar la mayor
# cantidad de trabajos posibles. Por eso seleccionará primero
# aquellos trabajos que le demanden menos tiempo. Mostrarle que esta
# solución puede no ser la óptima. Proponer una solución utilizando
# programación dinámica que nos otorgue el resultado óptimo.
# Analizar su complejidad temporal y espacial.

def seleccionar_trabajos(trabajos):
    # Ordenar los trabajos por fecha de finalización
    trabajos_ordenados = sorted(trabajos, key=lambda x: x[1])

    # Inicializar una lista para almacenar la ganancia máxima en cada índice
    ganancia_maxima = [0] * len(trabajos_ordenados)

    # Inicializar la ganancia máxima para el primer trabajo
    ganancia_maxima[0] = trabajos_ordenados[0][2]

    # Iterar sobre los trabajos restantes
    for i in range(1, len(trabajos_ordenados)):
        # Encontrar el índice del último trabajo compatible con el trabajo actual
        indice_compatible = encontrar_trabajo_compatible(trabajos_ordenados, i)

        # Calcular la ganancia máxima para el trabajo actual
        ganancia_incluyendo = trabajos_ordenados[i][2] + (ganancia_maxima[indice_compatible] if indice_compatible != -1 else 0)
        ganancia_excluyendo = ganancia_maxima[i - 1]

        # Actualizar la ganancia máxima en el índice actual
        ganancia_maxima[i] = max(ganancia_incluyendo, ganancia_excluyendo)

    # La ganancia máxima estará en el último elemento de la lista
    ganancia_total = ganancia_maxima[-1]

    return ganancia_total

def encontrar_trabajo_compatible(trabajos, indice_actual):
    for i in range(indice_actual - 1, -1, -1):
        if trabajos[i][1] <= trabajos[indice_actual][0]:
            return i
    return -1

# Ejemplo de uso
trabajos = [(1, 3, 50), (2, 5, 60), (4, 7, 80), (6, 9, 100)]
resultado_optimo = seleccionar_trabajos(trabajos)

# Una empresa de autobuses se conformó luego de la fusión de varias
# compañías menores. Actualmente tienen diferentes rutas que cubrir.
# Cada una con horario de inicio en una ciudad y finalización en
# otra. Existe la posibilidad de cubrir con un mismo micro
# diferentes rutas.
# Siempre la ruta comienza desde donde parte el micro, pero también
# puede pasar que el micro tenga tiempo suficiente para trasladarse
# hasta otro punto y cubrir otra ruta. Cuentan con una flota activa
# de N micros. Necesitan saber si les es posible cubrir con ella los
# requerimientos o si requieren contar con micros extra.
# Resolver el problema utilizando como parte del mismo redes de
# flujo. Analice su complejidad temporal y espacial.