# Problemas de scheduling con peso

# Tengo un aula/sala donde quiero dar charlas. Las charlas tienen horario
# de inicio y fin, y un peso asociado al valor de cada charla. Quiero utilizar
# el aula para maximizar la sumatoria de pesos de las charlas dadas.


def maximizar_pesos_charlas_dinamico(n, valores, p):
    if n == 0:
        return 0

    M_CHE = [None] * (n + 1)
    M_CHE[0] = 0

    for j in range(1, n + 1):
        M_CHE[j] = max(valores[j - 1] + M_CHE[p[j - 1]], M_CHE[j - 1])

    return M_CHE[n]
#******************************************************************************

# Juan del vago

# Juan es ambicioso pero tambi´en algo vago. Dispone de varias ofertas
# de trabajo diarias, pero no quiere trabajar dos d´ıas seguidos. Dado un
# arreglo con el monto esperado a ganar cada d´ıa, determinar por programaci´on din´amica el m´aximo monto a ganar, sabiendo que no aceptar´a
# trabajar dos d´ıas seguidos.

def juan_del_vago(lista):
    n = len(lista)
    res = [0] * n
    res[0] = lista[0]
    res[1] = max(res[0], lista[1])
    for i in range(2, n):
        res[i] = max(res[i-1], res[i-2] + lista[i])
    dias_trabajados = [False] * n
    i = n-1
    while i >= 2:
        if res[i] == res[i-1]:
            i -= 1
        else:
            dias_trabajados[i] = True
            i -=2
    dias_trabajados[0] = res[0] > res[1]
    dias_trabajados[1] = res[1] > res[0]

    for i in range(2, n):
        if dias_trabajados[i] and dias_trabajados[i - 1]:
            dias_trabajados[i] = False
    return dias_trabajados, res

# print(juan_del_vago([5,10,2,15,20,3,1]))
#******************************************************************************

# Problema de la mochila
# Tenemos una mochila con una capacidad W (peso, volumen). Hay elementos a guardar. 
# Cada elemento tiene un peso y un valor. Queremos
# maximizar el valor de lo que nos llevamos sin pasarnos de la capacidad.

def mochila(capacidad, valor, peso):
    n = len(valor)
    opt = [[0]*(capacidad+1)for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(capacidad+1):
            if peso[i-1] <= w:
                opt[i][w] = max(valor[i-1] + opt[i-1][w-peso[i-1]],opt[i-1][w])
            else:
                opt[i][w] = opt[i-1][w]
    
    elementos_en_mochila = []
    i, w = n, capacidad
    while i > 0 and w > 0:
        if opt[i][w] != opt[i-1][w]:
            elementos_en_mochila.append((peso[i-1], valores[i-1]))
            w -= peso[i-1]
        i-=1
    return opt[n][capacidad], elementos_en_mochila

capacidad_mochila = 50
valores = [60, 100, 120]
pesos = [10, 20, 30]
# print(mochila(capacidad_mochila, valores, pesos))
#Complejidad O(W*N)

#******************************************************************************

# Problema del cambio
# Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar cambio de una determinada cantidad de plata. Implementar un algoritmo
# que devuelva el cambio pedido, usando la m´ınima cantidad de monedas/-
# billetes.
def problema_del_cambio(sistema, plata):
    res = ["INF"] * (plata+1)
    res[0] = 0
    monedas_utilizadas = [[] for _ in range(plata + 1)] 
    for i in range(1 ,plata+1):
        minimo = i
        for j in sistema:
            if j <= i:
                if 1 + res[i-j] < minimo:
                    minimo = 1 + res[i-j]
                    monedas_utilizadas[i] = monedas_utilizadas[i - j] + [j]

        res[i] = minimo
    return res[plata], monedas_utilizadas[plata]
print(problema_del_cambio([5,2,1,10,15,50], 85))


#******************************************************************************

# Subset Sum
# Tenemos un conjunto de n´umeros v1, v2, . . . Vn, y queremos obtener
# un subconjunto de todos esos n´umeros cuya suma sea igual a un valor
# V, o bien aproximar lo mayor posible a ese valor V.

def subset_sum(numeros, numero):
    n = len(numeros)
    res = [[0]*(numero+1)for _ in range(n+1)]
    for i in range(n+1):
        for j in range(numero+1):
            if i == 0 or j == 0:
                res[i][j] = 0
            elif numeros[i - 1] > j:
                res[i][j] = res[i - 1][j]
            else:
                res[i][j] = max(res[i - 1][j], res[i - 1][j - numeros[i - 1]] + numeros[i - 1])
    
    numeros_seleccionados = []
    i, j = n, numero
    while i > 0 and j > 0:
        if res[i][j] != res[i - 1][j]:
            numeros_seleccionados.append(numeros[i - 1])
            j -= numeros[i - 1]
        i -= 1

    numeros_seleccionados.reverse()
    
    return res[n][numero], numeros_seleccionados
# numeros = [3, 54, 4, 12, 5, 2]
# valor_objetivo = 75
# print(subset_sum(numeros, valor_objetivo))

#******************************************************************************

# T´u a Londres y yo a California
# Manejamos un negocio que atiende clientes en Londres y en California.
# Nos interesa cada mes decidir si operar en una u otra ciudad. Los costos
# de operaci´on para cada mes pueden variar y son dados: Li y Ci para
# todo n.
# Naturalmente, si en un mes operamos en una ciudad, y al siguiente en
# una distinta, habr´a un costo fijo M por la mudanza.
# Dados los costos de operaci´on en Londres (L) y California (C), indicar
# la secuencia de las n localizaciones en las que operar durante n meses,
# sabiendo que queremos minimizar los costos de operaci´on. Se puede
# empezar en cualquier ciudad

#******************************************************************************

# Fraccionamiento del aceite de oliva
# Contamos con un dep´osito de L litros lleno de aceite de oliva. Queremos
# fraccionarlo y venderlo en el mercado. De acuerdo a las especificaciones
# vigentes solo se puede fraccionar en valores enteros de litros. Una tabla
# regulatoria determina el valor de venta para cada i litros como Vi
# . Podemos fraccionar como queramos, pero deseamos maximizar la ganancia.

#******************************************************************************

# M´axima suma de segmento
# Dado una lista L de n elementos. Cada elemento tiene asociado un
# valor num´erico (positivo o negativo). Queremos encontrar el subconjunto
# contiguo de elementos que sume el mayor valor posible.