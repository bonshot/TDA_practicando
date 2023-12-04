# 1) Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El listado (ordenado por nombre del pueblo) 
#    contiene el número de kilómetro donde está ubicada cada una. 
#    Se desea ubicar la menor cantidad de patrullas policiales (en las bifurcaciones) de tal forma que no haya bifurcaciones con vigilancia a menos de 50 km.
# Ciudad      Bifurcación
# Castelli    185
# Gral Guido  249
# Lezama      156
# Maipú       270
# Sevigne     194
# Si pongo un patrullero en la bifurcación de Lezama, cubro Castelli y Sevigne. Pero no Gral Guido y Maipú. Necesitaría en ese caso, poner otro. 
# Agrego otro patrullero en Gral Guido. 
# Con eso tengo 2 móviles policiales en bifurcaciones que cubren todas los accesos a todas las ciudades con distancia menor a 50 km. 
# Proponer un algoritmo que lo resuelva. Justificar que la solución es óptima

#lista = [("Castelli", 185), ("Gral Guido", 249), ("Lezama", 156), ("Maipu", 270), ("Sevigne", 194)]

#lista = [("Lezama", 156), ("Castelli", 185) , ("Sevigne", 194), ("Gral Guido", 249), ("Maipu", 270)]

def patrulleros_ruta(lista):
    ordenado = sorted(lista, key=lambda x: x[1])
    patrulleros = []
    for bifu in ordenado:
        if len(patrulleros) == 0:
            patrulleros.append(bifu)
        else:
            if patrulleros[-1][1] + 50 < bifu[1]:
                patrulleros.append(bifu)
    print(len(patrulleros))

# La solución es óptima siempre ya que verifica de manera greedy que la distancia entre los patrulleros sea mayor a 50km
# De esta manera la cantidad de bifurcaciones en las que dejamos un patrullero será la mínima posible abarcando todas las ciudades
# en un rango de 50km hacia atrás y adelante (del patrullero).

# 2) El algoritmo de Prim sobre un grafo conexo y ponderado obtiene el árbol recubridor mínimo del mismo. 
#    Esto es, el subconjunto de aristas que formando un árbol incluye a todos los vértices. 
#    De todos los posibles árboles recubridores es aquel cuya suma de los valores de las aristas es el menor posible.
#    El algoritmo se puede resumir a “grosso modo” de la siguiente manera: 
#    1. Iniciar el árbol con un nodo elegido arbitrariamente 
#    2. Mientras existan vértices sin unir al árbol 
#    3. Obtener la arista de menor peso disponible que sale del árbol a un vértice externo 
#    4. Agregar el vértice con la arista al árbol. 
#   a) Explique por qué es un algoritmo de tipo greedy 
#   b) Ensaye una explicación para la optimalidad de este algoritmo 
#   c) Explique qué estructuras utilizaría para implementarlo y formalice el algoritmo
#   d) Calcule la complejidad temporal del mismo.

# a) El algoritmo de Prim es greedy ya que avanza de forma de usar el menor peso posible en la siguiente arista a agregar al grafo
#    sin mirar todas las posibilidades, sino que se va armando según el estado actual, de esta manera construye el MST optando por
#    la primera opción de arista mínima disponible.
# b) Este algoritmo es óptimo ya que como siempre opta por conectar los dos vértices con arista de menor peso posible, siempre vamos
#    a obtener una representación de árbol (Puede haber varias) cuyo recorrido sume el menor peso posible en el total de las aristas.
#    Al ir de menor a mayor en lo que a peso de aristas se refiere, siempre obtendremos un árbol que llegue todos los vértices con el
#    menor peso posible.
# c) Usaría un grafo para poder armar el árbol (que a fin de cuentas es un grafo sin ciclos) y luego un Heap de aristas del grafo original para
#    disponer de las aristas de menor a mayor en prioridad.
# d) La complejidad temporal de Prim está compuesta por la complejidad de sacar un elemento del heap E veces (ya que sacamos todas las aristas
#    en el peor caso donde debemos usar todas las aristas para conectar la totalidad de los vértices), esto es O(E * log(V)). Meter al heap los
#    elementos implica recorrer todas las aristas del grafo, lo que es recorrer a su vez todos los vértices (Tomamos eso como cota superior), 
#    esto es O(E * log(V)), entonces finalmente O(E * log(V) + E * log(V)) = O(2E * log(V)) = O(E * log(V))

# 3) Una empresa cuenta con N máquinas que pueden realizar la misma tarea. 
#    Las mismas se alquilan por diferentes días (contienen un día de inicio y fin). 
#    El trabajo del revisor de planta es, dado un conjunto de M pedidos en el mes, determinar si los mismos se podrán realizar sin problemas. 
#    Generar un algoritmo que retorne si los trabajos aceptados son válidos o no. ¿Qué complejidad tiene? ¿Es óptimo? 

