# La sala de guardia de un hospital tiene que tener al menos un médico en todos los feriados y en los fines de semana largos de feriados. Cada profesional indica sus posibilidades: 
# por ejemplo alguien puede estar de guardia en cualquier momento del fin de semana largo del 9 de julio (p. ej. disponibilidad de A para el 9 de julio = 
# (Jueves 9/7, Viernes 10/7, Sábado 11/7, Domingo 12/7)), también puede suceder que alguien pueda sólo en parte (por ejemplo, disponibilidad de B para 9 de julio = 
# (Jueves 9/7, Sábado 11/7, Domingo 12/7)). Aunque los profesionales tengan múltiples posibilidades, a cada uno se lo puede convocar para un solo día 
# (se puede disponer de B sólo en uno de los tres días que indicó). 
# Para ayudar a la sala de guardia a planificar cómo se cubren los feriados durante todo el año debemos resolver el problema de las guardias: Existen k períodos de feriados 
# (por ejemplo, 9 de julio es un período de jueves 9/7 a domingo 12/7, en 2019 Día del Trabajador fue un período de 1 día: miércoles 1 de mayo, etc.). 
# Dj es el conjunto de fechas que se incluyen en el período de feriado j-ésimo. Todos los días feriados son los que resultan de la unión de todos los Dj. 
# Hay n médicos y cada médico i tiene asociado un conjunto Si de días feriados en los que puede trabajar 
# (por ejemplo B tiene asociado los días Jueves 9/7, Sábado 11/7, Domingo 12/7, entre otros).
# Proponer un algoritmo polinomial (usando flujo en redes) que toma esta información y devuelve qué profesional se asigna a cada día feriado 
# (o informa que no es posible resolver el problema) sujeto a las restricciones:
# Ningún profesional trabajará más de F días feriados (F es un dato), y sólo en días en los que haya informado su disponibilidad.
# A ningún profesional se le asignará más de un feriado dentro de cada período Dj.

# Para resolver este problema, podemos modelarlo como un problema de flujo en redes.
# Creamos el grafo de flujo:
#     creamos un nodo fuente y un nodo sumidero
#     para cada medico i y dia feriado j, creamos un nodo en el grafo
#     conectamos el nodo fuente con cada medico i con una capacidad igual a F(el limite de dias 
#     feriados que puede cubrir)
#     conectamos cada nodo medico con los nodos de los dias feriados en los que puede trabajar
#     con capacidad de 1
#     conectamos cada nodo feriado j con el nodo sumidero con capacidad de 1
# Aplicamos el algoritmo de ford fulkerson para encontrar el flujo maximo en el grafo
# Y verifico que si el flujo maximo es la cantidad de dias feriados a cubrir por los medicos
# si es asi, mostramos los dias asignados por los medicos
# La complejidad del algoritmo es:
# Construccion del grafo O(n*m) donde n es la cantidad de medicos y m es la cantidad de dias feriados
# Flujo maximo done la complejidad es O(V*E**2)

#*************************************************************************************************************

# Definimos el Problema de la Evacuación de la siguiente manera: Se tiene un grafo dirigido G = (V, E) que describe una red de caminos. 
# Tenemos una colección de nodos X ⊂ V que son los nodos poblados (ciudades) y otra colección de nodos S ⊂ V que son los nodos de refugio (supondremos que X y S son disjuntos). 
# En caso de una emergencia queremos poder definir un conjunto de rutas de evacuación de los nodos poblados a los refugios. 
# Un conjunto de rutas de evacuación es un conjunto de caminos en G tales que (i) cada nodo en X es el origen de un camino, 
# (ii) el último nodo de cada camino es un refugio (está en S), y (iii) los caminos no comparten aristas entre sí. 
# Se pide: dados G, X y S, mostrar cómo se puede decidir en tiempo polinomial si es posible construir un conjunto de rutas de evacuación 
# (usar flujo en redes para eso. Construir la red adecuada).

# Para abordar el problema de la evacuacion y decidir si es posible construir un conjunto de rutas
# de evacuacion en tiempo polinomial utilizando redes de flujo, podemos modelar el problema como un problema
# de flujo maximo en una red
# Contruccion de la red de flujo:
#     crear un grafo dirigido auxiliar G' = (V', E') a partir de G
#     agregar un noodo fuende s y un nodo sumidero tablero
#     para cada nodo x en X, agregar una arista (s,x) con capacidad 1
#     para cada noxo r en S, agregar una arista (r,t) con capacidad 1
#     para cada arista (u,v) en G, agregar una arista (u,v) en G' con capacidad infinita

