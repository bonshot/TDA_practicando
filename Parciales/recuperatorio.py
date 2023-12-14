# 1. Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un
# mínimo Vertex Cover del mismo.

# 2. Dado un arreglo de n enteros, encontrar el subarreglo contiguo de máxima suma, utilizando División y Conquista.
# Indicar y justificar la complejidad del algoritmo.

# 3. Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar de 0 a K, siendo que las operaciones
# posibles son: (i) aumentar el valor del operando en 1; (ii) duplicar el valor del operando.
# Implementar un algoritmo que, por programación dinámica obtenga la menor cantidad de operaciones a realizar (y
# cómo son dichas operaciones). Desarrollar la ecuación de recurrencia. Indicar y justificar la complejidad del algoritmo
# implementado.

def operaciones(K):
    cant = [float('inf')] * (K + 1)
    cant[0] = 0

    for i in range(1, K + 1):
        cant[i] = min(cant[i], cant[i - 1] + 1)
        if i % 2 == 0:
            cant[i] = min(cant[i], cant[i // 2] + 1)
    i = K
    operaciones = []
    while i >0:
        operaciones.append(i)
        if i % 2 == 0 and cant[i//2] == cant[i] -1:
            i//=2
        i-=1
    return operaciones[::-1]
# print(operaciones(10))
#La complejidad del algoritmo o(k), donde K es el valor al que queremos llegar
#por el ciclo anido que recorre de 1 hasta K inclusive viendo que operacion usar
#y luego pasa lo mismo en la reconstruccion de la solucion


# 4. El problema de selección de caminos (Path Selection) pregunta: dado un grafo dirigido G y un set de pedidos P1, P2, ..., Pc
# de caminos dentro de dicho grafo y un número k, ¿es posible seleccionar al menos k de esos caminos tales que ningún
# par de ellos compartan ningún nodo?
# Path Selection es un problema NP-Completo. Ahora bien, queremos demostrar nuevamente (pero de otra forma a la
# vista en clase) que Independent Set es un problema NP-Completo. Demostrar que Independent Set es un problema
# NP-Completo, utilizando Path Selection para esto.

# 5. Trabajamos para el mafioso Arnook, que es quien tiene la máxima influencia y poder en la ciudad costera de Ciudad
# República. Allí reina el caos y la delincuencia, a tal punto que quien termina organizando las pequeñas mafias locales
# no es otro sino Arnook. En particular, nos vamos a centrar en unos pedidos que recibe de parte de dichos grupos por el
# control de diferentes kilómetros de la ruta costera. Cada pequeña mafia le pide a Arnook control sobre un rango de
# kilómetros (por ejemplo, la mafia nro 1 le pide del kilómetro 1 al 5, la mafia 2 le pide del 3 al 8, etc. . . ). Si hay una
# mafia tomando control de algún determinado kilómetro, no puede haber otra haciendo lo mismo (es decir, no pueden
# solaparse). Cada mafia pide por un rango específico. Arnook no cobra por kilómetraje sino por “otorgar el permiso”,
# indistintamente de los kilómetros pedidos. Ahora bien, esto es una mafia, no una ONG, y no debe rendir cuentas con
# nadie, así lo único que le interesa es maximizar la cantidad de permisos otorgados (asegurándose de no otorgarle algún
# lugar a dos mafias diferentes). Implementar un algoritmo Greedy que reciba los rangos de kilómetros pedidos por cada
# mafia, y determine a cuáles se les otorgará control, de forma que no hayan dos mafias ocupando mismo territorio, y a su
# vez maximizando la cantidad de pedidos otorgados. Indicar y justificar la complejidad del algoritmo implementado.
# Justificar por qué el algoritmo planteado es Greedy. ¿El algoritmo da la solución óptima siempre?

def problema_mafias(zonas):
    zonas.sort(key=lambda x: x[1])
    print(zonas)
    orden = []
    for zona in zonas:
        if len(orden) == 0 or not hay_intersection(orden[-1], zona):
            orden.append(zona)
    return orden

def hay_intersection(anterior, actual):
    if anterior[1] > actual[0]:
        return True
    return False
print(problema_mafias([(0,10), (11, 60), (15,19), (20,80)]))
# Este algoritmo es Greedy porque en cada paso toma la decisión óptima localmente, eligiendo la mafia que menor diferencia con el anterior hay sin superponerse con la anterior.
# Asi hasta obtener la mayor cantidad mafias cubriendo el territorio y asi arnook obtendria mayor ganancia 
# No reconsidera sus decisiones anteriores, lo que es característico de los algoritmos Greedy.
# Casos en los que el Algoritmo no es Óptimo:
#     Mafias con Rangos Desiguales:
#         Si una mafia con un rango más pequeño puede permitir que otras mafias ocupen territorios adicionales, el algoritmo Greedy puede no seleccionar la combinación óptima.
#     Mafias con Prioridades Estratégicas:
#         Si algunas mafias son estratégicamente más importantes que otras y deberían tener prioridad, el algoritmo Greedy no considerará esta información y podría suboptimizar la asignación.
#     Cambios Dinámicos:
#         Si las condiciones cambian dinámicamente y la estrategia óptima varía con el tiempo, el enfoque Greedy inicial puede no adaptarse de manera óptima a estos cambios.