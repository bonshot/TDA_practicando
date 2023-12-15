# Un almacén registra en una matriz qué productos compra cada uno de sus clientes. 
# Un conjunto de clientes es diverso si cada uno de ellos compra cosas diferentes (tiene intersección vacía con lo que compran los demás). 
# Definimos al problema de los clientes diversos como: Dada una matriz de registro, de tamaño m (clientes) x n (productos), y un número k<=m, 
# ¿existe un subconjunto de tamaño al menos k de los clientes que sea diverso? 
# Probar que el problema es NP-completo. Sugerencia: Reducir polinomialmente conjuntos independientes a clientes diversos.

# Primero demostramos que el problema de clientes diversos es NP
# Dado un conjunto de clientes que afirman ser diversos, podemos verificar facilmente
# en tiempo polinomial si son realmente diversos. Necesitamos comprar si los productos
# comprados por cada de cliente en el conjunto para asegurarno que nadie coincida con algun
# producto comprado. De esta manera, sabremos si son diversos o no y eso seria NP

# Ahora para demostrar que el problema es NP-completo, reduciremos IS al problema de clientes
# diversos

# Dado un grafo G y un numero K, contruimos una matriz de registro A y un numero K' tal que
# exista un IS de al menos K nodos si solo si existe un subconjunto de tamaño almenos K' 
# de clientes diversos

# TRANSFORMACION:
# Construccion de la matriz A: Cada nodo en G se asocia con un cliente en A y cada columna
# de este cliente representa un elemento en U. Si un nodo esta en IS, entonces marcamos con 1
# las columnas correspondientes en la fila asociada al cliente
# K clientes: asociamos el k nodos como el K' minimo clientes adversos

# *Si existe un IS de almenos K nodos G, existe un subconjunto de tamaño K' clientes en A
# que sea diverso. Cada cliente (nodo en G) del IS tiene una fila asociada en A que no
# comparte ninguna columna(elemento en U) con los demas clientes, lo que hace que el conjunto
# de clientes sea diversos
# *Si existe un subconjunto de K' clientes en A que sea diverso, entonces existe un IS de al menos
# K nodos en G. La diversidad implica que los nodos correspondientes en G no estan conectados entre
# Si

# Esta construccion es polinomica en el tamaño de la entrada original y podemos demostrar
# que el problema de clientes diversos  es NP-Completo
#ARREGLAR

#*************************************************************

# Nos piden que organicemos una jornada de apoyo de estudio para exámenes. Tenemos que poder dar apoyo a “n” materias y hemos recibido currículos de “m” postulantes para ser potenciales ayudantes. 
# Cada ayudante puede ayudar en un determinado subconjunto de materias. Para cada una de las materias hay un subconjunto de postulantes que pueden dar apoyo en ella. 
# La pregunta es: dado un número k < m, ¿es posible seleccionar a lo sumo “k” ayudantes de modo tal que siempre haya un ayudante que pueda dar consultas en alguna de las n materias? 
# Este problema se llama Contratación Eficiente. Probar que “Contratación Eficiente” es NP-completo. Sugerencia: se puede tratar de usar Cubrimiento de Vértices.


# Primero, demostraré que el problema de "Contratación Eficiente" es NP (en tiempo polinómico).

# Demostración de NP:
# Dado un conjunto de ayudantes candidatos S de tamaño k, podemos verificar en tiempo polinómico si 
# S satisface la condición de que siempre haya al menos un ayudante que pueda dar consultas en alguna de las 
# n materias. Para cada materia en M, verificamos si al menos un ayudante en S puede dar apoyo en esa materia. Si es así, entonces 
# S satisface la condición para todas las materias. Esta verificación se puede hacer en tiempo polinómico, por lo tanto, el problema es NP.

# Ahora, para demostrar que es NP-completo, haremos una reducción desde el problema conocido NP-completo "Cubrimiento de Vértices".
# Reducción a partir de "Cubrimiento de Vértices":
# Dado un grafo G y un número k, queremos construir una instancia del problema de "Contratación Eficiente".