# Para resolver el problema de flujo maximo, aplicamos un algoritmo de flujo maximo en G'.
# Este algoritmo encontrara la cantidad maxima de flujos que pueden pasar desde s a t
# def ford_fulkerson(grafo, fuente, sumidero):
#     max_flujo = 0
#     parent = [-1] * len(grafo)

#     while bfs(parent):
#         path_flujo = float('inf')
#         s = sumidero

#         while s != fuente:
#             path_flujo = min(path_flujo, grafo[parent[s]][s])
#             s = parent[s]

#         max_flujo += path_flujo

#         v = sumidero
#         while v != fuente:
#             u = parent[v]
#             grafo[u][v] -= path_flujo
#             grafo[v][u] += path_flujo
#             v = parent[v]

#     return max_flujo
# def es_factible(G,X):
#     num_poblados = len(x)
#     fuente = 0
#     sumidero = 1
#     flujo_maximo = ford_fulkerson(G,fuente, sumidero)
#     return flujo_maximo == num_poblados

# Si la cantidad maxima de flujo desde s a t es igual al numero de nodos
# poblados, entonces es posible construir un conjunto de rutas de evacuacion
# En este caso, cada nodo poblado tendra una ruta hacia un refugio sin compartir camino con
# otras rutas
# La complejidad del algoritmo es O(V*E**2)

#*************************************************************************************************************

# Una empresa global de tecnología tiene un conjunto de “c” centros
# de cómputos. Cada centro “i” tiene una capacidad de procesamiento
# “pi” por día. Todos los centros están conectados en una red
# privada. En la red se encuentran enlaces punto a punto que fueron
# construidos en diferentes momentos. Por lo tanto cada enlace “j”
# tiene una capacidad de transmisión diaria de “ej” en ambos
# sentidos. Un enlace conecta dos centros de cómputos. No todos los
# centros de cómputos están conectados entre sí. Cada uno tiene
# enlaces a un subconjunto de ellos. Para un proceso intensivo han
# separado los centros de cómputos en dos conjuntos. Los primeros
# realizan un procesamiento de un lote de datos y los empaquetan
# para enviarselos a los segundos. Los segundos reciben los paquetes
# y terminan con un segundo procesamiento. No hay dependencia entre
# paquetes de datos ni impedimentos en determinar los tamaños de
# cada paquete.
# En base a una instancia de este problema desean determinar si va a
# ser posible o no procesar en el día todos los datos “d” .
# Modelar el problema como una red de flujo y explicar como
# resolverlo paso a paso. Analizar complejidad espacial y temporal.

# Para resolver el problema, construimos la red de flujo
#     Creamos nodos para cada centro de computo, el nodo fuente y el nodo sumidero
#     conectamos cada centro de computo al nodo sumidero con un enlace que tiene capacacidad
#     igual a la capacidad de procesamiendo del centro (pi)
#     concetamos el nodo origen a cada centro de computo con un enlace que tiene capacidad de procesamiento
#     conectamos los centro de computo entre si con la capacidad de transmision ej
# Para analisar el flujo maximo, aplicamos el algoritmo de ford fulkerson
#     inicializamos el flujo en cero
#     mientras haya un camino aumentable desde el nodo de origen hasta el nodo de destinto:
#         encontramos un camino aumentante
#         calculamos la capacidad residual del camino
#     devolvemos el flujo resultante
# Y verificamos si el flujo total desde el origen hasta el destino es mayor o igual a la suma de capacidades
# de procesamiendo de los nodos de destinos, entonces es factible procesar todos los datos
# La compeljidad del algoritmo es O(VE**2)

#*************************************************************************************************************

# Una empresa de autobuses se conformó luego de la fusión de varias
# compañías menores. Actualmente tienen diferentes rutas que cubrir.
# Cada una con horario de inicio en una ciudad y finalización en
# otra. Existe la posibilidad de cubrir con un mismo micro
# diferentes rutas.
# Siempre la ruta comienza desde donde parte el micro, pero también
# puede pasar que el micro tenga tiempo suficiente para trasladarse
# hasta otro punto y cubrir otra ruta. Cuentan con una flota activa
# de N micros. Necesitan saber si les es posible cubrir con ella los
# requerimientos o si requieren contar con micros extra.
# Resolver el problema utilizando como parte del mismo redes de
# flujo. Analice su complejidad temporal y espacial.