# 4) Los grupos sanguíneos de las personas son cuatro: A, B, O y AB. Los pacientes se clasifican según su grupo sanguíneo. 
#    Un paciente O sólo puede recibir sangre O, un paciente A sólo puede recibir sangre A u O, un paciente B sólo puede recibir sangre B u O, 
#    un paciente AB puede recibir cualquier grupo sanguíneo. Diseñar una estrategia greedy para resolver el siguiente problema: 
#    Sean Sa, Sb, So, Sab la sangre disponible de cada uno de los grupos y Pa, Pb, Po, Pab los pacientes de cada grupo que concurren al hospital para 
#    recibir una unidad de transfusión. Informar cómo se puede satisfacer la demanda de sangre de los pacientes (o si no se puede satisfacer). Justificar. 

# arr_disp = [(A, 10), (B, 25), (O, 12), (AB, 54)]
# arr_requerido = [(A, 5), (B, 40), (O, 10), (AB, 42)]

# Ordenamos de menor a mayor según la cantidad de sangres aceptadas por el paciente, entonces aquellos de sangre O recibirán sangre primero
# , los de sangre A o B recibirán después y finalmente los de sangre AB, de esta forma agotamos la primera posibilidad de sangre requerida 
# encontrada de tal manera que se pueda satisfacer la mayor cantidad de pacientes posibles (Al priorizar primero los que tienen un requisito
# estricto o de menor cantidad de fuentes, optimizo el uso de esa sangre).

# arr_disp = [(A, 10), (B, 25), (O, 12), (AB, 54)]
# arr_requerido = [(A, 5), (B, 40), (O, 10), (AB, 42)] sum(97)

# Ingresan los pacientes O
# arr_sang_disp = [(A, 10), (B, 25), (O, 2), (AB, 54)]
# arr_requerido = [(A, 5), (B, 40), (AB, 42)]

#Ingresan los pacientes A
# arr_sang_disp = [(A, 5), (B, 25), (O, 2), (AB, 54)]
# arr_requerido = [(B, 40), (AB, 42)]

#Ingresan los pacientes B
# arr_sang_disp = [(A, 5), (AB, 54)]
# arr_requerido = [(B, 13), (AB, 42)]

#Ingresan los pacientes AB

# arr_sang_disp = [(AB, 17)]
# arr_requerido = [(B, 13)] # Como tenemos una de las sangres con requerido > 0, no pudimos satisfacer la demanda

#OTRO EJEMPLO
# arr_disp = [(A, 25), (B, 10), (O, 12), (AB, 54)]
# arr_requerido = [(A, 40), (B, 5), (O, 10), (AB, 42)]

# Ingresan los pacientes O
# arr_disp = [(A, 25), (B, 10), (O, 2), (AB, 54)]
# arr_requerido = [(A, 40), (B, 5), (AB, 42)]

#Ingresan los pacientes A
# arr_disp = [(B, 10), (AB, 54)]
# arr_requerido = [(A, 13), (B, 5), (AB, 42)]

#Ingresan los pacientes B
# arr_disp = [(AB, 17)]
# arr_requerido = [(A, 13)]

#5) Una carrera tipo “Ironman” es un triatlón compuesto por 3 instancias: natación (3,86 km de natación), ciclismo (180 km) y carrera a pie (42,2km).
#   Para conocer al ganador se suman los tiempos realizados en cada una de las etapas. 
#   Tanto el ciclismo como la carrera a pie se puede realizar en simultáneo con todos los inscriptos. 
#   Pero, por una regulación se prohibió que más de 1 persona realice la etapa de nado en el lago en simultáneo. 
#   Se conoce el tiempo estimado de cada participante para cada evento. Proponga un orden de salida de tal forma de minimizar el tiempo total de toda la competencia. 

# (Natacion, ciclismo, carrera a pie)
def ironman(lista):
    ordenado_por_natacion = sorted(lista, key=lambda x: x[0], reverse=False)
    total_natacion = 0
    list_sobrantes = []
    for part in ordenado_por_natacion:
        total_natacion += part[0]
    suma_nat = 0
    for tiempos in ordenado_por_natacion:
        if suma_nat + sum(tiempos) > total_natacion:
            list_sobrantes.append(tiempos[1] + tiempos[2] - (total_natacion - tiempos[0]- suma_nat))
        suma_nat += tiempos[0]

    max_sobrante = max(list_sobrantes)
    print(max_sobrante)
    resultado = total_natacion + max_sobrante
    
    print(resultado)