# Cada vértice en G se corresponderá con un postulante en el conjunto de postulantes P para el problema de "Contratación Eficiente".
# Cada arista en G se corresponderá con una materia en el conjunto de materias M para el problema de "Contratación Eficiente".
# Para cada materia en M que está asociada con una arista en 
# G, el conjunto de postulantes que pueden dar apoyo en esa materia será precisamente los dos vértices conectados por la arista.
# Estableceremos k igual al número de vértices en G.

# Demostración de la Reducción:
# Si hay un conjunto de k vértices en G que cubre todas las aristas, entonces este conjunto de vértices se corresponde con un conjunto de 
# k postulantes en P que pueden dar consultas en todas las materias en M.
# Si hay un conjunto de k postulantes en P que pueden dar consultas en todas las materias en M, entonces este conjunto de postulantes se corresponde con un conjunto de 
# k vértices en G que cubre todas las aristas.
# La reducción es válida en ambos sentidos, lo que demuestra que el problema de "Contratación Eficiente" es NP-completo.
# En resumen, hemos demostrado que el problema es NP y que es NP-completo al reducirlo desde el problema de "Cubrimiento de Vértices".

#*************************************************************

# Se conoce Bin-Packing al problema de decisión donde se cuenta con “N” elementos de diferentes pesos y con “M” contenedores de cierta capacidad. 
# Queremos saber si es posible acomodar todos los elementos en no más de k contenedores. Se pide demostrar que el problema es NP-Completo. Sugerencia utilizar 2-partition.

# Para demostrar que el problema de Bin-Packing es NP, primero debemos mostrar que una solución propuesta puede ser verificada en tiempo polinómico.
# Dada una configuración de elementos en contenedores y un valor de k, podemos verificar en tiempo polinómico si todos los elementos están acomodados en no más de k contenedores y si la capacidad de cada contenedor no se excede. Por lo tanto, el problema de Bin-Packing es NP.
# Ahora, para demostrar que Bin-Packing es NP-completo, utilizaremos la reducción desde el problema NP-completo 2-partition.

# 1. Problema 2-partition:
# Dado un conjunto de números enteros positivos 
# a1,a2,...,an, ¿es posible dividirlos en dos subconjuntos de igual suma?

# 2. Reducción a Bin-Packing:
# Dado una instancia del problema 2-partition, donde tenemos 
# n números enteros positivos, vamos a construir una instancia equivalente del problema de Bin-Packing.
# Para cada número ai en el conjunto, creamos un elemento de peso ai. Además, establecemos 
# k=2 (queremos acomodar los elementos en dos contenedores).

# La capacidad de cada contenedor en el problema de Bin-Packing será la mitad de la suma de todos los números en la instancia original de 2-partition.
# 3. Demostración:
# Si la instancia original de 2-partition tiene una solución (los números pueden dividirse en dos subconjuntos de igual suma), entonces podemos colocar esos elementos en dos contenedores en el problema de Bin-Packing, cumpliendo con la capacidad de cada contenedor.
# Si el problema de Bin-Packing tiene una solución (podemos acomodar los elementos en dos contenedores), entonces la suma de los elementos en cada contenedor debe ser igual a la capacidad del contenedor. Esto implica que hemos encontrado una partición de los números originales en dos subconjuntos de igual suma.
# Esta reducción demuestra que el problema de Bin-Packing es NP-completo, ya que hemos reducido un problema NP-completo (2-partition) a Bin-Packing en tiempo polinómico. Por lo tanto, Bin-Packing es NP-completo.

#*************************************************************

# Definimos el problema del Hitting Set como: dado un conjunto finito S de “n” elementos, una colección C de subconjuntos de S, un número positivo K ≤ n, 
# ¿existe un subconjunto S’ ⊆ S tal que S’ contiene al menos un elemento de cada subconjunto de C y |S’| ≤ K? Demostrar que este problema es NP-Completo. Sugerencia: utilizar Vertex Cover.

#Para demostrar que el problema del Hitting Set es NP, primero debemos demostrar que un certificado
# de solucion se puede verificar en tiempo polinomial.
#Dado un conjunto finito S, una coleccion C de subconjuntos de S, y un numero positivo K <= n,
#un certificador seria un subconjunto S' de S tal que |S'| <= K y S' contiene al menos un
#elemento de cada subconjunto en C.