# El objetivo es determinar si es posible cubrir todas las rutas con la flota activa
# de micros y, en caso contrario, cuantos micros adicionales son necesarios.

# Para crear el grafo:
#     Agregamos un nodo fuente que representa la ciudad de inicio de los micros
#     agregamos un nodo sumidero que representa la ciudad de finalizacion de los micros
#     conectamos el nodo fuente a cada ciudad de inicio con aristas de capacidad igual
#     al numero de micros disponibles y peso cero
#     conecatmos cada ciudad de finalziacion al nodo sumidero con aristas de capacidad igual
#     al numero de micros necesarios para cubrir la ruta
#     conectamos cada ciudad de inicio a cada ciudad de finalizacion con capacidad infinita

# Aplicamos ford fulkerson para encontrar el flujo maximo:
#     inicializamos el flujo en 0
#     mientras haya camino aumentable de la fuente al cumidero
#         encontramos un camino aumentante
#         calculamos la capaciadd residual del camino
#     devolvemos el flujo resultante
# Si el flujo maximo es igual al numero total de micros disponibles, entonces es posible cubrir
# todas las rutas
# La complejidad espacial es O(V+E) por la ceracion del grafo y la complejidad temporal es 
# O(V*E**2) por el el algoritmo de ford fulkerson















# OTRODIA
#*************************************************************************************************************

# Para satisfacer la producción de un producto electrónico una
# empresa debe comprar un componente a sus diferentes proveedores.
# Cada proveedor tiene una cantidad máxima que puede ofrecer
# mensualmente. Además las diferentes plantas de producción demandan
# una cantidad mensual del mismo. Por cuestiones logísticas algunos
# proveedores no pueden enviar a ciertas plantas de producción. El
# mes próximo por una promoción se va a tener que producir al 100%
# de la capacidad. Determinar en forma eficiente si es posible
# satisfacer esta demanda.
# Explicar detalladamente y paso a paso la solución propuesta.
# Analizar complejidad


#*************************************************************************************************************

# La red de transporte intergaláctico es una de las maravillas del nuevo imperio terráqueo. 
# Cada tramo de rutas galácticas tiene una capacidad infinita de transporte entre ciertos planetas. 
# No obstante, por burocracia - que es algo que no los enorgullece - existen puestos de control en cada planeta que reduce cuantos naves espaciales pueden pasar por día por ella. 
# Por una catástrofe en el planeta X, la tierra debe enviar la mayor cantidad posible de naves de ayuda. 
# Por un arreglo, durante un día los planetas solo procesaran en los puestos de control aquellas naves enviadas para esta misión.  
# Tenemos que determinar cuál es la cantidad máxima de naves que podemos enviar desde la tierra hasta el planeta X. 
# Sugerencia: considerar a este un problema de flujo con capacidad en nodos y no en ejes

#*************************************************************************************************************

# La compañía eléctrica de un país nos contrata para que le ayudemos a ver si su red de transporte desde su nueva generadora hidroeléctrica hasta su ciudad capital es robusta. 
# Nos otorgan un plano con la red eléctrica completa: todas las subestaciones de distribución y red de cableados de alta tensión. 
# Lo que quieren que le digamos es: cuantas secciones de su red se pueden interrumpir antes que la ciudad capital deje de recibir la producción de la generadora? 
# (Sugerencia: investigue sobre el Teorema de Menger) Puede informar cual es el subconjunto de ejes cuya falla provoca este problema?

#*************************************************************************************************************

# La red ARPANET, antecesora de internet, se creó para seguir funcionando incluso antes fallas en parte de su red. 
# El país “Atrasoñia” - que se mantuvo cerrado a los avances tecnológicos de las últimas décadas - ha decidido construir su propia red de redes. 
# Han leído la documentación desclasificada de ARPANET y se han instruido en conectividad de redes. 
# Proponen una red informática para unir sus principales organismos estatales. Nos convocan para que validemos su diseño. 
# Debemos responder: ¿Cuántos cables de datos de la red se tienen que romper antes que la conectividad del grafo se rompa? 
# (tener en cuenta que los cables de datos son bidireccionales) ¿Cuántos nodos se tienen que romper antes que el grafo restante deje de ser conexo? 
# (Sugerencia: piense en transformar de alguna forma los nodos para resolverlo mediante lo creado en el punto a)  

