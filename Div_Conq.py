#Un grupo de científicos han liberado “n” boyas en diferentes puntos de los océanos para realizar un estudio sobre las
#corrientes marinas. Cada boya tiene un emisor de posición que informa a una computadora central su ubicación cada minuto. Entre
#los estudios que desean realizar se encuentra determinar cuales dos boyas se encuentran más cerca entre sí. Ese proceso lo tienen
#que realizar en forma eficiente, ya que se realiza de forma constante y solo es uno de los tantos análisis que realizan.
#Utilizando división y conquista proponga una forma de solucionarlo. Explique paso a paso su solución y analice su complejidad.

# Si asumimos que se nos fue un algoritmo ordenado de menor distancia a mayor distancia, podemos asumir que dos elementos adyacentes son
# los mas cercanos entre si con respecto al resto.
# Lo que pense que podiamos hacer era dividir la lista hasta tener listas de un elemento. De alli vamos uniendo observando 
# si entre los dos elementos unidos son menores a un mínimo predefinido, hacemos esto hasta terminar de unir la lista en completo.
# la complejidad, si la lista está ordenada, sería aplicar el teorema maestro, con O(n) de complejidad (A=2, B=2, C=0) (es como buscar el minimo con div y conq.)
# En caso de que no esté ordenado el algoritmo, aplico un algoritmo de ordenamiento comparativo segun se necesite (O n log(n))

#boyas = [(0,0), (2,2), (3,4), (4,4), (5,5), (8,8), (10,10)]
from math import sqrt

def distancia(p1, p2):
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def distancia_minima_puntos(puntos):
    puntos = sorted(puntos, key=lambda x: x[0])
    return _distancia_minima_puntos(puntos)

def _distancia_minima_puntos(puntos):
    n = len(puntos)
    medio = n // 2
    
    if n <= 3:
        return min(distancia(puntos[i], puntos[j]) for i in range(n) for j in range(i+1, n))

    punto_medio = puntos[medio]
    d_izq = _distancia_minima_puntos(puntos[:medio])
    d_der = _distancia_minima_puntos(puntos[medio:])

    d = min(d_izq, d_der)

    puntos_cercanos = []
    for punto in puntos:
        if abs(punto[0] - punto_medio[0]) < d:
            puntos_cercanos.append(punto)
    puntos_cercanos = sorted(puntos_cercanos, key=lambda x: x[1])
    print(puntos_cercanos)
    for i in range(len(puntos_cercanos)):
        for j in range(i+1, len(puntos_cercanos)):
            if abs(puntos_cercanos[j][1] - puntos_cercanos[i][1] < d):
                d = distancia(puntos_cercanos[i], puntos_cercanos[j])
    return d

# La complejidad temporal de este algoritmo es O(n) 

#*************************************************************************************************
#Un equipo de trabajo ha realizado una votación anónima para
#seleccionar a una persona entre ellos que los represente. En total
#hay “n” personas. Cada una de ellas realiza un voto. Tenemos el
#voto de cada uno de ellos. El líder debe ser seleccionado por más
#del 50% del total para ganar. Proponer un algoritmo por división y
#conquista que determine si hay un ganador y en caso afirmativo que
#informe quien es. Analice la complejidad de su propuesta

# votos = [4, 3, 4, 1, 3, 2, 2, 1, 3]

#Buscar el que aparece más de la mitad de las veces con div y conq
def lider_trolo(votos):
    votos = sorted(votos)
    return _lider_trolo(votos)

def _lider_trolo(votos):
    n = len(votos)
    medio = n // 2

    if n == 1:
        return votos[0]
    
    lider_izq = _lider_trolo(votos[:medio])
    lider_der = _lider_trolo(votos[medio:])

    if lider_izq == lider_der:
        return lider_izq
    
    contador_izq = 0
    contador_der = 0

    for voto in votos:
        if voto == lider_izq:
            contador_izq += 1
        elif voto == lider_der:
            contador_der += 1

    if contador_izq > n // 2:
        return lider_izq
    elif contador_der > n // 2:
        return lider_der
    else:
        return -1 


#*****************************************************************************************
#Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, 
#tal que la cantidad total de elementos del arreglo es potencia de 2 (por ende, n también lo es). 
#Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, 
#sin utilizar espacio adicional (obviando el utilizado por la recursividad). ¿Cual es la complejidad del algoritmo?
#Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos ({C1, C2, D1, D2}). 
#Luego, pensar a partir de allí el caso de 8 elementos, etc… para encontrar el patrón.

def wea(lista):
    res = []
    n = len(lista)//2
    for i in range(n):
        res.append(lista[i])
        res.append(lista[n+i])
    return res

#******************************************************************************************
#Se cuenta con un vector de “n” posiciones en el que se encuentran algunos de los primeros ”m” números naturales ordenados en forma creciente (m >= n). 
#En el vector no hay números repetidos. Se desea obtener el menor número no incluido. Ejemplo: [1, 2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 20, 22]. 
#Solución: 6. Proponer un algoritmo de tipo división y conquista que resuelva el problema en tiempo inferior a lineal. 
#Expresar su relación de recurrencia y calcular su complejidad temporal.

