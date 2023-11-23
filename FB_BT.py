#1)Contamos con un conjunto de “n” puntos (x,y) en el plano cartesiano.
# Un par de puntos es el más cercano si la distancia euclidiana entre ellos es menor a la de cualquier otro par. 
# Resuelva el problema mediante un algoritmo naive que nos informe cuales son los 3 pares de puntos más cercanos. 
# Lista = [(1,2), (5,8), (2,13), (5,10), (7,2), (9,15), (15,30), (2,9)]

from math import sqrt


def distancia_euclideana(x1,x2,y1,y2):
    suma = ((x2-x1)**2)+((y2-y1)**2)
    return sqrt(suma)

def puntos_chotos(lista):
    arr_distancias = []
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j and (lista[j], lista[i], distancia_euclideana(lista[i][0],lista[j][0],lista[i][1],lista[j][1])) not in arr_distancias:
                arr_distancias.append((lista[i], lista[j], distancia_euclideana(lista[i][0],lista[j][0],lista[i][1],lista[j][1])))
    ordenado = sorted(arr_distancias, key=lambda x: x[2], reverse=False)
    return ordenado[:3]

#2)Un cuadrado mágico de tamaño “n” es una disposición de los números enteros desde 1 a n^2 en una matriz de nxn que cumple la siguiente condiciones.  
#Cada número aparece solo una vez. La suma de cada fila, columna y diagonal principal da el mismo valor.
#Proponer un algoritmo por generar y probar que dado un valor “n” calcule, si existe, un cuadrado mágico de ese tamaño. 
# matriz[[1,2,3],[4,5,6],[7,8,9]]

#Usamos backtracking ya que tenemos información para la poda
def generar_matriz_culorrota(n):
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
    return matriz

def culeado_magico_batrakin(n):
    matriz = generar_matriz_culorrota(n)
    numeros = []
    for i in range(1, n**2 + 1):
        numeros.append(i)
    
    return _culeado_magico_batrakin(matriz, numeros, 0, 0, n)

def es_culeado_magico(matriz, fila, columna, n):
    suma_fila = 0
    suma_columna = 0
    suma_diagonal = 0
    visitados = set()

    for i in range(n):
        suma_fila += matriz[fila][i]
        suma_columna += matriz[i][columna]
        suma_diagonal += matriz[i][i]
    
    if suma_fila != suma_columna or suma_columna != suma_diagonal:
        return False
    
    for i in range(n):
        suma_fila_aux = 0
        suma_columna_aux = 0
        for j in range(n):
            if matriz[i][j] in visitados and matriz[i][j] != 0:
                return False
            visitados.add(matriz[i][j])
            suma_fila_aux += matriz[i][j]
            suma_columna_aux += matriz[j][i]
        if (suma_fila_aux != 0 and suma_columna_aux != 0) and (suma_fila_aux != suma_fila or suma_columna_aux != suma_columna):
            return False # Fijarse como chota hacer esto (Verificar que es culeado magico parcialmente cuando tenemos 0's)
     
    return True

def _culeado_magico_batrakin(matriz, numeros, fila, columna, n):
    if fila == n:
        return True
    for i in range(len(numeros)):
        print(numeros[i])
        matriz[fila][columna] = numeros[i]
        if es_culeado_magico(matriz, fila, columna, n):
            if columna == n-1:
                if _culeado_magico_batrakin(matriz, numeros, fila + 1, 0, n):
                    return True
                else:
                    _culeado_magico_batrakin(matriz, numeros, fila, columna + 1, n)
        
    print(matriz)
    matriz[fila][columna] = 0
    return False

#3)Se encuentran en un río 3 caníbales y 3 vegetarianos. En la orilla hay un bote que permite pasar a dos personas atravesarlo. 
#Los 6 quieren cruzar al otro lado. Sin embargo existe un peligro para los vegetarianos: 
#si en algún momento en alguna de las márgenes hay más caníbales que vegetarianos estos los atacarán. 
#Tener en cuenta que el bote tiene que ser manejado por alguien para regresar a la orilla. 
#Determinar si es posible establecer un orden de cruces en el que puedan lograr su objetivo conservando la integridad física. 
#Explicar cómo construir el grafo de estados del problema. Determinar cómo explorarlo para conseguir la respuesta al problema. 
#Brinde, si existe, la respuesta al problema.