#*************************************************************************************************************

# La policía de la ciudad tiene “n” comisarías dispersas por la ciudad. 
# Para un evento deportivo internacional deben asignar la custodia de “m” centros de actividades. 
# Una comisaría y un centro de actividades pueden ser emparejados si y sólo si la distancia entre ellos no es mayor a un valor d. 
# Contamos con la distancia entre todos los centros y las comisarías. Una comisaría sólo puede custodiar un centro. 
# El centro puede ser custodiado por una comisaría. Determinar si es posible la asignación de tal forma que todos los centros estén custodiados. 
# ¿Cómo modificaría la resolución del problema si en lugar de que cada centro de actividades i tenga que ser asignado a una sola comisaría, 
# tenga que ser asignado a mi comisarías? 
# ¿Cómo modificaría la resolución del problema si además hubiera una restricción entre comisarías que implicaría que una comisaría Ni 
# y una Nj no pudieran ser asignadas juntas a un centro Mi? ¿Para qué casos dejaría de ser eficiente la resolución?

#*************************************************************************************************************

# Una compañía minera nos pide que la ayudemos a analizar su nueva explotación. Ha realizado el estudio de suelos de diferentes vetas y porciones del subsuelo. 
# Con estos datos se ha construido una regionalización del mismo. Cada región cuenta con un costo de procesamiento y una ganancia por extracción de metales preciosos. 
# (En algunos casos el costo supera al beneficio). Al ser un procesamiento en profundidad ciertas regiones requieren previamente procesar otras para acceder a ellas. 
# La compañía nos solicita que le ayudemos a maximizar su ganancia, determinando cuales son las regiones que tiene que trabajar. 
# Tener en cuenta que el costo y ganancia de cada región es un valor entero. Para cada región sabemos cuales son aquellas regiones que le preceden. 
# Resolver el problema planteado utilizando una aproximación mediante flujo de redes.

#*************************************************************************************************************

# Un taller metalúrgico cuenta con un conjunto de M controles numéricos computarizados (CNC). Cada uno de ellos puede realizar trabajos de duración en bloques de 1 hora. 
# Por otro lado, cuenta con N tareas a realizar. Cada tarea i tiene una duración de horas de desarrollo, una hora de posible comienzo (cuando puede comenzar a realizarse) 
# y una hora de entrega (momento donde debe estar finalizada). Las tareas pueden realizarse parcialmente y utilizarse para su elaboración una o varias máquinas. 
# Por ejemplo si la tarea A requiere 4 horas. Podría realizarse 1 hora en la máquina 1 y luego de un intervalo concluir su desarrollo en la máquina B (3 horas restantes). 
# El jefe de planta nos solicita nuestra ayuda para que le ayudemos a determinar si podrá cumplir con la finalización de las tareas en tiempo y forma. 
# Y en caso afirmativo le indiquemos cómo organizarla. Se solicita utilizando redes de flujos dar una solución al problema.

#*************************************************************************************************************

# Una red de espías se encuentran diseminados por todo el país. 
# Cada uno de ellos únicamente conoce a un número limitado de sus pares con los que pude tener contacto dejando un mensaje escrito en una ubicación conocida. 
# Este conocimiento no es recíproco. En caso de una crisis la agencia puede enviar mensajes utilizando esta red desde su base principal a un determinado agente especial. 
# Una cuestión importante es que una vez utilizado un espía para transmitir un mensaje durante el resto de la crisis no se vuelve a utilizar. 
# La agencia desea conocer, dada su red y un agente de destino de sus mensajes. 
# ¿Cuál es la mínima cantidad de espías que un rival podría neutralizar para reducir en un 30% la cantidad de mensajes máximos que puede enviar desde la base al agente? 
# Utilizando redes de flujos dar una solución al problema.

#*************************************************************************************************************

# En un juego multijugador cooperativo de "p" participantes se muestra una grilla de n*n celdas. 
# Inicialmente en una posición al azar se colocan los avatares de los jugadores e igual cantidad de cuevas. 
# Cada "gusano" se desplaza 1 celda por turno ocupando una circundante que esté vacía (como máximo tiene 4: arriba, abajo, izquierda y derecha). 
# A medida que se desplaza crece y por lo tanto sigue ocupando por las que pasó anteriormente. 
# El objetivo del juego es lograr que los “p” jugadores lleven a sus gusanos a las cuevas (es indiferente a cual pero cada uno tiene que estar en una cueva diferente).
#  Nos solicitan que realicemos el pseudocódigo que verifique en un turno determinado si aún es posible que los jugadores ganen. Es decir que todos los gusanos puedan llegar a la cueva.

