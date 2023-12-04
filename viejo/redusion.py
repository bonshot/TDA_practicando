#****************************************************************************************************************************

#3.Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados,
#utilizando programación dinámica. Indicar y justificar el orden del algoritmo implementado.
#Aclaración: siempre es posible escribir a n como suma de n términos de la forma 1**2, por lo que siempre existe solución.
#Sin embargo, la expresión 10 = 3**2 + 1**2
#es una manera más económica de escribirlo para n = 10, pues sólo tiene dostérminos. Además, tener en cuenta que no se piden los términos,
#sino la cantidad mínima de términos cuadráticosnecesaria.

#4. Realizar una reducción polinomial del problema del ejercicio 3 a otro de los vistos durante la cursada. Ayuda: pensar en
#alguno de los vistos de programación dinámica.

# Podemos reducir este problema al problema del cambio ya que usamos nuestra denominación o sistema monetario como los cuadrados de 1 a n para
# ver el que más se acerca a n, y así obtener la mínima cantidad de cuadrados necesarios en la suma hasta llegar a n.
# Reducción:
# Sea n y S = {1, 4, 9, 16, ..., n^2}. Queremos saber la cantidad mínima de cuadrados sumados que dan n. Entonces, creamos un sistema monetario
# con las denominaciones de S, si existe un cambio de n con las denominaciones de S, existe una suma de cuadrados que da n.

#Verificador
def cuadrados_minimizados2(n,s):
    cant = ["inf"] * (n+1)
    cant[0] = 0
    for i in range(1, n+1):
        minimo = i
        for cuadrado in s:
            if cuadrado > i:
                continue
            cantidad = 1 + cant[i-cuadrado]
            if cantidad < minimo:
                minimo = cantidad
        cant[i] = minimo
    return cant[n]

#******************************************************************************************************************************************
#El problema de elección de caminos (Path Selection) pregunta: dado un grafo dirigido G y un set de pedidos P1, P2, ..., Pc
#de caminos dentro de dicho grafo y un número k, ¿es posible seleccionar al menos k de esos caminos tales que ningún
#par de ellos compartan ningún nodo?
#Demostrar que Path Selection es un problema NP-Completo. Ayuda: este problema tiene mucha semejanza con
#Independent Set. Recomandamos reducir dicho problema a Path Selection.
# Drama-turgo, a tu dama la mas-turbo >8)

#p1-p2-p3-p1
#p6-p7-p3-p6


#primero demostramos que Path Selection es Np. Para eso vemos si la cantidad de caminos seleccionados
#sean al menos K. Y luego vemos que para cada par de caminos seleccionados, ver que no compartan nodo en comun.
#De esta manera se podria verificar en tiempo polinomial
# Reducción de Independent Set a Path Selection:
# Para reducir IS a PS me pego un tiro en la rodilla. No, mentira. Para reducir IS a PS, creamos un grafo G' con los mismos vértices que G,
# y creamos un camino de longitud 2 entre cada par de vértices de G'. Luego, creamos un set de pedidos P1...Pc, donde cada pedido es un camino
# de longitud 2. Por último creamos un k', que es el mismo que el k de IS. Si existe IS de tamaño K en G, entonces existe PS de K' en G'.
# Esta reducción es en tiempo polinomial y como ya sabiamos de antes que IS es NP-Completo, podemos confirmar que Path selecction
# tambien es NP-Completo
#**********************************************************************************

#... Modelo 01 de final ...
#Se requiere realizar un viaje a través de un territorio de difícil acceso.
#El mismo se encuentra dividido en zonas por las que se debe pasar.
#Existen m facciones que controlan algunas de esas zonas.
#Una facción puede controlar más de 1 zona y una zona puede ser controlada por más de una.
#Para poder realizar el viaje se debe pactar con alguna de estas.
#Cada pacto con una facción nos asegura el paso seguro por todas las zonas que controlan independientemente de si alguna de sus zonas son
#también controladas por otras facciones.
#Deseamos saber si es posible pactar con no más de k facciones para poder concretar el viaje de forma segura.
#Se pide: Demostrar que el problema es NP-Completo.
#HINT: Se puede utilizar Vertex Cover.

