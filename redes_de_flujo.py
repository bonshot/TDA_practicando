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
	
#Se cuenta con una grafo G=(V,E) con capacidad 1 en cada uno de sus ejes. Existen 2 nodos que tomaremos como “s” fuente y “t” sumidero. 
#Podemos determinar el flujo máximo F entre s-t. Se pide proponer un algoritmo eficiente que dado un valor “k”, 
#determine la cantidad mínima de ejes y cuáles de ellos eliminar para que el nuevo flujo máximo sea F-k. Determinar su complejidad y detallar mediante pseudocódigo y una explicación cómo funciona.
#5. Dado un flujo máximo de un grafo, implementar un algoritmo que, si se le aumenta la capacidad a una artista, permita
#   obtener el nuevo flujo máximo en tiempo lineal en vértices y aristas. Indicar y justificar la complejidad del algoritmo
#   implementado.

def main():
    pass

if __name__ == '__main__':
    main()
