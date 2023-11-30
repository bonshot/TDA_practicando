from TDAS import Grafo

#4. Carlos tiene un problema: sus 5 hijos no se soportan. Esto es a tal punto, que ni siquiera están dispuestos a caminar
#  juntos para ir a la escuela. Incluso más: ¡tampoco quieren pasar por una cuadra por la que haya pasado alguno de sus
#  hermanos! Sólo aceptan pasar por las esquinas, si es que algún otro pasó por allí. Por suerte, tanto la casa como la
#  escuela quedan en esquinas, pero no está seguro si es posible enviar a sus 5 hijos a la misma escuela. Utilizando lo visto
#  en la materia, formular este problema y resolverlo. Indicar y justificar la complejidad del algoritmo.


def ford_fulkerson(grafo, s, t):
	flujo = {}
	for v in grafo:
		for w in grafo.adyacentes(v):
			flujo[(v, w)] = 0
	grafo_residual = copiar(grafo)
	while (camino = obtener_camino(grafo_residual, s, t)) is not None:
		capacidad_residual_camino = min_peso(grafo, camino)
		for i in range(1, len(camino)):
			if grafo.hay_arista(camino[i-1], camino[i]):
				flujo[(camino[i-1], camino[i])] += capacidad_residual_camino
				actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], capacidad_residual_camino)
			else:
				flujo[(camino[i], camino[i-1])] -= capacidad_residual_camino
				actualizar_grafo_residual(grafo_residual, camino[i], camino[i-1], capacidad_residual_camino)

	return flujo

def actualizar_grafo_residual(grafo_residual, u, v, valor):
	peso_anterior = grafo_residual.peso(u, v)
	if peso_anterior == valor:
		grafo_residual.remover_arista(u, v)
	else:
		grafo_residual.cambiar_peso(u, v, peso_anterior - valor)
	if not grafo_residual.hay_arista(v, u):
		grafo_residual.agregar_arista(v, u, valor)
	else:
		grafo_residual.cambiar_peso(v, u, peso_anterior + valor)
		
        
def carlos_de_mierda(grafo, casa, escuela):
	red_residual = ford_fulkerson(grafo, casa, escuela)
	flujo = 0
	for v in red_residual.adyacentes(casa):
		flujo += red_residual.peso_arista(v,casa)
	return flujo >=5
	
# Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah
# decidió que en una misma parada de colectivo nunca pararán dos colectivos que usen el mismo
# color. El problema es que ya saben que eso está sucediendo hoy en día, así que van a repintar
# todas las líneas de colectivos. Por problemas presupuestarios, sólo pueden pintar los colectivos
# de k colores diferentes (por ejemplo, k = 4, pero podría se otro valor). Como no quieren parecer
# un grupo de improvisados que malgasta los fondos públicos, quieren hacer un análisis para saber
# si es posible cumplir con lo pedido (pintar cada línea con alguno de los k colores, de tal forma
# que no hayan dos de mismo color coincidiendo en la misma parada).
# Considerando que se tiene la información de todas las paradas de colectivo y qué líneas paran allí,
# modelar el problema utilizando grafos e implementar un algoritmo que determine si es posible resolver
# el problema.
# Indicar la complejidad del algoritmo implementado. 



# Se está formando una nueva comisión de actividades culturales de un pueblo. Cada habitante es miembro de 0 o más
# clubes, y de exactamente 1 partido político. Cada grupo de interés debe nombrar a un representante ante la nueva
# comisión de actividades culturales, con las siguientes restricciones: cada partido político no puede tener más de N/2
# simpatizantes en la comisión, cada persona puede representar a solo un club, cada club debe estar representado por
# un miembro. Implementar un algoritmo que dada la información de los habitantes (a qué clubes son miembros, a
# qué partido pertenecen), nos dé una lista de representantes válidos. Indicar y justificar la complejidad del algoritmo
# implementado.

def partidos_corruptos(dic_clubes, dic_partidos, cant_personas):
	grafo = Grafo
	grafo.agregar_vertice("S")
	grafo.agregar_vertice("F")
	for key in dic_partidos.keys():
		grafo.agregar_vertice(key)
		grafo.unir("F",key,cant_personas//2)
		for persona in dic_partidos[key]:
			if not persona in grafo.vertices():
				grafo.agregar_vertice(persona)
			grafo.unir(key, persona, 1)
	for key in dic_clubes.keys():
		grafo.agregar_vertice(key)
		grafo.unir(key, "S", 1)
		for persona in dic_clubes[key]:
			if not persona in grafo.vertices():
				grafo.agregar_vertice(persona)
			grafo.unir(persona, key, 1)
	flujo = grafo.ford_fulkerson("S", "F")
	participantes = []
	for arista in flujo.keys():
		if arista.origen in dic_partidos.values():
			participantes.append(arista.origen)
	return participantes


def main():
    pass

if __name__ == '__main__':
    main()