# lista = [((canibales_inicio, vegetarianos_inicio, canibales_fin, vegetarianos_fin), (canibales_bote, vegetarianos_bote)), ...]
def estado_valido(estado):
    if (estado[0] > estado[1]) or (estado[2] > estado[3]):
        return False
    return True


#Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos.
#Implementar un algoritmo que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden
#iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las
#directamente adyacentes a estas (es decir, un “radio de 2 celdas”).

#Porque estamos iluminando submarinos con gps??
    
def submarinos_del_orto2(matriz):
    faros_totales = {}
    lista = []
    submarinos_cubiertos_totales = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != "s":
                submarinos_cubiertos = revisar_radio_2(matriz, i, j)
                if len(submarinos_cubiertos) != 0:
                    faros_totales[(i,j)] = submarinos_cubiertos
    # print(faros_totales)
    for faro, submarinos in faros_totales.items():
        lista.append((faro, submarinos))
    lista.sort(key=lambda x: len(x[1]), reverse=True)
    
    # consigo la cantidad minima de faros que cubran todos los submarinos
    faros = 0
    faros_ubicados = []
    for faro in lista:
        if revisar_submarino_cubierto(submarinos_cubiertos_totales, faro[1]):
            for submarino in faro[1]:
                if submarino not in submarinos_cubiertos_totales:
                    submarinos_cubiertos_totales.append(submarino)
            faros +=1
            faros_ubicados.append(faro[0])

    print(faros_ubicados)
    print(faros)   

def revisar_submarino_cubierto(submarinos_cubiertos, submarinos_por_ver):
    largo_por_ver = len(submarinos_por_ver)
    submarinos_no_cubiertos = 0
    for submarino in submarinos_por_ver:
        if submarino not in submarinos_cubiertos:
            return True
    return False

def revisar_radio_2(matriz, i, j):
    submarinos = []
    min_x, max_x = max(i - 2, 0), min(i + 2, len(matriz) - 1)
    min_y, max_y = max(j - 2, 0), min(j + 2, len(matriz[0]) - 1)
    for k in range(min_x, max_x +1):
        for l in range(min_y, max_y+1):
            if matriz[k][l] == "s":
                submarinos.append((k, l))
    return submarinos

#7)Se cuenta con “n” trabajos por realizar y la misma cantidad de contratistas para realizarlos. 
# Ellos son capaces de realizar cualquiera de los trabajos aunque una vez que se comprometen a hacer uno, no podrán realizar el resto.
# Tenemos un presupuesto de cada trabajo por cada contratista. Queremos asignarlos de forma tal de minimizar el costo del trabajo total. 
# Proponer un algoritmo por branch and bound que resuelva el problema de la asignación. 

#8)Contamos con un conjunto de “n” de equipamientos que se deben repartir entre un conjunto de “m” equipos de desarrollo. 
#  Cada equipo solicita un subconjunto de ellas. Puede ocurrir que un mismo equipamiento lo soliciten varios equipos o incluso que un equipamiento no lo solicite nadie. 
#  Queremos determinar si es posible seleccionar un subconjunto de equipos de desarrollo entregándoles a todos ellos todo lo que soliciten 
#  y al mismo tiempo que ninguno de los equipamientos quede sin repartir. Resolver el problema mediante backtracking.


#10)Contamos con un conjunto de “n” actividades entre las que se puede optar por realizar. 
#Cada actividad x tiene una fecha de inicio Ix, una fecha de finalización fx y un valor vx que obtenemos por realizarla. 
#Queremos seleccionar el subconjunto de actividades compatibles entre sí que maximice la ganancia a obtener (suma de los valores del subconjunto). 
#Proponer un algoritmo por branch and bound que resuelva el problema.

def main():
    #lista = [(1,2), (5,8), (2,13), (5,10), (7,2), (9,15), (15,30), (2,9)]
    #print(puntos_chotos(lista))
    
    # print(culeado_magico_batrakin(3))

    # matriz =[["s", "a", "a", "a", "a", "a", "a", "a", "a", "s"],
    #         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #         ["a", "a", "a", "a", "s", "a", "a", "a", "a", "a"],
    #         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #         ["a", "a", "a", "a", "a", "a", "a", "s", "a", "a"],
    #         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #         ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
    #         ["s", "a", "a", "a", "a", "a", "a", "a", "a", "s"],

    #         ]
    # submarinos_del_orto2(matriz)
    pass
    
if __name__ == '__main__':
    main()