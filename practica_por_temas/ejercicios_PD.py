# Para una inversión inmobiliaria un grupo inversor desea desarrollar un barrio privado paralelo a la una ruta. 
# Con ese motivo realizaron una evaluación de los diferentes terrenos en un trayecto de la misma. Diferentes inversores participarán, 
# pero a condición de comprar algún terreno en particular. El grupo inversor determinó para cada propiedad su evaluación de ganancia. 
# El mismo surge como la suma de inversiones ofrecida por el terreno menos el costo de compra. Debemos recomendar que terrenos contiguos comprar para que maximicen sus ganancias.  
# Ejemplo: S = [-2, 3, -3, 4, -1, 2]. La mayor ganancia es de 5, comprando los terrenos de valor  [4, -1, 2]. Solucionar el problema mediante un algoritmo de programación dinámica.
def maximizar_ganancias_terrenos(S):
    n = len(S)
    ganancias = [0] * n
    seleccion = [-1] * n

    ganancias[0] = S[0]

    for i in range(1, n):
        if ganancias[i - 1] > 0:
            ganancias[i] = ganancias[i - 1] + S[i]
            seleccion[i] = i - 1
        else:
            ganancias[i] = S[i]

    max_ganancia = max(ganancias)
    index = ganancias.index(max_ganancia)

    terrenos_seleccionados = []
    while index != -1:
        terrenos_seleccionados.insert(0, S[index])
        index = seleccion[index]

    return terrenos_seleccionados

# La organización de una feria internacional tiene que programar diferentes eventos a realizar en su escenario principal. 
# Para ello pueden elegir, en los diferentes días del evento, entre algunos de los siguientes rubros: un cantante, una compañía de danza, un show de variedades o un humorista.  
# Disponen de una oferta de cada tipo para cada día y la posible ganancia por venta de entradas. Existen ciertas restricciones que se aplican. 
# No se pueden repetir 2 días seguidos el mismo rubro. 
# Además por el tiempo de preparación un día después de un cantante solo puede presentarse un humorista. Plantear la resolución mediante programación dinámica.
def max_ganancia(eventos):
    dias = len(eventos)
    rubros = len(eventos[0])

    # Inicializar una matriz para almacenar las ganancias máximas
    dp = [[0] * rubros for _ in range(dias)]

    # Llenar la matriz bottom-up
    for dia in range(dias):
        for rubro in range(rubros):
            ganancia_actual = eventos[dia][rubro]

            # Calcula la ganancia máxima considerando las restricciones
            if dia > 0:
                ganancia_anterior = max(dp[dia - 1][r] for r in range(rubros) if r != rubro)
                dp[dia][rubro] = ganancia_actual + ganancia_anterior
            else:
                dp[dia][rubro] = ganancia_actual

    # La ganancia máxima estará en la última fila de la matriz
    return max(dp[dias - 1])

# Ejemplo de uso
eventos = [
    [10, 5, 8, 3],  # Ganancias para el día 1
    [7, 12, 6, 2],  # Ganancias para el día 2
    [5, 8, 10, 4]   # Ganancias para el día 3
]

ganancia_maxima = max_ganancia(eventos)
# print("Ganancia máxima posible:", ganancia_maxima)
# Una empresa de transporte aéreo cuenta con un avión que cubre una ruta que une dos ciudades. Se especializa en llevar maquinaria pesada. 
# Puede realizar un vuelo diario y trasladar una cantidad de peso determinada. 
# Por cada kilo transportado cobra una tarifa. Por día recibe un pedido de transporte que puede aceptar o rechazar en su totalidad (no se pueden fraccionar). 
# Si rechaza un pedido, lo pierde y no lo puede realizar otro día. Existe una regulación especial que indica que la carga máxima a transportar disminuye según una fórmula  por día. 
# Se restablece a su máximo únicamente si el avión pasa por revisión e inspección.  Este proceso insume 3 días seguidos. 
# El gerente de la empresa cuenta con una planilla que detalla los envíos solicitados en el próximo mes y la tabla de peso máximo por día pasado desde la última revisión. 
# El avión llegó el día anterior de la revisión. Construir un algoritmo que permita maximizar las ganancias.
def maximizar_ganancias(envios, capacidad_maxima, dias_para_revision):
    n = len(envios)
    dp = [0] * (n + dias_para_revision)

    for i in range(n - 1, -1, -1):
        dp[i] = max(dp[i + 1], envios[i] + dp[i + dias_para_revision])

    return dp[0]

# Ejemplo de uso
    # Datos de ejemplo