# Deseamos ver si podemos con una facción cubrir todas las zonas, entonces modelando con un grafo, cada facción es un vértice y las zonas son
# aristas, si existe un Vertex Cover, entonces existe un pacto con no más de K facciones para poder concretar el viaje. Para esto, reducimos
# Vertex Cover a este problema.
# Reducción:
# Creamos un G' con mismos vértices que G, creamos un vértice V, y conectamos con todos los de G', luego creamos un set de zonas Z, donde cada
# zona es una arista de G'. Luego un K'. Si existe VC de tam K en G, entonces existe pacto con no más de K' facciones para el viaje en G'.
# Reducimos VC a este problema en tiempo polinomial, y sabemos que VC es NP-C, entonces este problema también lo es.

#**********************************************************************************

#4) La siguiente es una versión de Independet Set.
#Dado un grafo G= (V, E) y un entero k,
#decimos que I ⊆ V es fuertemente independiente si dados dos vértices u y v en I,
#la arista (v, u) no pertenece a E y además no hay ningún camino de tamaño 2 (con dos aristas) de u a v.
#El problema de Strongly Independent Sets consiste en decidir si G tiene un conjunto fuertemente independiente de tamaño al menos k.
#Probar que el problema de Strongly Independent Sets es NP completo (y para eso usar que Independent Set es NP completo).

#primero demostramos que SIS es NP, para verificar la solución en tiempo polinomial, vemos si la cantidad de vértices en el conjunto
# es K, y vemos que entre cada par de vértices no haya un camino de tamaño 2. Esto es una operación polinomial (O(n^2)).

# Reducción de IS a SIS:
# Nos pegan un tiro en las pelotas, pero bueno, lo hacemos igual porque sino voy a desaprobar. Creamos un grafo G' con los mismos blablabla
# Creamos un set de pedidos P1...Pc, donde cada pedido es un camino con long 2. Creamos K'. Si existe IS de tam K en G, entonces existe SIS
# de tam K' en G'. La reducción es en tiempo polinomial y como sabemos que IS es NP-C, entonces SIS también lo es.

#**********************************************************************************

#Un instituto de enseñanza debe coordinar las fechas de exámenes finales de sus respectivos cursos. En cada curso se anotaron
#varios alumnos. Y un alumno puede estar en varios cursos. En total se cuenta con “k” fechas posibles de examen. Se desea generar un
#procedimiento eficiente para decidir si es posible cumplir con ese requerimiento. En caso afirmativo, dar una posible asignación de
#exámenes por fecha. Se pide: Demostrar que el problema es NP-Completo.
#HINT: Se puede utilizar K-coloreo de grafos.

#

#**********************************************************************************

# Se cuenta con un conjunto de porongas de distintos tamaños. Queremos saber si es posible armar un conjunto de porongas que
# sumen exactamente un número dado de tamaño total. Demostrar que este problema es NP-Completo.
# HINT: Se puede usar Subset Sum.


#**********************************************************************************

# La organización de un workshop internacional debe coordinar las
#fechas de paneles de exposición. En cada panel se presentan un
#conjunto de oradores. Un orador puede estar en varios paneles. Se
#cuenta con un total “j” jornadas diferentes donde se pueden
#establecer paneles. Se desea generar un procedimiento eficiente
#para decidir si es posible cumplir con cumplir con todos los
#paneles con todos sus oradores. En caso afirmativo, dar una
#posible asignación de paneles por jornada.
#Se pide: Demostrar que el problema es NP-Completo.
#HINT: Se puede utilizar K-coloreo de grafos.


#*******************************************************************************************************************
#4. Carlos tiene un problema: sus 5 hijos no se soportan. Esto es a tal punto, que ni siquiera están dispuestos a caminar
#juntos para ir a la escuela. Incluso más: ¡tampoco quieren pasar por una cuadra por la que haya pasado alguno de sus
#hermanos! Sólo aceptan pasar por las esquinas, si es que algún otro pasó por allí. Por suerte, tanto la casa como la
#escuela quedan en esquinas, pero no está seguro si es posible enviar a sus 5 hijos a la misma escuela. Utilizando lo visto
#en la materia, formular este problema y resolverlo. Indicar y justificar la complejidad del algoritmo.

