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

# A este problema lo podemos reducir a Vertex Cover, ya que la idea es que los vértices sean los guardianes y
# las aristas sean las calles, entonces si un vértice está en el vertex cover, significa que ese guardián puede ver
# todas las calles que conectan a ese vértice, si no está en el vertex cover no. Entonces si el vertex cover
# es de tamaño K, podemos ver con K guardianes todas las calles. Ahora, el problema de Vertex Cover es NP-Completo,
# si logramos reducir el problema Vertex Cover al de los Guardianes, entonces el de los guardianes será NP-Completo.
# Reducción:
# Sea G = (V, E) un grafo, y K un entero. Queremos saber si existe un Vertex Cover de tamaño K. Entonces, creamos
# un grafo G' con mismos vértices y aristas que G, luego agregamos un vértice v a G' y lo conectamos con todos los
# vértices de G. Si existe un Vertex Cover de K vértices en G, entonces existe un VC de K+1 vértices en G'.
# Si pasa esto, entonces existe un VC de K vértices en G, por lo que reduje Vertex Cover a Guardianes de Gondor.
# Con esto Guardianes de Gondor es NP-Completo. Culo

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

# Este problema es NP ya que podemos recorrer el grafo de cursos viendo si sus cursos adyacentes (cursos que comparten alumnos)
# comparten una misma fecha de final. Esto lo haria O(V+E) ya que hacemos BFS.

# Los vértices son los cursos (que van a la fecha de color X) y las aristas son los alumnos en común que tienen los cursos. Si existe
# un k-coloreo, entonces existe una posible asignación de exámenes por fecha. Para esto reducimos k-coloreo a este problema. De esa forma
# podemos ver que este problema es NP-C.
# Entonces a la "caja negra" de este problema le metemos un arreglo de colores que son las fechas y un grafo que es el de los cursos para
# ver si existe una posible asignación tal que los "colores" (fechas) que le pasamos
# no se choquen entre sí. Si existe una posible asignación, entonces existe un k-coloreo, y por ende el problema es NP-C.

#**********************************************************************************

# Se cuenta con un conjunto de porongas de distintos tamaños. Queremos saber si es posible armar un conjunto de porongas que
# sumen exactamente un número dado de tamaño total. Demostrar que este problema es NP-Completo.
# HINT: Se puede usar Subset Sum.

# Este problema es NP ya que podemos recorrer el arreglo de porongas viendo si la suma de porongas es igual al tamaño total y corroborar que
# los subconjuntos de porongas que nos da, son las correctas ---> O(n).

# Reducción de Subset Sum a este problema:
# Creamos un set de porongas P, donde cada poronga es un número. Creamos un T total. Si existe un subconjunto de porongas que sumen T
# entonces existe un Subset Sum de T en P. La reducción es en tiempo polinomial y como SS es NP-C, entonces este problema también lo es.

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

#Este problema es Np ya que podemos recorrer el grafo de paneles y ver que los paneles adyacentes (que comparten oradores)
#no tengan la misma fecha de presentacion. Seria O(V+E) ya que hacemos BFS

# Queremos demostrar que este problema es NP-C, para eso reducimos K-Coloreo a este problema (por transitividad).
# Reducción:
# Tenemos un conjunto de paneles, un conjunto de oradores y un j' de jornadas. Llamamos a K-Paneles con estos parametros y de esta manera obtenemos
# si es posible asignar a todos los paneles por jornada. De esta manera, podemos afirmar que si tenemos un K-paneles con paneles, oradores y J', podemos tener
# un K-colores con V y E y un K. De esta manera podemos concluir que K-Paneles es NP-C
#   K-Coloreo <=p K-paneles

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


# Para demostrar que este problema es NP-Completo, primero tenemos que demostrar que sea NP
#  y luego mostrar que un problema NP-completo, sea reducible a este problema.

# 1)Para eso primero podemos crear un certificador polinomial,
# tomamos del problema, el conjunto de personas y el k conjunto de canciones y la solucion esperada.
# Para eso realizamos un bfs y vamos agregando las aristas (el nombre de la persona) a visitados, 
# y chequeamos que el largo de set de visitados (personas diferentes encontradas en aristas del grafo)
# sea el largo del conjunto de personas totales. O(V + E) = O(m + n) = O(n) siendo polinomial.

# 2) Para reducir vertex cover a este problema tenemos que pensar lo siguiente:
# En 

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

# 1)Primero buscamos un certificador polinomial. Dado Los candidatos y N,
# verificamos que el subconjunto de granjeros-espaciales elegidos sean N por lo menos.

# 2) Creamos un Grafo (V,E) y creamos un N con un valor similar al del K deseado, utilizamos
#    la "caja negra" de este problema y vemos si existe un conjunto de granjeros que sean compatibles entre todos
#    y que sean por lo menos N. Si existe, entonces existe un clique de tamaño N en G, y por ende el problema es NP-C

#***********************************************