envios = [100, 200, 150, 50, 300]  # Lista de pedidos diarios
capacidad_maxima = [500, 450, 400, 350, 300]  # Capacidad máxima según los días desde la última revisión
dias_para_revision = 3

    # Calcular la ganancia máxima
ganancia_maxima = maximizar_ganancias(envios, capacidad_maxima, dias_para_revision)

# Un ramal ferroviaria pone en concesión los patios de comida en todas las estaciones. Son en total “n” estaciones. 
# Por cada estación se cuenta con el promedio de facturación de los últimos 5 años. 
# Por normativa antimonopólica existe como limitante que ninguna empresa puede explotar 3 o más estaciones contiguas. Pero ,no existe una cantidad máxima de estaciones a explotar. 
# Un oferente nos solicita que le digamos cuales son las estaciones que le conviene obtener para maximizar sus ganancias. Plantee la solución mediante programación dinámica.
def maximizar_ganancias_estaciones(facturacion):
    n = len(facturacion)

    # Inicializar una matriz para almacenar las ganancias acumulativas
    dp = [0] * n

    # Llenar la matriz bottom-up
    for i in range(n):
        # Caso base
        if i == 0:
            dp[i] = facturacion[i]
        elif i == 1:
            dp[i] = max(facturacion[i], dp[i - 1])
        elif i == 2:
            dp[i] = max(facturacion[i] + dp[i - 2], dp[i - 1])
        else:
            dp[i] = max(facturacion[i] + dp[i - 2], facturacion[i] + dp[i - 3], dp[i - 1])

    # Determinar las estaciones seleccionadas
    estaciones_seleccionadas = []
    i = n - 1
    while i >= 0:
        if i == 0 or dp[i] != dp[i - 1]:
            estaciones_seleccionadas.append(i)
            i -= 2
        else:
            i -= 1

    estaciones_seleccionadas.reverse()
    return estaciones_seleccionadas
facturacion = [10, 20, 15, 30, 5, 25]

    # Calcular las estaciones que maximizan las ganancias
estaciones_maximizadas = maximizar_ganancias_estaciones(facturacion)
print("Estaciones seleccionadas:", estaciones_maximizadas)

# Para un nuevo satélite a poner en órbita una empresa privada puede optar por incluir diversos sensores a bordo 
# (por ejemplo: variación de temperatura, humedad en tierra, caudal de ríos, etc). 
# Cada uno de ellos tiene un peso "pi" y una ganancia "gi" calculado por su uso durante la vida útil del satélite. 
# Si bien les gustaría incluir todos, el satélite tiene una carga máxima P que puede llevar. 
# Nos piden que generemos un algoritmo (utilizando programación dinámica) para resolver el problema. Indique si su solución es polinomial.
def mochila_satelite(carga_maxima, pesos, ganancias):
    n = len(pesos)
    matriz_dp = [[0] * (carga_maxima + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for capacidad_actual in range(carga_maxima + 1):
            # No incluir el elemento actual
            sin_incluir = matriz_dp[i - 1][capacidad_actual]

            # Incluir el elemento actual si es posible
            incluir = 0
            if pesos[i - 1] <= capacidad_actual:
                incluir = ganancias[i - 1] + matriz_dp[i - 1][capacidad_actual - pesos[i - 1]]

            # Actualizar la matriz DP
            matriz_dp[i][capacidad_actual] = max(sin_incluir, incluir)

    ganancia_total = matriz_dp[n][carga_maxima]
    return ganancia_total


# Ejemplo de uso
if __name__ == "__main__":
    carga_maxima = 10
    pesos = [2, 3, 4, 5]
    ganancias = [3, 4, 5, 6]

    ganancia_maxima = mochila_satelite(carga_maxima, pesos, ganancias)
    print("Ganancia máxima posible:", ganancia_maxima)
# Se conoce como “Longest increasing subsequences” al problema de, dado un vector de numérico, encontrar la subsecuencia más larga de números (no necesariamente consecutivos) 
# donde cada elemento sea mayor a los anteriores. Ejemplo: En la lista →  2, 1, 4, 2, 3, 9, 4, 6, 5, 4, 7. 
# Podemos ver que la subsecuencia más larga es de longitud 6 y corresponde a la siguiente “1, 2, 3, 4, 6, 7”.  Resolver el problema mediante programación dinámica.

def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Ejemplo de uso
if __name__ == "__main__":
    vector = [2, 1, 4, 2, 3, 9, 4, 6, 5, 4, 7]
    
    longitud_lis = longest_increasing_subsequence(vector)
    
    print("Longitud de la subsecuencia creciente más larga:", longitud_lis)