#5. Demostrar si la siguiente afirmación es verdadera o falsa: “P es igual a NP”. Nah, mentira.
#Definir la relación entre la dificultad entre el problema del ejercicio 4 con el problema de obtener el corte mínimo en una
#red de transporte. ¿Se puede concluir si alguno de estos problemas es NP-Completo, o que no lo sea? ¿Estos problemas
#pertenecen a PSPACE? Justificar adecuadamente cada respuesta.

#5) Ninguno es NP-Completo, el primero se resuelve con una red de flujo y el segundo es un algoritmo de flujo máximo en una red.
# Ambos problemas pertenecen a PSPACE ya que se resuelven de manera polinomial con un tamaño en memoria proporcional al tamaño de la entrada
# es decir, lineal.

# ************************************************************************************
# 5) Para un evento a realizar se requiere conformar una selección
# musical entre el conjunto A de “n” canciones. Podemos enumerar a
# los elementos de A como a1,a2,...,an. Por otra parte, contamos con
# un conjunto “B” de “m” personas. Cada una de ellas con un subsets
# de esas canciones que le gustan. Deseamos saber si podemos
# seleccionar un subconjunto de no más de “k” canciones, de tal
# forma que existe al menos 1 canción que le gusta a cada uno.
# Se pide: Demostrar que el problema es NP-Completo.

# HINT: Se puede utilizar Vertex Cover.

#1)El problema es claramente de verificacion en tiempo polinomial, ya que podemos 
# verificar rapidamente si un subconjunto de canciones satisface la condicion de que 
# hayaa al menos una cancion que le guste a cada persona en B. Por eso, dado un subconjunto 
# de canciones, simplemente verificamos si para cada persona en B hay almenos una cancion
# en el subconjunto que le gusta. Esta verificacion nos confirmaria que el problema es NP
def verificador(conjunto_B, conjunto_A, solucion, k):
    if len(solucion) > k:
        return False
    for persona in conjunto_B:
        le_gusta = False
        for cancion in solucion:
            if cancion in conjunto_A[persona]:
                le_gusta = True
                break
        if not le_gusta:
            return False
    return True

#2)Ahora para reducir Vertex cover al problema de seleccion musical, creamos un 
# Grafo G, su conjunto de vertices V y su conjunto de aristas E,
# construimos una instancia equivalente del problema:
# Construccion de A: asociamos cada vertice i de V con una cancion unica Ai en A
# Construccion de B: asociamos cada arista (i,j) de E con una persona unica en Bj en B
# K' = K de Vertex Cover
# Relación entre los Problemas:
# La clave para la reducción es establecer una relación entre la existencia de un Vertex Cover de tamaño
# k′ en G y la existencia de un subconjunto de canciones de tamaño k′que le guste a cada persona en B.
# *Si existe un Vertex Cover S de tamaño k′ en G, entonces podemos tomar las canciones asociadas a los vértices en S como el subconjunto de canciones en 
# A, y cada persona en B tendrá al menos una canción de ese subconjunto.
#           *Dado que S es un Vertex Cover, cada arista (i,j) en E debe tener al menos uno de sus extremos en S.
#           *Si tomamos las canciones asociadas a los vértices en S como el subconjunto de canciones en A, 
#           entonces cada arista (i,j) estará representada por al menos una canción en el subconjunto.
#           *Por lo tanto, cada persona Bij en B (asociada a la arista (i,j)) tendrá al menos una canción en el subconjunto que le gusta.
# # *Si no existe un Vertex Cover S de tamaño k′ en G, entonces no hay suficientes vértices para cubrir todas las aristas, 
# # lo que significa que hay al menos una arista sin ninguno de sus extremos en S. Entonces, no podemos encontrar un subconjunto de canciones en 
# # A que le guste a cada persona en B.
#         *Si S no es un Vertex Cover, significa que hay al menos una arista (i,j) en E tal que ambos extremos 
#         i y j no están en S.

