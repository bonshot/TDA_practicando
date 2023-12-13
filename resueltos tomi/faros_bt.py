#Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos.
#Implementar un algoritmo que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden
#iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las
#directamente adyacentes a estas (es decir, un “radio de 2 celdas”).


# submarinos = [
#     (2, 4),
#     (5, 1),
#     (6, 7),
#     (4, 3),
# ]

submarinos = [
          (2,0),
    #faro      

    (1,3),     (3,3),

    (1,5),     (3,5),
    #faro

          (2, 8)
]

# submarinos = [
#                       (3, 0),
#  (0, 1),               
#                             (4, 2),
            
#               (2, 4),                     (6, 4), (7, 4),
# ]



mejor_solucion = 0
def resolver(submarinos):
    global mejor_solucion
    mejor_solucion = len(submarinos) + 1
    return _resolver(submarinos, set())

#          sin iluminar    solución parcial  
def _resolver(submarinos, faros):
    global mejor_solucion

    # Ya no quedan submarinos a iluminar
    if len(submarinos) == 0:
        # Si esta solución es mejor, guardo el nuevo máximo de faros
        if len(faros) < mejor_solucion:
            mejor_solucion = len(faros)

        # Devuelvo la solución
        return faros
    
    # En este punto ya hay una solución con len(faros) o menos faros
    if len(faros) >= mejor_solucion:
        return None

    # generar posiciones posibles para faros
    posibles_faros = generar_posibles_faros(submarinos)
    soluciones = []

    # Probamos las soluciones a partir de todos los lugares que puedo poner un faro
    for coordenadas, submarinos_iluminados in posibles_faros:
        # Creamos un nuevo se de submarinos para usar en la llamada recursiva
        subs_set = submarinos.copy()
        # Eliminamos los submarinos iluminados
        for ilum in submarinos_iluminados:
            subs_set.remove(ilum)

        # Creamos un nuevo set de faros para usar en la llamada recursiva
        nuevo_set = set()
        for faro in faros:
            nuevo_set.add(faro)
        # Agregamos el nuevo faro
        nuevo_set.add(coordenadas)

        # Llamamos recursivamente, resolvemos el subproblema
        nuevos_faros = _resolver(subs_set, nuevo_set)
        # Si no se encontró ninguna solución mejor, no la agregamos
        if nuevos_faros != None:
            soluciones.append(nuevos_faros)

    # Buscamos la mejor solución de las encontradas recursivamente
    min_faros = None
    for sol in soluciones:
        if min_faros == None:
            min_faros = sol
        elif len(min_faros) > len(sol):
            min_faros = sol
    return min_faros



def generar_posibles_faros(submarinos):
    posibles_faros = dict()
    for sub in submarinos:
        for x in range(-2, 3):
            for y in range(-2, 3):
                # if y == 0 and x == 0:
                #     continue
                sub_x, sub_y = sub
                # coords = f"{sub_x + x}_{sub_y + y}"
                coords = (sub_x + x, sub_y + y)

                if coords[0] < 0 or coords[1] < 0:
                    continue

                valor = posibles_faros.get(coords) or set()
                valor.add(sub)
                posibles_faros[coords] = valor
    posibles_faros_lista = []
    for coordenada, cantidad_de_submarinos_que_ilumina in posibles_faros.items():
        posibles_faros_lista.append((coordenada, cantidad_de_submarinos_que_ilumina))
    posibles_faros_lista.sort(key=lambda x:x[1])
    return posibles_faros_lista

print(resolver(submarinos))
