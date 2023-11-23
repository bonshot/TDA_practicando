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
def main():
    print(libros_de_mierda(7, [3,3,2,2,2,2]))

main()