#6) Una fotocopiadora cada mañana recibe un conjunto de pedidos de clientes. 
# El pedido del cliente i demora ti en ejecutarse. 
# Para una planificación dada (es decir un cierto orden de las tareas) Ci es la hora en la cual el pedido i termina de ejecutarse 
# (por ejemplo, si el pedido j es el primero que se ejecuta, Cj = tj; si el pedido j se ejecuta a continuación del pedido i, Cj=Ci+tj). 
# Cada cliente tiene un peso wi que representa su importancia. 
# Se supone que la felicidad de un cliente depende de cuán rápido le entregan el trabajo, por lo que la empresa decide minimizar el tiempo de demora ponderado = Suma (wi * Ci).
# Diseñar un algoritmo greedy eficiente para resolver este problema. Calcular su eficiencia temporal y espacial. Justificar la optimalidad de la solución. 


# [(Tj, Wj)...]
def fotoculeadora(planificacion):
    return sorted(planificacion, key=lambda x: x[1]/x[0], reverse=True)
    
def calcular_fotoculeadora(planificacion):
    tiempo, demora = 0, 0
    for p in planificacion:
        tiempo += p[0]
        demora += tiempo * p[1]
    return demora
# La solución es óptima ya que al ordenar por el cociente entre el peso y el tiempo de cada pedido, estamos priorizando 
# aquellos con mayor peso y menor tiempo, entonces al ir de mayor a menor en este criterio, optimizamos el tiempo
# de demora ponderado. La complejidad temporal es O(n*log(n)) por el ordenamiento de mergesort y la espacial es O(n)

#7) El club de amigos de la república Antillense prepara un ágape en sus instalaciones en la que desea invitar a la máxima cantidad de sus “n” socios.
#   Sin embargo por protocolo cada persona invitada debe cumplir un requisito: Sólo puede asistir si conoce a al menos otras 4 personas invitadas. 
#   Nos solicita seleccionar el mayor número posible de invitados. Proponga una estrategia greedy óptima para resolver el problema.


def amigos_invitados(diccionario, persona):
    amigos_invitados = 0
    for amigo in persona[1]:
        if diccionario.get(amigo) == True:
            amigos_invitados += 1
    return amigos_invitados

def amigos_culo2(lista):
    ordenado = sorted(lista, key=lambda x: len(x[1]), reverse=False)
    invitados = {}
    for persona in ordenado:
        invitados[persona[0]] = True
    
    for persona in ordenado:
        amigos_invitados_culo = amigos_invitados(invitados, persona)
        if amigos_invitados_culo < 4:
            invitados[persona[0]] = False

    lista = []
    for persona, invitacion in invitados.items():
        if invitacion:
            lista.append(persona)
    print(lista)
    print(len(lista))

# [(Nombre, [Amigos])...]

#11) Un fabricante de perfumes está intentando crear una nueva fragancia. 
#    Y desea que la misma sea del menor costo posible. El perfumista le indicó un listado de ingredientes. 
#    Por cada uno de ellos determinó una cantidad mínima (puede ser cero) y una máxima que debe contar en la fórmula final. 
#    Cada ingrediente tiene asociado un costo por milímetros cúbicos. Sabiendo que en la presentación final es de X milímetros cúbicos. 
#    Presentar una solución utilizando metodología greedy que resuelva el problema.

# [(nombre, (min, max), costo_por_mm3)...]
def perfume_olor_poronga(ingredientes, w):
    ordenado = sorted(ingredientes, key=lambda x: x[2], reverse=False)
    
    lista_costos = {}

    olor = 0
    for ingrediente in ordenado:
        olor += ingrediente[1][0]
        lista_costos[ingrediente[0]] = ingrediente[1][0] * ingrediente[2]

    for ingrediente in ordenado:
        if olor + (ingrediente[1][1] - ingrediente[1][0]) >= w:
            lista_costos[ingrediente[0]] += (w - olor) * ingrediente[2]
            break
        else:
            olor += (ingrediente[1][1] - ingrediente[1][0])
            lista_costos[ingrediente[0]] += (ingrediente[1][1] - ingrediente[1][0]) * ingrediente[2]
    print(lista_costos)
    print(sum(lista_costos.values()))


#Se tiene como posibles grupos sanguíneos de personas O, A, B y AB. Alguien con sangre tipo O sólo puede recibir sangre
#tipo O. Alguien de sangre A sólo puede recibir sangre de tipo A u O. Alguien de sangre tipo B sólo puede recibir sangre
#de tipo B u O. Alguien con sangre tipo AB puede recibir sangre de cualquier tipo. Se tienen las cantidades de bolsas de
#sangre disponibles (SA, SB, SAB, SO) y la cantidad de personas a tratar (PA, PB, PAB, PO). Implementar un algoritmo
#greedy que determine cómo se puede satisfacer la demanda de sangre (o si no puede hacerse). Indicar el orden del
#algoritmo y justificar por qué el algoritmo propuesto es un algoritmo greedy.

