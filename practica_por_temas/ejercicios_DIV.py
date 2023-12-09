# Se cuenta con un vector de “n” posiciones en el que se encuentran algunos de los primeros ”m” números naturales ordenados en forma creciente (m >= n). 
# En el vector no hay números repetidos. Se desea obtener el menor número no incluido. Ejemplo: [1, 2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 20, 22]. 
# Solución: 6. Proponer un algoritmo de tipo división y conquista que resuelva el problema en tiempo inferior a lineal.
# Expresar su relación de recurrencia y calcular su complejidad temporal.
def numero_faltante(arr):
    return _numero_faltante(arr, 0, len(arr)-1)

def _numero_faltante(arr, inicio, fin):
    if inicio > fin:
        return arr[fin]+1
    medio = (inicio+fin)//2
    if arr[medio] == medio+1:
        return _numero_faltante(arr, medio+1, fin)
    else:
        return _numero_faltante(arr, inicio, medio-1)

print(numero_faltante([1, 2, 3, 4, 5, 6,7,8, 9, 11, 12, 13, 14, 20, 22]))
# Dado un vector A de “n” números enteros (tanto positivos como negativos) 
# queremos obtener el subvector cuya suma de elementos sea mayor a la suma de cualquier otro subvector en A. 
# Ejemplo: Array: [-2, -5, 6, -2, -3, 1, 5, -6]. Solución: [6, -2, -3, 1, 5]. 
# Resolver el problema de subarreglo de suma máxima por división y conquista.
def subset_suma(arr):
    return _subset_suma_maxima(arr, 0, len(arr)-1)
def _subset_suma_maxima(arr, inicio, fin):
    if inicio == fin:
        return arr[inicio]
    
    medio = (inicio + fin) // 2
    suma_izq = _subset_suma_maxima(arr, inicio, medio)
    suma_der = _subset_suma_maxima(arr, medio + 1, fin)

    suma_izq_max = arr[medio]
    suma_iz_temp = 0
    for i in range(medio, inicio-1, -1):
        suma_iz_temp += arr[i]
        suma_izq_max = max(suma_izq_max, suma_iz_temp)
    suma_der_max = arr[medio+1]
    suma_der_temp = 0
    for i in range(medio+1, fin+1):
        suma_der_temp += arr[i]
        suma_der_max = max(suma_der_max, suma_der_temp)
    return max(suma_der_max + suma_izq_max, suma_izq, suma_der)
# print(subset_suma([-2, -5, 6, -2, -3, 1, 5, -6]))

#****************************************************

#Un equipo de trabajo ha realizado una votación anónima para
#seleccionar a una persona entre ellos que los represente. En total
#hay “n” personas. Cada una de ellas realiza un voto. Tenemos el
#voto de cada uno de ellos. El líder debe ser seleccionado por más
#del 50% del total para ganar. Proponer un algoritmo por división y
#conquista que determine si hay un ganador y en caso afirmativo que
#informe quien es. Analice la complejidad de su propuesta
def lider(arr):
    return _lider(arr)

def _lider(arr):
    n = len(arr)
    medio = n//2
    if n==1:
        return arr
    lider_izq = _lider(arr[:medio])
    lider_der = _lider(arr[medio:])
    contadorizq, contadorder = 0,0
    for voto in arr:
        if voto == lider_izq:
            contadorizq+=1
        elif voto == lider_der:
            contadorder+=1
    if contadorizq > n//2:
        return lider_izq
    elif contadorder > n//2:
        return lider_der
    return -1

#******************************************

#Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, 
#tal que la cantidad total de elementos del arreglo es potencia de 2 (por ende, n también lo es). 
#Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, 
#sin utilizar espacio adicional (obviando el utilizado por la recursividad). ¿Cual es la complejidad del algoritmo?
#Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos ({C1, C2, D1, D2}). 
#Luego, pensar a partir de allí el caso de 8 elementos, etc… para encontrar el patrón.
def _alternar(arr, ini, fin):
    if fin - ini < 2:
        return arr
    medio = (ini+fin)//2
    arr = _alternar(arr, ini, medio)
    arr = _alternar(arr, medio+1, fin)
    for i in range(1, medio-ini+2, 2):
        arr[ini + i], arr[medio+i] = arr[medio+i], arr[ini + i]
    return arr
arr = ["c1", "c2", "c3", "d1", "d2", "d3"]
def alternar(arr):
    return _alternar(arr, 0, len(arr)-1)
# print(alternar(arr))

#***********************************************

# Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número 
# n, en tiempo O(logn). Por ejemplo, para 
# n=10 debe devolver 3, y para 
# n=25 debe devolver 5.
def cuadrado_mas_cercano(n):
    inicio, final = 0, n
    while inicio <= final:
        medio = (inicio+final)//2
        medio_cuadrado = medio**2
        if medio_cuadrado == n: #Encontre un numero al cuadrado igual a n
            return medio_cuadrado
        elif medio_cuadrado > n:
            final = medio -1
        else:
            inicio = medio + 1
            resultado = medio_cuadrado #Esta la posibilidad de que el cuadrado que busco sea este
    return resultado

#*****************************************

# Se realiza un torneo con n jugadores en el cual cada jugador juega con todos los otros n-1. 
# El resultado del partido solo permite la victoria o la derrota. 
# Se cuenta con los resultados almacenados en una matriz. 
# Queremos ordenar los jugadores como P1, P2, …, Pn tal que P1 le gana a P2, P2 le gana a P3, …, Pn-1 
# le gana a Pn (La relación “le gana a” no es transitiva). 
# Ejemplo: P1 le gana a P3, P2  le gana a P1 y P3 le gana a P2. Solución: [P1, P3, P2]. 
# Resolver por división y conquista con una complejidad no mayor a O(n log n).

# Se cuenta con un vector V de “n” elementos. Este vector visto de forma circular está ordenado. 
# Pero no necesariamente en la posición inicial se encuentra el elemento más pequeño. 
# Deseamos conocer la cantidad total de rotaciones que presenta “V”. 
# Ejemplo: V = [6, 7, 9, 2, 4, 5] se encuentra rotado en 3 posiciones. 
# Podemos hacerlo en tiempo O(n) por fuerza bruta. 
# Presentar una solución utilizando división y conquista que mejore esta complejidad.

# Una encuesta de internet pidió a personas que ordenen un conjunto de “n” películas 
# comenzando por las que más les gusta a las que menos. 
# Con los resultados quieren encontrar quienes comparten gustos entre sí. 
# Nos solicitan generar un algoritmo, que basándose en el concepto de inversión, 
# compare entre pares de personas y determine qué tan compatibles o incompatibles son. 
# Proponer un algoritmo utilizando división y conquista que lo resuelva.

# Dado “L” un listado ordenado de “n” elementos y un elemento “e” determinado. Deseamos conocer la cantidad total de veces que “e” se encuentra en “L”. 
# Podemos hacerlo en tiempo O(n) por fuerza bruta. 
# Presentar una solución utilizando división y conquista que mejore esta complejidad.