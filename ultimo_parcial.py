# Tenés una colección de n libros con diferentes espesores, que pueden estar entre 1 y n (valores no necesariamente
# enteros). Tu objetivo es guardar esos libros en la menor cantidad de cajas. Todas las cajas que disponés son de la
# misma capacidad L (se asegura que L ≥ n). Obviamente, no podés partir un libro para que vaya en múltiples cajas,
# pero sí podés poner múltiples libros en una misma caja, siempre y cuando no superen esa capacidad L. Implementar un
# algoritmo Greedy que obtenga la mínima cantidad de cajas a utilizar. Indicar y justificar la complejidad del algoritmo
# implementado. Justificar por qué se trata de un algoritmo greedy (no dar una respuesta genérica, sino aplicada a tu
# algoritmo). ¿El algoritmo propuesto encuentra siempre la solución óptima? Justificar.

def libros_de_mierda(L, libros):
    libros.sort(reverse=False)
    cajas = 1
    suma_parcial = 0
    for i  in range(0, len(libros)):
        if suma_parcial + libros[i] <= L:
            suma_parcial += libros[i]
        else:
            cajas += 1
            suma_parcial = libros[i]
    return cajas
#La complejidad del algoritmo es O(n + n * log(n)) ya que primero se ordena y después recorremos todo el arreglo haciendo verificaciones O(1).
# El algoritmo propuesto es greedy porque agarra el primer libro que mejor entre en la caja actual hasta poder guardar todos los libros y 
# obtener la cantidad minima de cajas totales.
# El algoritmo no es optimo ya que en el caso de L=7 y libros = [3,3,2,2,2,2], la solucion optima seria [3,2,2] y [3,2,2], es decir, 2 cajas, pero
# el algoritmo devolveria un total de 3 cajas por haber distribuido los libros de esta manera, [2,2,2], [2,3], [3] 


##########################################################################################################################
# Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que todo vértice de G
# pertenece a D o es adyacente a un vértice en D. El problema de decisión del set dominante implica, dado un grafo G y
# un número k, determinar si existe un set dominante de a lo sumo tamaño k.

# RESOLUCION 
# Como nos preguntaron también por el ejercicio 3, dejamos por acá un par de soluciones.

# En primer lugar, probamos que el problema se encuentra en NP: 
# dada una instancia del problema (grafo y valor de k) y una presunta solución, 
# validar dicha solución puede hacerse metiendo todos los vértices de la solución en un conjunto, 
# y también sus respectivos adyacentes, viendo que al final con ello estén todos los vértices del grafo 
# (comparar cantidades). Esto es O(V+E), siendo polinomial. 
# Validar que la solución es de tamaño <= k se hace en O(1) viendo la cantidad.
# Yendo a la reducción, podemos reducir vertex cover a este problema pensando en lo siguiente: 
# para vertex cover necesitamos que cada arista esté cubierta. 
# En dominating set cada vértice debe estar en el conjunto o ser adyacente a uno. 
# Eso quiere decir que tenemos que "forzar" que dominating set elija un vértice por cada arista (al menos),
# y eso sucede si metemos un nuevo vértice que sea únicamente adyacente a ambos de una arista. 
# Es decir, creamos un grafo nuevo con los mismos vértices y aristas del original, 
# agregando un vértice por cada arista original, conectándolos a los vértices que dicha arista une. 
# Entonces, si existe un dominating set de tamaño a lo sumo k, 
# necesariamente tiene que estar seleccionando un vértice por cada una de las aristas originales. 
# Si llegase a elegir un vértice de los agregados, 
# es porque daría lo mismo cuál de los dos extremos se debería elegir. 
# Al mismo tiempo, si no encuentra un dominating set de tamaño k, es porque no existe solución (no hubo forma de cubrir las aristas, básicamente).
# Notar que esta solución es análoga a la de Independent Set -> Path Selection.

##########################################################################################################################
# Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. Decidió en este caso robar
# toda una calle en un barrio privado, que tiene la particularidad de ser circular. Gracias a los trabajos de inteligencia
# realizados, sabemos cuánto se puede obtener por robar en cada casa. Podemos enumerar a la primer casa como la casa
# 0, de la cual podríamos obtener g0, la casa a su derecha es la 1, que nos daría g1, y así hasta llegar a la casa n − 1, que
# nos daría gn−1. Como la calle es circular, la casa 0 y la n − 1 son vecinas. El problema con el que cuenta el Lunático
# es que sabe de experiencias anteriores que, si roba en una casa, los vecinos directos se enterarían muy rápido. No le
# daría tiempo a luego intentar robarles a ellos. Es decir, para robar una casa debe prescindir de robarle a sus vecinos
# directos. El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. Dado
# que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema. Implementar un
# algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar, a
# partir de recibir un arreglo de las ganancias obtenibles. Para esto, escribir y describir la ecuación de recurrencia que
# correspondiente. Indicar y justificar la complejidad del algoritmo propuesto.

#Este problema se asemeja al juan del vago, donde la ecuacion de recurrencia llevaba a opt[i] = max(opt[i-1], opt[i-2] + casa[i])
#El tema es que nos da la condicion de que el barrio es circular, entonces no podria pasar que robo en la casa 0 y luego en la casa n-1, porque
#se enteraria el barrio
#Por eso la idea es buscar la ganancia maxima entre recorrer desde 0 a n-2 o  de 1 a n-1
#[10,12,5,8,9,2,4]
def juan_del_vago_ahora_ladron(casas):
    if len(casas) == 0:
        return []
    if len(casas) == 1:
        return [casas[0]]
    n = len(casas)
    

    ganancia1 = juan_del_vago_casa(casas, 0, n-2, n)
    ganancia2 = juan_del_vago_casa(casas, 1, n-1, n)
    return ganancia1[n-2] if ganancia1[n-2] > ganancia2[n-1] else ganancia2[n-1]


def juan_del_vago_casa(casas, inicio, fin, n):
    res = [0] * (n)

    res[inicio] = casas[inicio]
    res[inicio+1] = max(casas[inicio], casas[inicio+1])

    for i in range(inicio+2,fin+1):
        res[i] = max(res[i-1], res[i-2] + casas[i])
    return res


def main():
    # print(libros_de_mierda(7, [3,3,2,2,2,2]))
    print(juan_del_vago_ahora_ladron([10,12,5,8,9,2,4]))
main()