#*************************************************************************************************************

# Se cuenta con una grafo G=(V,E) con capacidad 1 en cada uno de sus ejes. Existen 2 nodos que tomaremos como “s” fuente y “t” sumidero. 
# Podemos determinar el flujo máximo F entre s-t. Se pide proponer un algoritmo eficiente que dado un valor “k”, 
# determine la cantidad mínima de ejes y cuáles de ellos eliminar para que el nuevo flujo máximo sea F-k. 
# Determinar su complejidad y detallar mediante pseudocódigo y una explicación cómo funciona.

#*************************************************************************************************************

# Una empresa de autobuses se conformó luego de la fusión de varias compañías menores. Actualmente tienen diferentes rutas que cubrir. 
# Cada una con horario de inicio en una ciudad y finalización en otra. Existe la posibilidad de cubrir con un mismo micro diferentes rutas. 
# Siempre la ruta comienza desde donde parte el micro, pero también puede pasar que el micro tenga tiempo suficiente para trasladarse hasta otro punto y cubrir otra ruta. 
# Cuentan con una flota activa de N micros. Necesitan saber si les es posible cubrir con ella los requerimientos 
# y si pueden contar con micros de backup ante la necesidad de controles programados de algunos de los móviles. 
# Ayudar a resolver el problema mediante el uso de redes de flujo.

#*************************************************************************************************************

# Contamos con una red de Flujo definida sobre el grafo G=(V,E) y tenemos una asignación de flujo f(e) sobre G. 
# Nos solicitan elaborar un algoritmo que en base a esta información nos indique cómo se actualiza el flujo si uno de los ejes tiene un cambio de capacidad 
# (puede ser positiva o negativa). Debemos evitar volver a ejecutar el algoritmo de Ford-Fulkerson desde cero. 
# Explicar los diferentes casos que podrían suceder. Utilizar los conceptos de flujo máximo/corte mínimo en su explicación. 
# Brindar pseudocódigo de su propuesta y análisis de complejidad.

#*************************************************************************************************************

# Un grupo de "n" amigos participan en un torneo de voley. En cada partido se debe presentar una planilla de "y" jugadores. 
# Se juegan partidos 1 vez por semana, durante un periodo de 9 meses. Para lograr que juegue la mayoría se propuso que cada amigo no juegue más de 4 partidos. 
# Esos partidos deben estar lo más separados posible, por lo que no pueden jugar más de 1 partido por mes. 
# Finalmente se tiene que tener en cuenta que algunos amigos en ciertas fechas no pueden asistir por cuestiones personales. 
# Proponer un algoritmo polinomial que utilizando esta información realice la asignación de jugadores por partido 
# (o que indique que con esas restricciones no es posible realizarlo)

#*************************************************************************************************************

# Para un evento solidario un conjunto de n personas se ofrecieron a colaborar. En el evento hay m tareas a desarrollar. 
# Cada tarea tiene un cupo máximo de personas que la puede realizar. A su vez cada persona tiene ciertas habilidades que la hacen adecuadas para un subconjunto de tareas. 
# Proponga una solución mediante red de flujos que maximice la cantidad de personas asignadas a las tareas. 
# ¿Hay forma de lograr asegurarnos un piso mínimo de personas en cada tarea? ¿Cómo impacta en la solución presentada en el punto anterior?

#*************************************************************************************************************

# Una ciudad tiene una red inalámbrica interna para interconectar
# diferentes servidores de varias instituciones públicas. Existen un
# conjunto "A" de antenas de interconexión que están dispersas por
# la ciudad. Cada una de ellas tiene una localización "x,y", un
# alcance de recepción limitado (un radio "R_a") y una cantidad
# máxima de conexiones que puede tener en forma simultánea. Se
# recopiló una lista "S" de servidores, cada uno de ellos con su
# ubicación "x,y"
# Determinar si es posible que todos los servidores pueden estar
# conectados a una antena respetando las restricciones impuestas.
# Explique paso a paso la solución propuesta y analice su
# complejidad temporal.