#La verificaciond e la solucion se puede hacer en tiempo polinomial, ya que simplemente
#se necesita verficar si S' tiene un tamaño menor o igual a K  y si contiene al menos un elemento
#de cada subconjunto en C. Ambos pasos pueden hacerse en tiempo O(n) donde n es el tamaño de S.

#Reduccion:
#Construimos la instancia de HS:
#Conjunto S: Asignamos el conjunto de vertices V de G como nuestro conjunto S en hitting set
#Colleccion C: para cada arista(u,v) en E, creamos un conjunto en C que contiene los vertices
#u y v. Asi, C es una coleccion de conjuntos, cada uno corresponde a una arista en E
#Numero K: Tomamos K como el tamaño deseado del vertex cover

#Si existe un vertex Cover de tamaño K en G, podemos seleccionar los K elementos correspondientes
# en S para formar un conjunto S'. Este conjunto S' tendra al menos un elemento de cada conjunto
#en C
#Si existe un conjunto S' en hitting Set, que contiene almenos un elemento de cada conjunto en C,
#entonces estos elementos en S' forman un vertex cover de tamaño K en G

#La reduccion establece una correspondencia entre las soluciones de VC y las soluciones de hitting set.
#Existe un vertex cover de almenos K vertices si y solo si existe un conjunto S' de almenos K elementos
#pertenecientes a la colleccion C.

#*************************************************************

# Un país está modificando su red radiofónica. 
# Existen muchas estaciones de radios cada una con su propia frecuencia de transmisión. 
# Desean reasignarlas de tal forma de no usar más de N frecuencias. El problema es que ciertas radios por su ubicación geográfica y potencia pueden interferir con otras. 
# Un estudio informa cuántas radios hay, y para cada radio con cuáles hay riesgo de interferencia. Quisieran determinar si es posible realizar la reasignación. 
# Demuestre que el problema planteado es NP-COMPLETO. HINT!: Tal vez le resulte útil coloreo de grafos.

#Demostracion que pertenece a NP:
#Dado un conjunto de frecuencias de radio asignadas a las estaciones actuales,
#Podemos verificar en tiempo polinomial si la asignacion propuesta
#satisface todas las restricciones de interferencia. Solo necesitamos verificar que ninguna
#estacion interfiera con otra asignada a la misma frecuencia. La verificacion de esta condicion
#se puede realizar en tiempo polinomial, lo que demuestra que el problema esta en NP.
#La complejidad seria O(n), donde n es el tamaño del conjunto de estaciones de radio

#Reduccion de coloreo a reasignacion de frecuencias de radio:
#Dado un grafo = (V,E), donde V es el conjunto de vertices y E es el conjunto de aristas, 
#queremos colorear los vertices de manera que ningun par de vertices adyacentes tenga el mismo color.
#Transformaremos este problema de coloreo de grafos en un problema de reasignacion de frecuencias
#de radio

#Estaciones de radio:Asociaremos cada vertice v en G con una estacion de radio.
#Frecuencias de transmision: Asociaremos cada color en el problema de coloreo de grafos con una 
#frecuencia de transmision
#Interferencia:Habra una interferencia entre dos estaciones si y solo si los vertices correspondientes
#en el grafo son adyacentes

#Si dos vertices estan concetados por una arista en el grafo original, las estaciones de radios
#intereferiran entre si
#Si se puede asignar a dos estaciones de radio que interfieren entre si con frecuencias diferentes,
#podemos colorear dos vertices adyacentes con colores distintos

#Por lo tanto, existe un coloreo de grafos si y solo si existe una solucion para el problema de radios
#de esta manera se puede comprobar que el problema es NP-completo

#*************************************************************