#         *Esto implica que no hay una canción asociada a i o j en el subconjunto de canciones A. 
#         Por lo tanto, no podemos construir un subconjunto de canciones en A que satisfaga la condición de que cada persona en 
#         B tenga al menos una canción que le guste.
# Reducción: Si existe un conjunto de vertices de tamaño K que cubre todas las 
# aristas en G, entonces existe un subconjunto de canciones de tamaño K' que le gusta a cada persona en B.
# Por lo tanto, el problema de selección musical es NP-Completo.

# ***********************************
# El proyecto de colonización de Marte lleva años desarrollándose en
# secreto. En una nueva etapa se requieren N granjeros-espaciales
# para terraformar una hectárea del suelo marciano. Se realizó una
# amplia búsqueda de candidatos “r” (r>>n), siendo todos ellos
# capaces. Dadas las duras condiciones que enfrentarán, es
# primordial que sean compatibles entre ellos. Se realizaron
# complejos estudios psicológicos y se construyó una tabla donde
# para cada granjero se indica con cuáles otros puede trabajar sin
# conflictos. En este momento quieren saber si los candidatos
# disponibles pueden armar la tripulación necesaria.
# Demuestre que lo solicitado es NP-COMPLETO

# HINT!: Tal vez le resulte útil clique

# 1)El problema se puede verificar en tiempo polinomial. Dado un conjunto r de granjeros
# me fijo si existe n granjeros espaciales. Para eso, me fijo cada granjero, y voy viendo
# si tiene relacion con todo el resto de granjeros, hasta llegar a conseguir un conjunto de n granjeros
# que almenos conozcan a uno de ese conjunto elegido.

def verificador_grafo_completo(conexiones, granjeros, n):
    if len(granjeros) > n:
        return False
    for granjero in granjeros:
        for granjero2 in granjeros:
            if granjero != granjero2 and (granjero, granjero2) not in conexiones:
                    return False
    return True

# 2) Ahora para reducir Clique al problema de los granjeros espaciales, 
# creamos un Grafo G, su conjunto de vertices V y su conjunto de aristas E.
# Construimos una instancia equivalente del problema:
# Construccion de R: asociamos cada i de V con un granjero unico Ri en R
# Construccion de Relacion: asociamos cada arista (i,j) de E con una relacion entre dos 
# granjeros
# Tamaño de granjeros necesario = N de igual tamaño del clique deseado
# Reducción: Si existe un clique de tamaño N en G, entonces existe un conjunto de granjeros
# de tamaño N que pueden trabajar sin conflictos. Por lo que el problema de granjeros espaciales
# es PENE-Completo.

#***********************************************
#5. En el reino de Gondor ha incrementado enormemente la delincuencia luego de su urbanización. El rey Aragorn no
#quiere que todo su esfuerzo en construir calles resulte en vano, por lo que quiere poner guardianes a vigilar las calles por
#las noches. El problema es que cuesta mucho dinero entrenar a dichos guardianes, por lo que quiere reducir al mínimo
#la cantidad que sean necesarios entrenar. Sabe que cada guardian puede estar vigilando desde una esquina, y desde allí
#tener visibilidad hasta cualquier otra esquina directa. Necesita determinar la cantidad mínima de guardianes que son
#necesarios para cubrir todas las calles de su reino. Como primera medida, consulta con el oráculo Alumnus Teorius
#Algoritmus (es decir, quien lee esta consigna), para determinar si esto es conseguible en corto tiempo (el oráculo le
#pregunó algo sobre tiempo polinomial, que Aragorn no entendió y le dijo “si, eso”).
#Tenemos que explicarle a Aragorn que este pedido no es realizable (y debe armarse de paciencia, o no buscar el mínimo
#exacto), porque el problema de Guardianes de Gondor es, en realidad, un problema NP-Completo (en su versión de
#problema de decisión: “¿Se pueden vigilar todas las calles con esta topología con máximo K guardianes?”).

