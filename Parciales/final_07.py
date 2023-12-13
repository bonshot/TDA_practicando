# Se está formando una nueva comisión de actividades culturales de un pueblo. Cada habitante es miembro de 0 o más
# clubes, y de exactamente 1 partido político. Cada grupo de interés debe nombrar a un representante ante la nueva
# comisión de actividades culturales, con las siguientes restricciones: cada partido político no puede tener más de N/2
# simpatizantes en la comisión, cada persona puede representar a solo un club, cada club debe estar representado por
# un miembro. Implementar un algoritmo que dada la información de los habitantes (a qué clubes son miembros, a
# qué partido pertenecen), nos dé una lista de representantes válidos. Indicar y justificar la complejidad del algoritmo
# implementado.

# Para resolver el problema creamos una red de flujo con las siguientes
# caracteristicas:
#     Creamos un nodo fuente y un nodo sumidero
#     Por cada partido, persona y club, creamos un nodo
#     Conectamos la fuente con el partido con un peso de N//2, donde
#     N es la cantidad de habitantes
#     Conectamos los partidos con las personas con peso de 1
#     Conectamos las personas a los clubes que pertenecen con peso de 1
#     Y finalmente conectamos los clubes al sumidero con epso de 1
# Ahora, aplicamos el algoritmo de ford fulkerson para encontrar el flujo maximo
# Pseudocodig
# Incializamos el flujo
# Por cada arista de mi grafo, añado al flujo esa arista con peso 0
# realizo una copia de mi grafo
# Mientras haya camino aumentante de la fuente al sumidero
#     obtengo el peso minimo de mi camino
#     recorro el camino
#         si hay arista entre el anterior y el actual
#             aumento el flujo con el minimo peso en esa arista
#             actualizo el grafo residual
#         sino
#             disminuyo el flujo en esa arista con el minimo
#             actualizo el grafo residual
# devuelvo el flujo final

# Finalmente,me fijo cuales participantes del flujo pertenecen a los partidos
# y esos seran los participantes validos.
# La complejidad espacial es O(V+E), la complejidad de ford fulkerson es
# O(V*E*E). Por lo tanto la complejidad final es O(V*E**2)