# Un departamento dentro de una universidad adquirió “n” proyectores para dar clases durante el cuatrimestre. 
# Envió un formulario a los docentes de las distintas materias para conocer si los necesitaban como complemento para sus clases. 
# Un subconjunto de docentes respondió afirmativamente. Sabiendo que cada materia tiene clases 1 o más veces por semana en un horario establecido. 
# Y sabiendo que los horarios de varias de esas materias se superponen. Nos solicitan determinar si la cantidad comprada alcanza o si se tiene que dejar a docentes sin acceso a esas cuentas. 
# Demostrar que lo solicitado es NP-COMPLETO. Sugerencia: Tal vez le resulte útil “k” coloreo de grafos.

#Para demostrar que es Np, basta con crear un certificador en tiempo polinomial, ya que podemos
#verificar que para cada par de docentes que se superpongan sus clases, que se les pueda asignar distintos proyector
#de esta manera podremos comprobar que se puede asignar n proyectores de tal que no se superpongan entre clases
#Esta verificacion tiene complejidad O(n) donde n es la cantidad de profesores

#Ahora para comprobar que el problema es Np-completo, creamos una instancia del problema 
#Cada vertice del grafo G se asociara como un docente
#Cada color en K-coloreo se asociara con un proyector
#Cada conexion entre dos vertices en el grafo se asociara a docentes que tienen clases que se 
#superponen

#La idea es que si podemos asignar proyector a los docentes de manera que no haya superposicion de horarios,
#entonces podemos K-colorear el grafo original sin asignar el mismo color a vertices adyacentes. 
#del mismo modo, si podemo K colorear el grafo, entonces podemos asignar proyector a los docentes de manera
#que noh aya superposicion

#esta reduccion se peude hacer en tiempo polinomico, ya que estamos creando una instancia de nuyestro problema
#para cada instancia del problema de k-coloreo y viceversa.

#Por lo tanto, existe k-coloreo de un grafo si y solo existe una solucion al problema de n-proyectores

#*************************************************************

# Para elaborar una película de detectives un grupo de escritores se ha juntado para elaborar una trama atrapante y que tenga coherencia. 
# En largas jornadas han propuesto un gran conjunto de premisas, giros argumentales y eventos claves. Lamentablemente algunas de ellas no son compatibles entre sí. 
# Por cada situación han anotado con cual no es compatible. Desean poder seleccionar un conjunto de N premisas compatibles para presentar a los productores como idea inicial. 
# Se pide: Demostrar que el problema es NP-Completo. Sugerencia:  Tal vez le resulte útil clique

#Para demostrar que el problema es NP, necesitamos mostrar que dada una solucion candidata,
#podemos verificar en tiempo polinomico si es realmente una solucion correcta. En el caso del problema de premisas
#compatibles, esto implica verificar si un conjunto S de premisas de tamaño N no tiene incompatibles entre si
#Basicamente se verifica que el conjunto S tiene el tamaño requerido y luego verifico que ninguna premisa en S es incompatible
#con otra premisa en S. Esto implica revisar la lista de incompatibilidades I para cada par de premisas en S
#y aseugrarse de que no haya ninguna incompatibilidad
#La complejidad es O(N) donde N es es el largo de la lista I

#Ahora para reducir K-clique a N-premisas, construimos el problema
#Dado un grafo no dirigido G y un numero K, formamos:
#Para cada nodo v en G, creamos una premisa p en P
#Para cada arista(u,v) en G, añadimos la incompatibilidad (Pu, Pv) a I

#Si existe una clique de tamaño K en G entonces podemos seleccionar un conjunto S de premisas 
#y no habra incompatiblidades, ya que los nodos forman una clique. Ademas, |S| = k por lo que 
#habria solucion
#Si no existe un clique de tamaño K en g, entonces, cualquier conjunto de N premisas que seleccionemos
#tendra al menos un par de premisas incompatibles debido a la falta de una clique de tamaño K

#Por lo tanto, existe un K-clique en G si y solo si existe un N-premisas en el problema y de esta manera
#comprobamos que es Np-Completo

#*************************************************************

# Dado un grafo G=(V,E) no dirigido se denomina como Feedback set a un subconjunto X⊆V de vértices tal que el grafo resultante de eliminar los vértices de X 
# y los ejes adyacentes a estos no tiene ciclos. 
# El problema de decisión de Undirected Feedback Set quiere responder si dado un grafo G no dirigido existe un feedback set de tamaño k o menor. 
# Demostrar que este problema es NP-Completo. Sugerencia: Utilizar Vertex Cover.