#1) Podemos verificar en tiempo polinomial si es posible vigilar todas las calles con K guardianes. Vemos tener K guardianes
#   luego vemos si cada calle tiene almenos un guardia vigilandola. Para esto basta con recorrer el arreglo de calles y 
#   ver que tenga uno de sus extremos en la solución propuesta. Esto es O(n). Por lo tanto es NP

#2) Sabemos que este problema se asemeja al vertex cover y es np completo
# Pero a nosotros nos importa sacar que el problema de los guardianes es Np-Completo,
# por lo tanto vamos a reducir un problema np-completo a uno que momentaneamente es np,
# para confirmar que si el problema de guardianes es np-completo
#Para eso creamos un grafo G, su conjunto de vertices V y su conjunto de aristas E.
# Construimos una instancia equivalente del problema antes de usar el problema de los guardianes.
# Construccion de Esquinas: asociamos cada i de V como una esquina i en esquinas
# Construccion de calles: asociamos cada arista (i,j) de E con una calle unica
# Tamaño de esquinas elegidas = N de igual tamaño de vertices para que un grafo sea vertex cover
#Reduccion: Si existe un vertex cover de tamaño N en G, entonces existe un conjunto de esquinas elegidas
# de tamaño N para que se puedan cubrir todas las calles. Por lo que el problema de los guardianes 
# es NP-Completo. 

#**************************************************************************
# El problema de elección de caminos (Path Selection) pregunta: dado un grafo dirigido G y un set de pedidos P1, P2, ..., Pc
# de caminos dentro de dicho grafo y un número k, ¿es posible seleccionar al menos k de esos caminos tales que ningún
# par de ellos compartan ningún nodo?
# Demostrar que Path Selection es un problema NP-Completo. Ayuda: este problema tiene mucha semejanza con
# Independent Set. Recomandamos reducir dicho problema a Path Selection.

#Para demostrar que Path selection es NP-Completo, primero tenemos que demostrar que es NP y luego reducir un problema
#Np-completo al problema de Path Selection

# Verificamos que sea NP
# Para esto nos fijamos en los caminos pedidos, ponemos un un set, múltiples sets de vértices por los que pasan estos pedidos
# , luego nos fijamos si el nodo fue visitado, si estaba visitado entonces no es una solución válida, pero si no podemos continuar
# , al terminar la ejecución si ningún nodo estaba en "visitados" para un nuevo pedido, entonces es válida. Esto es en tiempo lineal
# ya que debemos únicamente pasar por todos los pedidos verificando todos sus componentes con comparaciones lineales contra el set
# de visitados. O(L) donde L es la suma de los vértices ocupados por los pedidos, en el peor de los casos los pedidos abarcan todos los 
# vértices del grafo ---> O(V)

# Reducimos Independent Set a Path Selection para demostrar por relación que Path Selection es NP-Completo
# Ahora, asumamos que tenemos un grafo no dirigido G y un K para una instancia de problema problema de IS.
# Queremos construir un grafo dirigido G y un conjunto de caminos P1, P2...Pc
# La construccion sera la siguiente:
# Creo un grafo G' y un K' que es igual K de la instancia de IS, donde en mi G' quiero unir aquellos vértices de G
# que comparten un mismo adyacente, los pedidos serán los caminos que unen a los vértices de G' que comparten un adyacente
# entonces si compartirmos un adyacente en G, entonces tenemos un camino en G' que une a los vértices que comparten el adyacente.
# De esta forma Path Selection se ve obligado a elegir un camino de cada par de vértices que comparten un adyacente, y como K' es igual
# a K, entonces debe elegir K caminos de los pedidos (estos son los caminos posibles que unen a los vértices mencionados).
# Si tengo 2 vértices unidos por la razón mencionada, entonces hay 2 caminos posibles entre esos vértices (El que va por la adyacencia
# y el directo), por lo que para poder encontrar un PS de tamaño K' se deberá tomar uno solo de esos
# Si existe IS de tamaño K en G, entonces existe PS de tamaño K' en G'. Por lo que Path Selection es NP-Completo (IS <p PS)

