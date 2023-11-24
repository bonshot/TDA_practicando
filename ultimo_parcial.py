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



def main():
    print(libros_de_mierda(7, [3,3,2,2,2,2]))

main()