# Dado una instancia del problema, que consiste en un grafo no dirigido G y un numero K, junto con un conjunto
# de vertices X C= V, podemos verificar en tiempo polinomico si X es un freedback Set de tamaño K o menor
# de la siguiente manera

# Verifico el tamaño: Verficar si |x| <= k. Eso se puede hacer en O(1)
# Eliminar vertices y aristas: Eliminar todos los vertices en X y las aristas adyacentes a ellos para 
# obtener el grafo G'
# Verificar la ausencia de ciclos: Verificar si G' no tiene ciclos, con DFS que tiene complejidad (V+E)
# De esta manera comprobamos que el problema es NP

# Ahora demostramos que es Np-completo
# Dado un grafo no dirigido G= (V,E) y un numero k, ¿existe un conjunto S incluido a V tal que |S| <= K
# y cada arista en E incide en almenos un vertice en S ?

# Construimos una instancia equivalente del problema Feedback Set
# Sea G=(V,E), una instancia del problema de VC
# Construimos un nuevo grafo G' = (V', E') de la siguiente manera
#     Para cada vertice v en V, creamos dos vertices v' y v'' en V'
#     Para cada arista (u,v) en E, agregamos lar aristas (u', u'') y (v', v'') en E'.

# Si existe un vertex Cover S en G: Tomamos S' = {v' | v E S}. El conjunto S' es un feedback Set
# en G' porque al eliminar los vertices en S' y los ejes adyacentes a ellos, eliminamos todas las 
# aristas originales de G, evitando asi la formacion de ciclos.
# Si existe un freedback Set S' en G': el conjunto S es un vertex cover en G porque cada arista en g
# tiene almenos un extremo en S, ya que al duplicar los vertices, garantizamos que al meons uno de los duplicados
# esta en S'

# Por lo tanto, exist eun VC si y solo si existe un feedback Set de tamaño k' y de esta manera 
# demostramos que es Np-completo

#*************************************************************

# El problema del Ciclo Hamiltoniano dirigido corresponde a una variante del problema de Ciclo Hamiltoniano con la diferencia que la instancia corresponde a un grafo dirigido. 
# Demostrar que este problema pertenece a NP-C. Sugerencia: Puede utilizar Ciclo Hamiltoniano.

# Para mostrar que nuestro problema esta en NP, simplemente verificamos que el ciclo Hamiltoniano
# contenga todos los vertices del grafo y que contenga exactamente una arista dirigida entre cada par consecutivo
# de vertices. Esto se puede hacer de forma lineal.

# Supongamos que tenemos una instancia del problema del ciclo hamiltoniano, que consiste en un grafo
# no dirigido y ahora queremos construir una instancia del problema del ciclo hamiltoniano dirigido
# Para cada arista no dirigida (u,v), agregamos dos aristas dirigidas en direcciones opuestas en el nuevo grafo
# dirigido. Esto significa que E' incluira tanto (u,v) como (v,u) para cada arista (u,v) en E
# Esto refleja la nocion de visitar tanto u como v en ambas direcciones, como se haria en un ciclo hamiltoniano
# no dirigido
# Garantizamos que cada vertice en V este presente en G' sin cambio
# Si encontramos un ciclo hamiltoninano dirigido en G', podemos reconstruir un ciclo no dirigido en G
# considerando solo las aristas no dirigidas correspondientes.
# De esta manera Podemos afirmar que el problema del ciclo hamiltoniando dirigido,
# es al menos tan dificil como el problema no dirigido

#*************************************************************

# Definimos al problema de Set Packing como: Dado “n” conjuntos S1,S2,...,Sn y un parámetro k. 
# Queremos saber si existe una colección de tamaño k de los subconjuntos tales que ningún elemento contenido en ellos está repetido en estos “k” conjuntos? 
# Demostrar que este problema es NP-Completo. Sugerencia: Utilizar Conjunto independiente.

