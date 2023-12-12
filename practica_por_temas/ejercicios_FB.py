# Contamos con un conjunto de “n” puntos (x,y) en el plano cartesiano. 
# Un par de puntos es el más cercano si la distancia euclidiana entre ellos es menor a la de cualquier otro par. 
# Resuelva el problema mediante un algoritmo naive que nos informe cuales son los 3 pares de puntos más cercanos. 

# Un cuadrado mágico de tamaño “n” es una disposición de los números enteros desde 1 a n2 en una matriz de nxn que cumple la siguiente condiciones.  
# Cada número aparece solo una vez. La suma de cada fila, columna y diagonal principal da el mismo valor. 
# Proponer un algoritmo por generar y probar que dado un valor “n” calcule, si existe, un cuadrado mágico de ese tamaño. 


# Se encuentran en un río 3 caníbales y 3 vegetarianos. En la orilla hay un bote que permite pasar a dos personas atravesarlo. 
# Los 6 quieren cruzar al otro lado. Sin embargo existe un peligro para los vegetarianos: 
# si en algún momento en alguna de las márgenes hay más caníbales que vegetarianos estos los atacarán. 
# Tener en cuenta que el bote tiene que ser manejado por alguien para regresar a la orilla. 
# Determinar si es posible establecer un orden de cruces en el que puedan lograr su objetivo conservando la integridad física. 
# Explicar cómo construir el grafo de estados del problema. Determinar cómo explorarlo para conseguir la respuesta al problema. Brinde, si existe, la respuesta al problema.


# Resuelva el problema de las reinas en el tablero de ajedrez mediante backtracking planteado como permutaciones. 
# Brinde el pseudocódigo y determine la cantidad máxima posible de subproblemas a explorar.


# En un tablero de ajedrez (una cuadrícula de 8x8) se ubica la pieza llamada “caballo” en la esquina superior izquierda. 
# Un caballo tiene una manera peculiar de moverse por el tablero: Dos casillas en dirección horizontal o vertical y después una casilla más en ángulo recto 
# (formando una forma similar a la letra “L”). El caballo se traslada de la casilla inicial a la final sin tocar las intermedias, dado que las “salta”. 
# Se quiere determinar si es posible, mover esta pieza de forma sucesiva a través de todas las casillas del tablero, 
# pasando una sola vez por cada una de ellas, y terminando en la casilla inicial. Plantear la solución mediante backtracking.

# En la teoría de gráfos, se conoce como etiquetado de vértices a asignarle a cada vértice una etiqueta diferente. 
# De igual manera se puede realizar un etiquetado de ejes. Generalmente el etiquetado se puede representar mediante un número entero. Existen diferentes etiquetados posibles. 
# Trabajaremos con el “etiquetado elegante” (graceful labeling). Dado un grafo G=(V,E) con m ejes se asignará como etiqueta a cada uno de sus vértices un número entre 0 y m. 
# Se computará para cada eje la diferencia absoluta entre las etiquetas de vértices y esa será su etiqueta. Se espera que los ejes queden etiquetados del 1 al m inclusive 
# (y que obviamente cada una sea única). Construya mediante generar y probar un algoritmo que dado un grafo determine un etiquetado elegante (si es posible).

# Se cuenta con “n” trabajos por realizar y la misma cantidad de contratistas para realizarlos. 
# Ellos son capaces de realizar cualquiera de los trabajos aunque una vez que se comprometen a hacer uno, no podrán realizar el resto. 
# Tenemos un presupuesto de cada trabajo por cada contratista. Queremos asignarlos de forma tal de minimizar el costo del trabajo total. 
# Proponer un algoritmo por branch and bound que resuelva el problema de la asignación. 


# Contamos con un conjunto de “n” de equipamientos que se deben repartir entre un conjunto de “m” equipos de desarrollo. 
# Cada equipo solicita un subconjunto de ellas. Puede ocurrir que un mismo equipamiento lo soliciten varios equipos o incluso que un equipamiento no lo solicite nadie. 
# Queremos determinar si es posible seleccionar un subconjunto de equipos de desarrollo entregándoles a todos ellos todo lo que soliciten 
# y al mismo tiempo que ninguno de los equipamientos quede sin repartir. Resolver el problema mediante backtracking.


# Un ciclo euleriano en un grafo es un camino que pasa por cada arista una y solo una vez, comenzando por un vértice y finalizando en el mismo. 
# Sea un grafo G=(V,E) se busca generar si es posible un ciclo euleriano. Resolverlo mediante generar y probar. 


# Contamos con un conjunto de “n” actividades entre las que se puede optar por realizar. 
# Cada actividad x tiene una fecha de inicio Ix, una fecha de finalización fx y un valor vx que obtenemos por realizarla. 
# Queremos seleccionar el subconjunto de actividades compatibles entre sí que maximice la ganancia a obtener (suma de los valores del subconjunto). 
# Proponer un algoritmo por branch and bound que resuelva el problema.


# Se cuenta con “n” servidores especializados en renderización de videos para películas animadas en 3d. 
# Los servidores son exactamente iguales. Además contamos con “m” escenas de películas que se desean procesar. 
# Cada escena tiene una duración determinada. 
# Queremos determinar la asignación de las escenas a los servidores de modo tal de minimizar el tiempo a esperar hasta que la última de las escenas termine de procesarse. 
# Determinar dos metodologías con la que pueda resolver el problema y presente como realizar el proceso.

# Un granjero debe trasladar un lobo, una cabra y una zanahoria a la otra margen de un río. Cuenta con un bote donde solo entra él y un elemento más. 
# El problema es que no puede quedar solo el lobo y la cabra. Dado que la primera se comería a la segunda. De igual manera, tampoco puede dejar solo a la cabra y la zanahoria. 
# La primera no dudaría en comerse a la segunda. ¿Cómo puede hacer para cruzar? Explicar cómo construir el grafo de estados del problema. 
# Determinar cómo explorarlo para conseguir la respuesta al problema. Brinde, si existe, la respuesta al problema.

