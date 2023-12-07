# Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El listado (ordenado por nombre del pueblo) c
# ontiene el número de kilómetros donde está ubicada cada una. Se desea ubicar la menor cantidad de patrullas policiales (en las bifurcaciones) 
# de tal forma que no haya bifurcaciones con vigilancia a más de 50 km.
#  Proponer un algoritmo que lo resuelva. 
def bifurcaciones_patrulla(lista):
    lista.sort(key=lambda x: x[1])
    patrulleros = []
    for bifu in lista:
        if len(patrulleros) == 0:
            patrulleros.append(bifu)
        else:
            if patrulleros[-1][1] + 50 < bifu[1]:
                patrulleros.append(bifu)
    return patrulleros
lista = [("Castelli", 185), ("Gral Guido", 249), ("Lezama", 156), ("Maipu", 270), ("Sevigne", 194)]
lista2 = [("A", 10), ("B", 20), ("C", 30), ("D", 40), ("E", 50)]
# print(bifurcaciones_patrulla(lista2))
#Este algoritmo es greedy porque busca aprovechar por cada seleccion, la mayor distancia 
#de cubrimiento de kilometros para saber donde poner patrulleros, asi para la solucion
#final es poner la menor cantidad de patrulleros en las bifurcaciones
#La complejidad esO(n), donde n es el largo de la lista
#Puede haber un caso donde las distancias entre las bifurcaciones sea mayor a 50 entonces tendriamos
#n patrulleros 

#**********************************************************************************

# Para la realización del próximo congreso de “charlas motivacionales para el joven de hoy” se contrató un hotel que cuenta con m salas de exposición. 
# Existirán “n” oradores. Cada uno solicitó un tiempo de exposición definido por un horario de ingreso y una duración. 
# Los organizadores quieren asignar las salas con un intervalo entre charla y charla de 15 minutos y desean utilizar la menor cantidad de salas posibles. 
# Presentar un algoritmo greedy que resuelve el problema indicando la cantidad de salas a utilizar y la asignación de las charlas. 
# En caso de sobrepasar el máximo de salas disponibles informar. Analice complejidad y optimalidad 
def asignar_salas(oradores, m):
    oradores_ordenados = sorted(oradores, key=lambda x: (x[0], x[1]))  # Ordenar oradores por tiempo de inicio

    salas = [[] for _ in range(m)]  # Inicializar salas

    for orador in oradores_ordenados:
        asignado = False
        orador_inicio = (orador[0], orador[1])
        orador_fin = (orador[2], orador[3])

        for sala in salas:
            if not sala or orador_inicio >= (sala[-1][2], sala[-1][3] + 15):
                sala.append((orador_inicio[0], orador_inicio[1], orador_fin[0], orador_fin[1]))
                asignado = True
                break

        if not asignado:
            salas.append([(orador_inicio[0], orador_inicio[1], orador_fin[0], orador_fin[1])])  # Asignar una nueva sala

    return salas


# Ejemplo de uso:
oradores = [(9, 0, 9, 30), (9, 30, 10, 15), (10, 15, 10, 35), (10, 45, 11, 15)]
m = 2  # Número máximo de salas

# print(asignar_salas(oradores, m))

#La complejidad del algoritmos es O(n*m) donde m es la cantidad de salas disponibles y n
#es la cantidad de oradores
#El algoritmo optimo no es optimo porque puede haber el caso que si evitamos la restriccion
#de 15 minutos post finalizacion de charla, podriamos usar mas charlas dentro de una sala y
#y usar menos salas
#**********************************************************************************

# El club de amigos de la república Antillense prepara un ágape en sus instalaciones en la que desea invitar a la máxima cantidad de sus “n” socios. 
# Sin embargo por protocolo cada persona invitada debe cumplir un requisito: Sólo puede asistir si conoce a al menos otras 4 personas invitadas. 
# Nos solicita seleccionar el mayor número posible de invitados. Proponga una estrategia greedy óptima para resolver el problema.
def amigos_invitados(diccionario, persona):
    amigos_invitados = 0
    for amigo in persona[1]:
        if diccionario.get(amigo) == True:
            amigos_invitados += 1
    return amigos_invitados
def amigos_club(amigos):
    amigos.sort(key=lambda x: len(x[1]), reverse=True)
    invitados = {}
    for persona in amigos:
        invitados[persona[0]] = True
    for persona in amigos:
        amigos_invitados_cu = amigos_invitados(invitados, persona)
        if amigos_invitados_cu < 4:
            invitados[persona[0]] = False
    print(invitados)
    lista = []
    for persona, invitacion in invitados.items():
        if invitacion:
            lista.append(persona)
    return lista

lista = [
    ("A", ["B", "C", "D"]),
    ("B", ["A", "C", "D"]),
    ("C", ["A", "B", "D"]),
    ("D", ["A", "B", "C"]),
    ("E", ["A", "B", "C", "D"]),
    ("F", ["A", "B", "C", "D"]),
    ("G", ["A", "B", "C", "D"]),
]
# print(amigos_club(lista))
#La complejidad del algoritmo es O(n**2 + I), donde I es la cantidad de invitados
# y n es la cantidad de personas}
#El algoritmo no es optimo porque en el caso de 
# lista = [
#     ("A", ["B", "C", "D"]),
#     ("B", ["A", "C", "D"]),
#     ("C", ["A", "B", "D"]),
#     ("D", ["A", "B", "C"]),
#     ("E", ["A", "B", "C", "D"]),
#     ("F", ["A", "B", "C", "D"]),
#     ("G", ["A", "B", "C", "D"]),
# ]
#No tendria que ir ningun invitado, porque A,B,C no cumplen el requisito
#Y automaticamente E,F,G pasarian a tener 0 invitados porque esos no van
#Pero el algoritmo me daria E,F,G como invitados