# arr_disp = [(A, 10), (B, 25), (O, 12), (AB, 54)]
# arr_requerido = [(A, 5), (B, 40), (O, 10), (AB, 42)]

def sangre_porongol(arr_disp, arr_requerido):
    dict = {"A": ["A", "O"], "B": ["B", "O"], "O": ["O"], "AB": ["A", "B", "O", "AB"]}
    # arr_disp = sorted(arr_disp, key=lambda x: len(dict[x[0]]))
    arr_requerido = sorted(arr_requerido, key=lambda x: len(dict[x[0]]))

    for i in range(0, len(arr_requerido)):
        chabones_actuales = arr_requerido[i]
        for j in range(0, len(arr_disp)):
            disponible_actual = arr_disp[j]
            if disponible_actual[0] in dict[chabones_actuales[0]] and disponible_actual[1] > 0:
                arr_disp[j] = (disponible_actual[0], disponible_actual[1] - chabones_actuales[1]) if disponible_actual[1] - chabones_actuales[1] > 0 else (disponible_actual[0], 0)
                arr_requerido[i] = (chabones_actuales[0], chabones_actuales[1] - disponible_actual[1]) if chabones_actuales[1] - disponible_actual[1] > 0 else (chabones_actuales[0], 0)
    print(arr_requerido)
    print(arr_disp)
    for k in range(0, len(arr_requerido)):
        if arr_requerido[k][1] != 0:
            return False
    return True
            

def vampiros_SA(arr_disp, arr_requerido):
    dict = {"A": ["A", "O"], "B": ["B", "O"], "O": ["O"], "AB": ["A", "B", "O", "AB"]}
    disponibilidad = {}
    for tipo in arr_disp:
        disponibilidad[tipo[0]] = tipo[1]
    arr_requerido = sorted(arr_requerido, key=lambda x: len(dict[x[0]]))

    for i in range(0, len(arr_requerido)):
        tipo = arr_requerido[i]
        for aceptado in dict[tipo[0]]:
            minimo = min(disponibilidad[aceptado], tipo[1])
            arr_requerido[i] = (tipo[0], tipo[1] - minimo)
            tipo = arr_requerido[i]
            disponibilidad[aceptado] -= minimo
        
    for tipo in arr_requerido:
        if tipo[1] != 0:
            return False
    return True

# La complejidad es O(Cant. Tipos de Sangre * Cant. Tipos aceptados), es un algoritmo greedy porque se busca una sangre que aceptemos de manera inmediata
# (la primera posible que encontramos la consumimos y pasamos a la siguiente). Antes de eso buscamos que se sacien aquellos con menor aceptación de sangres
# , de esa manera maximizamos la cantidad total de personas saciadas ya que no agotamos esa posibilidad con otro paciente que tenga otra sangre a disposición.


    
def main():
    #Ej 1
    #lista = [("Castelli", 185), ("Gral Guido", 249), ("Lezama", 156), ("Maipu", 270), ("Sevigne", 194), ("Lasalle", 360)]
    #patrulleros_ruta(lista) #Funca >:D

    #Ej 5
    # lista = [(13,10,5),(5,8,10),(8,15,2),(20,1,1)]
    # ironman(lista)
    #ordenado_por_natacion  = [(20,1,1),(13,10,5),(8,15,2),(5,8,10)]

    #Ej 6
    #planificacion = [(3,5),(6,1),(1,8),(3,4),(7,5)]
    #print(calcular_fotoculeadora(fotoculeadora(planificacion)))

    #Ej 7 Probamos con una lista de distinta cantidad de invitados (puede haber con cantidad <= 3)
    # lista = [("A", ["B", "C", "D", "E", "G"]), ("B", ["A", "C", "D", "E", "G"]), ("C", ["A", "B", "D", "E"]), ("D", ["A", "B", "C", "E", "G"]), ("E", ["A", "B", "C", "D", "G"]), ("F", ["G"]), ("G", ["A", "B", "C", "D", "E", "F"])]
    # amigos_culo2(lista)

    #Ej 11
    # ingredientes = [("A", (4, 10), 10), ("B", (2, 10), 5), ("C", (3, 10), 2), ("D", (3, 10), 1)]
    # perfume_olor_poronga(ingredientes, 15)

    #Ej sangre
    arr_disp = [("A", 5), ("B", 25), ("O", 17), ("AB", 54)]
    arr_requerido = [("A", 10), ("B", 25), ("O",12), ("AB", 54)]
    print(vampiros_SA(arr_disp, arr_requerido))

if __name__ == '__main__':
    main()