def poronga_de_busqueda_con_div_y_conq_porque_soy_un_culo_y_no_se_hacer_busquedas(lista):
    return _poronga_de_busqueda_con_div_y_conq_porque_soy_un_culo_y_no_se_hacer_busquedas(lista, 0, len(lista) - 1)
    
def  _poronga_de_busqueda_con_div_y_conq_porque_soy_un_culo_y_no_se_hacer_busquedas(lista, inicio, fin):
    if inicio > fin:
        return fin + 2
    
    medio = (fin + inicio) //2
    if lista[medio] == medio + 1:
        return _poronga_de_busqueda_con_div_y_conq_porque_soy_un_culo_y_no_se_hacer_busquedas(lista, medio+1, fin)
    else:
        return _poronga_de_busqueda_con_div_y_conq_porque_soy_un_culo_y_no_se_hacer_busquedas(lista, inicio, medio-1)

#*************************************************************************************************
#Dado un vector A de “n” números enteros (tanto positivos como negativos) 
#queremos obtener el subvector cuya suma de elementos sea mayor a la suma de cualquier otro subvector en A.  
#Ejemplo: Array: [-2, -5, 6, -2, -3, 1, 5, -6]. Solución: [6, -2, -3, 1, 5]. Resolver el problema de subarreglo de suma máxima por división y conquista.

def subarreglo_suma_maxima_te_odio_div_y_conq(lista):
    return _subarreglo_suma_maxima_te_odio_div_y_conq(lista, 0, len(lista) - 1)

def _subarreglo_suma_maxima_te_odio_div_y_conq(lista, inicio, fin):
    if inicio == fin:
        return lista[inicio]
    
    medio = (inicio + fin) // 2
    suma_izq = _subarreglo_suma_maxima_te_odio_div_y_conq(lista, inicio, medio)
    suma_der = _subarreglo_suma_maxima_te_odio_div_y_conq(lista, medio + 1, fin)

    suma_izq_max = lista[medio]
    suma_izq_temp = 0
    for i in range(medio, inicio - 1, -1):
        suma_izq_temp += lista[i]
        suma_izq_max = max(suma_izq_max, suma_izq_temp)
    
    suma_der_max = lista[medio + 1]
    suma_der_temp = 0
    for i in range(medio + 1, fin + 1):
        suma_der_temp += lista[i]
        suma_der_max = max(suma_der_max, suma_der_temp)

    return max(suma_izq, suma_der, suma_izq_max + suma_der_max)


# a. Hacer un seguimiento del algoritmo de Quicksort, con selección aleatoria de pivot, para ordenar los siguientes
# elementos: 45 14 24 35 16 11 30 15 39 19 41. Para las selecciones aleatorias de pivot, considerar que el primer
# elemento elegido es el 16. Para las siguientes selecciones aleatorias tuvimos “suerte”, siempre se seleccionó el valor
# de la mediana en cada caso.
# b. Indicar la complejidad temporal esperada de Quicksort.
# c. Mostrar un Árbol Binario de Búsqueda que, si se lo construye apropiadamente, realiza las mismas comparaciones
# que el segumiento de Quicksort detallado anteriormente. Indicar de qué manera se construyó el árbol.
# d. Indicar cuáles serían las peores selecciones de pivot e indicar en qué complejidad temporal resultaría.

# *********************

# Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número 
# n, en tiempo O(logn). Por ejemplo, para 
# n=10 debe devolver 3, y para 
# n=25 debe devolver 5.

def _raiz_entera_todita(arr, inicio, fin, n):
    if inicio == fin:
        return arr[inicio]
    medio = (inicio + fin) // 2
    if arr[medio]**2 > n:
        return _raiz_entera_todita(arr, inicio, medio - 1, n)
    elif arr[medio]**2 < n:
        return _raiz_entera_todita(arr, medio + 1, fin, n)
    else:
        return arr[medio]


def raiz_entera_todita(n):
    arr = [i for i in range(0, n)]
    return _raiz_entera_todita(arr, 0, n - 1, n)

def raiz_entera(n):
    inicio, final = 0, n
    while inicio <= final:
        medio = (inicio + final) // 2
        medio_cuadrado = medio*medio
        if medio_cuadrado == n:
            return medio_cuadrado
        if medio_cuadrado < n:
            inicio = medio + 1
            resultado = medio
            
        else:
            final = medio -1
    
    return resultado 
        

def main():
    #boyas = [(0,0), (3,25), (0,1)]
    #print(distancia_minima_puntos(boyas))

    #votos = [1, 3, 4, 1, 3, 1, 2, 1, 1]
    #print(lider_trolo(votos))

    #weaa = ["C1", "C2", "C3", "D1", "D2", "D3"]
    #print(wea(weaa))

    #numeros = [1, 2, 3, 4, 5, 6]
    #print(poronga_de_busqueda_con_div_y_conq_porque_soy_un_culo_y_no_se_hacer_busquedas(numeros))

    # lista = [-2, -5, 6, -2, -3, 1, 5, -6]
    # print(subarreglo_suma_maxima_te_odio_div_y_conq(lista))
    
    print(raiz_entera(10))

    
if __name__ == '__main__':
    main()