# Para demostrar que el problema pertenece a NP, dado una coleccion de k conjuntos, podemos
# seguir estos pasos
# 1)verificar si cada conjunto en la coleccion es realmente un subconjunto del conjunto original
# de elementos.Eso se puede hacer en tiempo lineal
# 2) verificar si hay algun elemento que esta presente en mas de un conjunto.
# El tiempo de ejecucion total seria de orden O(K*N), donde K es el numero de conjuntos y n es el tamaño
# maximo de un conjunto

# De esta manera se demuestra que el problema de set packing pertenece a NP

# Ahora vamos a demostrar que es Np-completo
# Dado una instancia (G, K) donde G es un grafo no dirigido(V,E) y K es un numero entero, del problema IS,
# construimos una instancia (S1,S2,.....,Sn, K') del problema de Set packing:
#     Para cada vertice v en V, creamos un conjunto Sv que contiene v como unico elemento
#     Tomamos k' como K del IS

# Dado que Sv tiene un solo elemento, no hay elementos repetidos en ningun conjuntos. Ademas seleccionar
# k' conjuntos, estamos buscando k' vertices distintos en G, lo que es equivalente a buscar un conjunto
# independiente de tamaño al menos K
# Si encontramos una solucion del problema de Set packing, seleccionando k' conjuntos, encontes los vertices
# correspondientes forman un IS de tamaño al menos k. La inversa tambien es cierta: si encontramos un conjunto
# independiente en G de tamaño al menos k, podemos seleccionar conjuntos correspondientes en la instancia Set packing

# De esta manera, hemos demostrado que hay un IS de tamaño almenos k si 
# y solo si hay un Set packing de al menos un tamaño
# k' y asi mostramos que el problema tambien es NP-completo







#**************************************************************OTRO DIA

# Para el desarrollo de un circuito digital se requiere construir
# “n” caminos por donde pasará corriente eléctrica. Por diseño cada
# uno de esos caminos debe empezar en un determinado punto y
# finalizar en otro. Por supuesto, estos caminos no deben cruzarse.
# Para la construcción de este circuito se cuenta diferentes capas
# conductoras en los que se pueden imprimir diferentes caminos. Pero
# esto se puede abstraer como una grafo donde cada vértice
# corresponde a una región por la puede pasar un camino y los ejes
# las regiones circundantes con las que puede conectarse.
# Se pide: Demostrar que el problema es NP-Completo.
# HINT: El problema se puede ver como “Node-disjoint directed path
# problem”. Pruebe con “3-SAT”

#*************************************************************

# La siguiente es una versión de Conjunto Independiente. 
# Dado un grafo G= (V, E) y un entero k, decimos que I ⊆ V es fuertemente independiente si dados dos vértices u y v en I, 
# la arista (v, u) no pertenece a E y además no hay ningún camino de tamaño 2 (con dos aristas) de u a v. 
# El problema de Conjuntos Fuertemente Independientes consiste en decidir si G tiene un conjunto fuertemente independiente de tamaño al menos k. 
# Probar que el problema de Conjuntos Fuertemente Independientes es NP completo. 
# Utilizar para ello que Conjuntos Independientes es NP completo.

#*************************************************************

# Una compañía multinacional desea contratar cobertura satelital para sus “n” sedes repartidas por el mundo. 
# Han averiguado entre varias empresas que proveen el servicio pero ninguna de ellas tiene cobertura total. 
# Les gustaría poder contratar a “k” o menos empresas. Pero tienen una condición adicional: al menos una de sus sedes debe tener cobertura de todas las empresas que la ofrecen. 
# Con eso pueden iniciar una certificación de calidad que necesitan. Se pide: Demostrar que el problema es NP-Completo. Sugerencia: Utilizar Set Cover

#*************************************************************

# El directorio de una empresa realizará una cena de fin de año. En total son “n” directivos que se deben sentar alrededor de una mesa circular. 
# Lamentablemente existen conflictos entre algunos de ellos que impiden que se sienten uno al lado del otro. Dado una instancia del problema, 
# que incluye los n directivos y un listado donde se ven aquellos pares de directivos que están peleados entre sí, determinar si es posible sentarse en la mesa. 
# Demostrar que el problema es NP-C. Sugerencia: Utilizar ciclo Hamiltoniano.

