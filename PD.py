#1) Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados,
#utilizando programación dinámica. Indicar y justificar el orden del algoritmo implementado.
#Aclaración: siempre es posible escribir a n como suma de n términos de la forma 1**2, por lo que siempre existe solución. 
# Sin embargo, la expresión 10 = 3**2 + 1**2
# es una manera más económica de escribirlo para n = 10, pues sólo tiene dos
# términos. Además, tener en cuenta que no se piden los términos, sino la cantidad mínima de términos cuadráticos
# necesaria.
from math import sqrt 
def cuadrados_minimizados(n):
    cant = [0]*(n+1)
    cant[0] = 0
    cant[1] = 1

    for i in range(2, n + 1):
        for j in range(1, int(sqrt(i)) + 1):
            cuadrado = j * j
            if cuadrado == i:
                cant[i] = 1
            else:
                if cant[i] == 0:
                    cant[i] = cant[i - cuadrado] + 1
                else:
                    cant[i] = min(cant[i], cant[i - cuadrado] + 1)
    print(cant)
    return cant[-1]
def cuadrados_minimizados2(n):
    cant = ["inf"]*(n+1)
    cant[0] = 0
    sist = [x**2 for x in range(1,n)]
    for i in range(1, n+1):
        minimo = i
        for cuadrado in sist:
            if cuadrado > i:
                continue
            cantidad = 1 + cant[i-cuadrado]
            if cantidad < minimo:
                minimo = cantidad
        cant[i] = minimo
    return cant[n]
# Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren
# sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en
# un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se
# trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden
# sentarse. Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan
# la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos). Indicar
# y justificar la complejidad del algoritmo.
#w = 10
#n = [2,5,8]

