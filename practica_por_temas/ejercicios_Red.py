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

#*************************************************************

# El problema del Ciclo Hamiltoniano dirigido corresponde a una variante del problema de Ciclo Hamiltoniano con la diferencia que la instancia corresponde a un grafo dirigido. 
# Demostrar que este problema pertenece a NP-C. Sugerencia: Puede utilizar Ciclo Hamiltoniano.

#*************************************************************

# Definimos el problema Subgrafo denso de la siguiente manera: Dado un grafo G=(V,E) y dos parámetros a y b. Existe en G un subconjunto de “a” vértices con al menos “b” ejes entre ellos. 
# Demostrar que este problema es NP-Completo. Sugerencia: Utilizar el problema del Clique.

#*************************************************************

# Definimos al problema de Set Packing como: Dado “n” conjuntos S1,S2,...,Sn y un parámetro k. 
# Queremos saber si existe una colección de tamaño k de los subconjuntos tales que ningún elemento contenido en ellos está repetido en estos “k” conjuntos? 
# Demostrar que este problema es NP-Completo. Sugerencia: Utilizar Conjunto independiente.

#*************************************************************

# Dado un grafo G=(V,E) no dirigido se denomina como Feedback set a un subconjunto X⊆V de vértices tal que el grafo resultante de eliminar los vértices de X 
# y los ejes adyacentes a estos no tiene ciclos. 
# El problema de decisión de Undirected Feedback Set quiere responder si dado un grafo G no dirigido existe un feedback set de tamaño k o menor. 
# Demostrar que este problema es NP-Completo. Sugerencia: Utilizar Vertex Cover.

#*************************************************************MAÑANA

# Un país está modificando su red radiofónica. 
# Existen muchas estaciones de radios cada una con su propia frecuencia de transmisión. 
# Desean reasignarlas de tal forma de no usar más de N frecuencias. El problema es que ciertas radios por su ubicación geográfica y potencia pueden interferir con otras. 
# Un estudio informa cuántas radios hay, y para cada radio con cuáles hay riesgo de interferencia. Quisieran determinar si es posible realizar la reasignación. 
# Demuestre que el problema planteado es NP-COMPLETO. HINT!: Tal vez le resulte útil coloreo de grafos.

#*************************************************************


# Para un evento a realizar se requiere conformar una selección musical entre el conjunto A de “n” canciones. 
# Podemos enumerar a los elementos de A como a1,a2,...,an. Por otra parte, contamos con un conjunto “B” de “m” personas. 
# Cada una de ellas con un subsets de esas canciones que le gustan. Deseamos saber si podemos seleccionar un subconjunto de no más de “k” canciones, 
# de tal forma que existe al menos 1 canción que le guste a cada uno. Se pide: Demostrar que el problema es NP-Completo. Sugerencia: Se puede utilizar Vertex Cover.

#*************************************************************

# Nos piden que organicemos una jornada de apoyo de estudio para exámenes. 
# Tenemos que poder dar apoyo a “n” materias y hemos recibido currículos de “m” postulantes para ser potenciales ayudantes. 
# Cada ayudante puede ayudar en un determinado subconjunto de materias. Para cada una de las materias hay un subconjunto de postulantes que pueden dar apoyo en ella. 
# La pregunta es: dado un número k < m, ¿es posible seleccionar a lo sumo “k” ayudantes de modo tal que siempre haya un ayudante que pueda dar consultas en alguna de las n materias? 
# Este problema se llama Contratación Eficiente. Probar que “Contratación Eficiente” es NP-completo. Sugerencia: se puede tratar de usar Cubrimiento de Vértices.
#*************************************************************

# Un departamento dentro de una universidad adquirió “n” proyectores para dar clases durante el cuatrimestre. 
# Envió un formulario a los docentes de las distintas materias para conocer si los necesitaban como complemento para sus clases. 
# Un subconjunto de docentes respondió afirmativamente. Sabiendo que cada materia tiene clases 1 o más veces por semana en un horario establecido. 
# Y sabiendo que los horarios de varias de esas materias se superponen. Nos solicitan determinar si la cantidad comprada alcanza o si se tiene que dejar a docentes sin acceso a esas cuentas. 
# Demostrar que lo solicitado es NP-COMPLETO. Sugerencia: Tal vez le resulte útil “k” coloreo de grafos.

#*************************************************************

# Para elaborar una película de detectives un grupo de escritores se ha juntado para elaborar una trama atrapante y que tenga coherencia. 
# En largas jornadas han propuesto un gran conjunto de premisas, giros argumentales y eventos claves. Lamentablemente algunas de ellas no son compatibles entre sí. 
# Por cada situación han anotado con cual no es compatible. Desean poder seleccionar un conjunto de N premisas compatibles para presentar a los productores como idea inicial. 
# Se pide: Demostrar que el problema es NP-Completo. Sugerencia:  Tal vez le resulte útil clique

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

#**************************************************************

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