#********************************************************************

# Un importante club de campo debe cerrar durante un mes sus instalaciones. En ese tiempo tiene que licenciar a la mayoría de sus empleados. 
# Entre ellos a los guardias de seguridad. Cada uno de ellos trabaja 1 vez por mes en un horario de corrido por mes iniciando un día determinado y finalizando unos días después. 
# Habitualmente varios guardias se superponen en algunos momentos del mes. Pero sabemos que siempre hay al menos 1 de ellos en las instalaciones. 
# Los que nos solicitan es que dejemos a la mínima cantidad de guardias posibles y que aun siempre haya al menos uno custodiando durante el mes. 
# Proponga un algoritmo greedy eficiente que lo resuelve.

def seleccionar_guardias(guardias):
    guardias.sort(key=lambda x: x[0])
    guardias_seleccionados = []
    fecha_actual = 1
    for guardia in guardias:
        inicia, fin = guardia
        if fecha_actual <=inicia:
            guardias_seleccionados.append(guardia)
            fecha_actual = fin+1
    return guardias_seleccionados

guardias = [(3, 10), (6, 15), (12, 20), (18, 25), (22, 30)]
print(seleccionar_guardias(guardias))

# El ajedrez se juega con un tablero cuadriculado. La pieza llamada “Rey” puede moverse en cualquiera de los 8 cuadrados aledañas a su posición actual comiendo cualquier 
# otra pieza que esté en ellos. Contamos con un tablero especial de nxm cuadrados y una cantidad ilimitada de piezas “Rey”. 
# Queremos ubicar la mayor cantidad de reyes sin que estos se puedan comer entre si. Proponer un algoritmo greedy para resolverlo. 
# Brindar complejidad. Justificar la optimalidad de su propuesta.

#El algoritmo no es optimo, porque pueden haber mejores ubicaciones para ubicar a los reyes y asi obtener mayor cantidad de reyes en el tablero

# El proceso de aprobación de trámites de la “central burocrática” está dividido en 2 partes.
# La primera parte consiste en una entrevista personalizada cuya duración se puede conocer
# según el tipo de trámite. La segunda parte es la revisión de la documentación cuya duración
# se calcula previamente mediante una fórmula matemática en función de la persona solicitante.
# Cada día se citan “n” personas. Cada una para realizar un trámite. Por cada persona se cuenta,
# entonces, con su tiempo de la etapa 1 y su tiempo de la etapa 2. La etapa 1 únicamente la
# realiza 1 empleado. Para la etapa 2, hay una cantidad ilimitada de personal para realizarla.
# Nuestra tarea es determinar el orden de atención para cada una de las “n”. El objetivo es
# minimizar el tiempo total de espera.
# Presentar una solución greedy que resuelva el problema. Explicar la optimalidad del mismo. 

def orden_atencion(tramites):
    tramites.sort(key=lambda x: x[1]/x[0])
    tiempo_actual_espera = 0
    tiempo_actual_etapa1 = 0
    for tramite in tramites:
        tiempo_actual_etapa1 += tramite[0]
        tiempo_actual_espera += max(0, tiempo_actual_etapa1 - tramite[1])
    return tiempo_actual_espera
# Un fabricante de perfumes está intentando crear una nueva
# fragancia. Desea que la misma sea del menor costo posible. El
# perfumista le indicó un listado de ingredientes. Por cada uno de
# ellos determinó una cantidad mínima (puede ser cero) y una máxima
# que debe contar en la fórmula final. Cada ingrediente tiene
# asociado un costo por milímetros cúbicos. Conocemos que la
# presentación final es de X milímetros cúbicos totales. Presentar
# una solución utilizando metodología greedy que resuelva el
# problema. Analizar la complejidad temporal y espacial. Probar
# optimalidad

def crear_fragancia(ingredientes, capacidad_total):
    # Asegurarse de que los valores sean numéricos
    ingredientes = [(nombre, float(min_cantidad), float(max_cantidad), float(costo)) for nombre, min_cantidad, max_cantidad, costo in ingredientes]

    # Ordenar ingredientes por costo por milímetro cúbico (mínimo primero)
    ingredientes_ordenados = sorted(ingredientes, key=lambda x: x[3] / x[2])
    print(ingredientes_ordenados)
    fragancia = []
    capacidad_actual = 0
    costo_total = 0
    while capacidad_actual < capacidad_total:
        for ingrediente, min_cantidad, max_cantidad, costo in ingredientes_ordenados:
            cantidad_a_utilizar = min(max_cantidad - min_cantidad, capacidad_total - capacidad_actual)
            
            if cantidad_a_utilizar > 0:
                fragancia.append((ingrediente, cantidad_a_utilizar))
                capacidad_actual += cantidad_a_utilizar
                costo_total += cantidad_a_utilizar * costo

    return fragancia, costo_total

# Ejemplo de uso:
ingredientes = [("Ingrediente1", 2, 3, 0.1), ("Ingrediente2", 2, 5, 1.5), ("Ingrediente3", 1, 3, 1)]
capacidad_total = 10

fragancia_optima, costo_optimo = crear_fragancia(ingredientes, capacidad_total)

print("Fragancia óptima:", fragancia_optima)
print("Costo total óptimo:", costo_optimo)