def trolegon(P, W):
    n = len(P)
    matriz = [[0 for i in range(W + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if P[i - 1] > j:
                matriz[i][j] = matriz[i - 1][j]
            else:
                matriz[i][j] = max(matriz[i - 1][j], matriz[i - 1][j - P[i - 1]] + P[i - 1])
    return matriz[n][W]
#Sea G un grafo dirigido “camino” (las aristas son de la forma (vi, vi+1)). Cada vertice tiene un valor (positivo).
#Implementar un algoritmo que, utilizando programación dinámica, obtenga el Set Independiente de suma máxima
#dentro de un grafo de dichas características. Indicar y justificar la complejidad del algoritmo implementado.

# G = [(1, 2), (2, 3), (3, 4), (4, 5)]
# V = [1, 2, 3, 4, 5]

def imprimir_matriz_de_mierda(matriz):
    for i in range(len(matriz)-1, -1, -1):
        print(matriz[i])

def set_hijo_de_remil_puta(G, V):
    matriz = [[0 for i in range(len(V) )] for j in range(len(G) + 1)]
    for i in range(1, len(G) + 1):
        for j in range(1, len(V)):
            if G[i - 1][1] == V[j - 1]:
                matriz[i][j] = max(matriz[i - 1][j], matriz[i - 1][j - 1] + V[j - 1])
            else:
                matriz[i][j] = matriz[i - 1][j]
    imprimir_matriz_de_mierda(matriz)
    return matriz[len(G)][len(V)-1]

#Dada una soga de n metros (n ≥ 2) implementar un algoritmo que, utilizando programación dinámica, permita cortarla
#(en partes de largo entero) de manera tal que el producto del largo de cada una de las partes resultantes sea máximo. El
#algoritmo debe devolver el valor del producto máximo alcanzable. Indicar y justificar la complejidad del algoritmo.
#Ejemplos:
#n = 2 --> Debe devolver 1 (producto máximo es 1 * 1)
#n = 3 --> Debe devolver 2 (producto máximo es 2 * 1)
#n = 5 --> Debe devolver 6 (producto máximo es 2 * 3)
#n = 10 -> Debe devolver 36 (producto máximo es 3 * 3 * 4)

def soga_de_mierda(n):
    max_product = [0] * (n+1)
    max_product[1] = 1
    max_product[2] = 1

    for i in range(3, n+1):
        for j in range(1, i):
            max_product[i] = max(max_product[i], max(j, max_product[j]) * max(i - j, max_product[i - j]))
    print(max_product)
    return max_product[n]


#**************************************************************************************************
#Se conoce como “Longest increasing subsequences” al problema de
#encontrar la subsecuencia más larga de números (no necesariamente
#consecutivos) donde cada elemento sea mayor a los anteriores en
#una secuencia de números.
#Ejemplo: En la lista → 2, 1, 4, 2, 3, 9, 4, 6, 5, 4, 7. Podemos
#ver que la subsecuencia más larga es de longitud 6 y corresponde a
#la siguiente (marcada en negrita) “1, 2, 3, 4, 5, 7”

def esta_materia_me_tiene_las_bolas_por_el_suelo(lista):
    res = [1] * len(lista)
    res2 = []

    for i in range(1, len(lista)):
        for j in range(i):
            if lista[j] < lista[i] and res[i] < res[j] + 1:
                res[i] = res[j] + 1
                res2.append(res[i])
    return max(res)

#**********************************************************************************
#El dueño de una cosechadora está teniendo una demanda muy elevada
#en los próximos 3 meses. Desde “n” campos lo quieren contratar
#para que preste sus servicios. Lamentablemente no puede hacer
#todos los contratos puesto que varios de ellos se superponen en
#sus tiempos. Cuenta con un listado de los pedidos donde para cada
#uno de ellos se consigna: fecha de inicio, fecha de finalización,
#monto a ganar por realizarlo. Su idea es seleccionar la mayor
#cantidad de trabajos posibles. Por eso seleccionará primero
#aquellos trabajos que le demanden menos tiempo. Mostrarle que esta
#solución puede no ser la óptima. Proponer una solución utilizando
#programación dinámica que nos otorgue el resultado óptimo.
#Analizar su complejidad temporal y espacial.

## Paso 1: ordenar como scheduling por fecha de finalizacion
## Paso 2: detectar colisiones 
## Paso 3: Agregar el de mas valor
## Paso 4: Repetir
## Paso 5: Devolver el valor total


#**********************************************************************************



# lista = [1, 2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 20, 22]
# def che_solucion(M_CHE, valor, p, j, solucion):
#     if j == 0:
#         return solucion
#     if M_CHE[j][p] != M_CHE[j - 1][p]:
#         solucion.append(j)
#         return che_solucion(M_CHE, valor, p - valor[j], j - 1, solucion)
#     else:
#         return che_solucion(M_CHE, valor, p, j - 1, solucion)

#**********************************************************************************


# Juan el vago
# Juan es ambicioso pero tambien algo vago. Dispone de varias ofertas
# de trabajo diarias, pero no quiere trabajar dos dias seguidos. Dado un
# arreglo con el monto esperado a ganar cada dıa, determinar por programacion dinamica el maximo monto a ganar, sabiendo que no aceptara
# trabajar dos dıas seguidos.
# La idea para afrontar esta problematica, es analizar lo que se puede hacer
# con un d´ıa en particular: trabajarlo y no poder trabajar el dıa anterior, o no
# trabajarlo y s´ı poder utilizar el dıa anterior.
# La ecuaci´on de recurrencia se reduce a:
# → OP T(j) = max ↗ trabajar un d´ıa: Vj + OP T(j - 2)
#                 ↘ no trabajar el dıa: OP T(j - 1)

# trabajo = [10,5,25,30,12,10,19,22,55]
def juan_del_vago(trabaajo):
    n = len(trabaajo)
    opt = [0]*n
    opt[0] = trabaajo[0]
    opt[1] = max(trabaajo[0], trabaajo[1])

    for i in range(2, n):
        opt[i] = max(opt[i-1], opt[i-2] + trabaajo[i])
    print(opt)
    return opt[n-1]
#Complejidad O(N)
#**********************************************************************************

#Problema de la mochila
def mochila(capacidad, valor, peso):
    n = len(valor)
    opt = [[0]*(capacidad+1)for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(capacidad+1):
            if peso[i-1] <= w:
                opt[i][w] = max(valor[i-1] + opt[i-1][w-peso[i-1]],opt[i-1][w])
            else:
                opt[i][w] = opt[i-1][w]
    return opt[n][capacidad]
#Complejidad O(W*N)

#**********************************************************************************
#Problema del cambio
def cambio(sistema, monto):
    n = len(sistema)
    opt = ["inf"]*(n+1)
    opt[0] = 0
    for i in range(1,monto+1):
        minimo = i
        for j in sistema:
            if minimo >j:
                continue
            cantidad = 1+ opt[i-j]
            if cantidad < moneda:
                minimo = cantidad
        opt[i] = minimo
    return opt[monto]

#**********************************************************************************
#Subste sum
def subset(conjunto,numero):
    n = len(conjunto)
    opt =[[0]*(numero+1)for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,numero+1):
            if conjunto[i-1] > j:
                opt[i][j] = opt[i-1][j]
            else:
                opt[i][j] = max(opt[i-1][j], opt[i-1][j-conjunto[i-1]]+conjunto[i-1])
    print(opt)
    return opt[n][numero]



def main():
    # print(cuadrados_minimizados(6))
    # print(cuadrados_minimizados2(6))
    #print(trolegon([2, 10, 3], 9))

    #print(set_hijo_de_remil_puta([(1, 2), (2, 3), (3, 4), (4, 5)], [1, 2, 3, 5, 10]))
    
    # print(soga_de_mierda(2))

    # print(esta_materia_me_tiene_las_bolas_por_el_suelo([2, 1, 4, 2, 3, 9, 4, 6, 5, 4, 7]))

    # print(che_solucion([(1, 2, 5), (3, 5, 10), (2, 4, 8), (5, 6, 2), (5, 8, 4), (4, 7, 20)]))
    # print(juan_del_vago([10,5,25,30,12,10,19,22,55]))
    # valor = [10,15,2]
    # peso =[5,10,12]
    # capacidad=27
    # print(mochila(capacidad, valor, peso))
    print(subset([1, 3, 5, 8, 10],7))

main()
